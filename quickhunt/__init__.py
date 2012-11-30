#!/usr/bin/python
# -*- coding: utf8

import os
import json
import bson
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
import pymongo
from pymongo import Connection

import urllib2
from redis_completion import RedisEngine
import urlparse
import redis
import requests
from requests.auth import HTTPBasicAuth


def create_app(env='debug'):

    """ TODO:
    if config is None:
        config = os.path.join(app.root_path, 'production.cfg')

    app.config.from_pyfile(config)
    """
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.config.update(
        SECRET_KEY=os.urandom(20)
                )
    if (env == 'debug'):
        app.debug=True
    if (env == 'prod'):
        app.debug=False

    if app.debug:
        from flaskext.lesscss import lesscss
        lesscss(app)
    app.static_path = '/static'


    # connect to the database
    connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
    jobs_collection =  connection.app8222672.jobs
    users_collection =  connection.app8222672.users
    url = urlparse.urlparse('redis://:bSpyvbncbJCCMn6sjb@pikachu.ec2.myredis.com:6777')
    autocomplete_engine = RedisEngine(host=url.hostname, port=url.port, password=url.password)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/settings')
    def settings():
        return render_template('settings.html')



    @app.route('/list')
    def list():
        jobs = []
        for job in jobs_collection.find():
            job['id'] = str(job['_id'])
            jobs.append(job)
        return render_template('list.html', jobs=jobs)

    @app.route('/delete/<jobid>')
    def delete(jobid):
        response = jobs_collection.remove({'_id':bson.ObjectId(jobid)});
        if (response == None):
            flash('Job erased')
        else:
            flash('Error occured')
        return redirect(url_for('list'))

    @app.route('/jobs/<jobid>')
    def inside(jobid):
        found_job = jobs_collection.find_one({'_id':bson.ObjectId(oid=str(jobid))});
        found_job['id'] = str(found_job['_id'])
        found_job['objectid'] = str(found_job['_id'])
        found_job['_id'] = str(found_job['_id'])
        return render_template('inside.html', job=found_job)


    @app.route('/edit/<jobid>')
    def edit(jobid):
        return render_template('add.html', job=jobid)

    @app.route('/registration')
    def registration():
        return render_template('registration.html')

    def get_user_id(email):
        return users_collection.find_one({ 'email' : email })

    @app.route('/login')
    def registration():
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        """Registers the user."""
        g.user = None
        if g.user:
            return render_template('registration.html')
        error = None
        if request.method == 'POST':
            if not request.form['email'] or \
                     '@' not in request.form['email']:
                error = 'You have to enter a valid email address'
            elif not request.form['password']:
                error = 'You have to enter a password'
            elif get_user_id(request.form['email']) is not None:
                error = 'The username is already taken'
            else:
                new_user_id = users_collection.save({ 'email' : request.form['email'], 'password' : request.form['password'], 'status' : 'awaiting confirm' })
                payload = {'from': 'Excited User <me@samples.mailgun.org>', 'to': request.form['email'], 'subject': 'Quick Hunt account confirmation', 'text': 'http://quickhunt.herokuapp.com/activate_user/' + str(new_user_id) }
                r = requests.post("https://api.mailgun.net/v2/app8222672.mailgun.org/messages", auth=HTTPBasicAuth('api', 'key-9m9vuzkafbyjqhm9ieq71n0lu9dgf9b9'), data=payload)
                flash('You were successfully registered. Confirm registration and login.')
                return render_template('login.html', error=error) 
        #flash('no luck ((' + request.method + error)
        flash(error)
        return render_template('registration.html', error=error)


    @app.route('/activate_user/<user_id>')
    def activate_user(user_id):
        """
        Activate user function.
        """
        found_user = users_collection.find_one({'_id':bson.ObjectId(oid=str(user_id))});
        if not found_user:
            return abort(404)
        else:
            if found_user['status'] == 'awaiting_confirm':
                ### Setting the user status active here ###*
                payload = {'from': 'Quick Hunt <me@samples.mailgun.org>', 'to': found_user['email'], 'subject': 'Quick Hunt account confirmation', 'text': 'Subscription confirmed.' }
                r = requests.post("https://api.mailgun.net/v2/app8222672.mailgun.org/messages", auth=HTTPBasicAuth('api', 'key-9m9vuzkafbyjqhm9ieq71n0lu9dgf9b9'), data=payload)
                flash('user has been activated', 'info')
            elif found_user['status'] == 'active':
                flash('user already activated', 'info')
            return redirect(url_for('content'))


    """ This is the API part of the equation """

    @app.errorhandler(404)
    def not_found(error=None):
        message = {
                'status': 404,
                'message': 'Not Found: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    @app.route('/api/search/', methods = ['GET'])
    @app.route('/api/search/<query>', methods = ['GET'])
    def search(query=None):
        jobs = []
        for job in jobs_collection.find():
            job['_id'] = str(job['_id'])
            jobs.append(job)
        return jsonify({'result':jobs})



    @app.route('/api/jobs/<jobid>', methods = ['GET'])
    def get_job(jobid):
        found_job = jobs_collection.find_one({'_id':bson.ObjectId(oid=str(jobid))});
        found_job['id'] = str(found_job['_id'])
        found_job['objectid'] = str(found_job['_id'])
        found_job['_id'] = str(found_job['_id'])
        #if userid in users:
        return jsonify(found_job)
        #else:
        #    return not_found()
        #return undef

    @app.route('/api/jobs/new', methods = ['POST'])
    def create_job():
        js = json.dumps(request.data)
        json_data = json.loads(request.data)
        jobs_collection.save(json_data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    @app.route('/api/jobs/<jobid>', methods = ['PUT'])
    def update_job(jobid):
        js = json.dumps(request.data)
        print 'js:' + str(js)
        json_data = json.loads(request.data)
        json_data['_id'] = bson.ObjectId(json_data['objectid'])
        jobs_collection.save(json_data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    @app.route('/api/jobs/<jobid>', methods = ['DELETE'])
    def delete_job(jobid):
        response = jobs_collection.remove({'_id':bson.ObjectId(jobid)});
        if (response == None):
            return jsonify({success:'Success'})
        else:
            return jsonify({error:'Error'})

    @app.route('/api/autocomplete/', methods = ['GET'])
    def autocomplete():
        js = {}
        searchword = request.args.get('q', '')
        if searchword:
            js = json.dumps({'result': autocomplete_engine.search(searchword)})
        else:
            js = {'error':'invalid argument'}
        return Response(js, status=200, mimetype='application/json')

    return app


