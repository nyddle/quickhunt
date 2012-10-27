# -*- coding: utf-8 -*-
import os
import json
import bson
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
import pymongo
from pymongo import Connection


SECRET_KEY = 'development key'



app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
if app.debug:
    from flaskext.lesscss import lesscss
    lesscss(app)
app.static_path = 'static'


# connect to the database
connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
jobs_collection =  connection.app8222672.jobs


@app.route('/')
def hello():
    return render_template('add.html')


@app.route('/list')
def list():
    #found_user = users_collection.find_one({'_id':bson.ObjectId(oid=str(user_id))});
    jobs = []
    for job in jobs_collection.find():
        job['id'] = str(job['_id'])
        jobs.append(job)
    return render_template('list.html', jobs=jobs)


@app.route('/edit')
def registration():
    return render_template('add.html')


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/jobs', methods = ['GET'])
def get_job():
    users = {'1':'john', '2':'steve', '3':'bill'}
    
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()
	return undef

@app.route('/jobs', methods = ['POST'])
def create_job():
	#print "POST:" + request.data
	js = json.dumps(request.data)
	json_data = json.loads(request.data)
	print json_data
	resp = Response(js, status=200, mimetype='application/json')
	return resp

@app.route('/jobs', methods = ['DELETE'])
def delete_job():
	return undef




#datetime.datetime.utcnow()
"""
@app.route('/<anypage>')
def anypage(anypage):
    return render_template(anypage+'.html')
"""


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

"""
  <form name="add_job" action="">
      <label>Вакансия: <input type="text" name="job_title"></label>
      <label>Категория: <input type="password" name="job_category"></label>
        <span><input type="radio" name="job_employment" value="full_time" checked="checked"> полная</span>
        <span><input type="radio" name="job_employment" value="part_time"> частичная</span>
        <span><input type="radio" name="job_workplace" value="office" checked="checked"> офис</span>
        <span><input type="radio" name="job_workplace" value="remote"> удаленно</span>
        <textarea name="job_description"></textarea>
        <textarea name="job_charge"></textarea>
        <textarea name="job_experience"></textarea>
        <textarea name="job_additional"></textarea>
        <textarea name="job_terms"></textarea>

      <label>Компания: <input type="text" name="company_name"></label>
        <textarea name="company_description"></textarea>
      <label>Лого: <input type="file" name="company_logo"></label>

"""

