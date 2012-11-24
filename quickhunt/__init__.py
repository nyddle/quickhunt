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


