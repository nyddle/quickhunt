import os
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash
from flask.ext.mail import Mail, Message
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)
import pymongo
import bson
import datetime
from werkzeug import check_password_hash, generate_password_hash
from mongokit import Connection, Document
from requests.auth import HTTPBasicAuth
import requests



SECRET_KEY = 'development key'



app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)


# connect to the database
connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
users_collection =  connection.app8222672.users
print users_collection

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active


def get_user_id(email):
    return users_collection.find_one({ 'email' : email })

@app.route('/')
def hello():
    return render_template('registration.html')



@app.route('/add')
def registration():
    return render_template('add.html')

@app.route('/secret')
def registration():
    return render_template('content.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/login')
def registration():
    return render_template('login.html')

@app.route('/<anypage>')
def anypage(anypage):
    return render_template(anypage+'.html')


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
            payload = {'from': 'Excited User <me@samples.mailgun.org>', 'to': request.form['email'], 'subject': 'Quick Hunt account confirmation', 'text': 'http://obscure-springs-3022.herokuapp.com/activate_user/' + str(new_user_id) }
            r = requests.post("https://api.mailgun.net/v2/app8222672.mailgun.org/messages", auth=HTTPBasicAuth('api', 'key-9m9vuzkafbyjqhm9ieq71n0lu9dgf9b9'), data=payload)
            flash('You were successfully registered. Confirm registration and login.')
            return render_template('login.html', error=error) 
    flash('no luck ((')
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


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)


