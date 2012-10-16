import os
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash
from flask.ext.mail import Mail, Message
import pymongo
from pymongo import Connection


SECRET_KEY = 'development key'



app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
mail = Mail(app)
if app.debug:
    from flaskext.lesscss import lesscss
    lesscss(app)
app.static_path = 'static'


# connect to the database
connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
users_collection =  connection.app8222672.users
print users_collection


@app.route('/')
def hello():
    return render_template('add.html')



@app.route('/add')
def registration():
    return render_template('add.html')


@app.route('/<anypage>')
def anypage(anypage):
    return render_template(anypage+'.html')



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


