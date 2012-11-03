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


def create_app(env='debug'):

    SECRET_KEY = 'development key'
    """ TODO:
    if config is None:
        config = os.path.join(app.root_path, 'production.cfg')

    app.config.from_pyfile(config)
    """
    app = Flask(__name__)
    app.config.from_object(__name__)
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


    @app.route('/')
    def hello():
        return render_template('home.html')


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

    @app.route('/api/search/<query>', methods = ['GET'])
    def search(query):
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

    @app.route('/api/jobs/<jobid>', methods = ['POST'])
    def create_job(jobid):
        js = json.dumps(request.data)
        print 'js:' + str(js)
        json_data = json.loads(request.data)
        if (json_data['objectid'] != 'new'):
            json_data['_id'] = bson.ObjectId(json_data['objectid'])
        jobs_collection.save(json_data)
        print str(json_data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    @app.route('/api/jobs/<jobid>', methods = ['DELETE'])
    def delete_job(jobid):
        response = jobs_collection.remove({'_id':bson.ObjectId(jobid)});
        if (response == None):
            return jsonify({success:'Success'})
        else:
            return jsonify({error:'Error'})

    return app


