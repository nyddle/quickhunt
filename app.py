import os
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash
from flask.ext.mail import Mail, Message
import pymongo
from mongokit import Connection, Document


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




def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate

"""
   structure = {
                'title':unicode,
                'body':unicode,
                'author':unicode,
                'date_creation':datetime.datetime,
                'rank':int
                }
"""
class User(Document):
    structure = {
        'name': unicode,
        'email': unicode,
    }
    validators = {
        'name': max_length(50),
        'email': max_length(120)
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.name)

connection.register([User])



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


