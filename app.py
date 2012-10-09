import os
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash
from flask.ext.mail import Mail, Message
from werkzeug import check_password_hash, generate_password_hash

from mongokit import Connection, Document


SECRET_KEY = 'development key'



app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

# connect to the database
connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate

@connection.register
class User(Document):
    structure = {
        'password': unicode,
        'email': unicode,
    }
    validators = {
        'password': max_length(120),
        'email': max_length(120)
    }
    required_fields = ['password', 'email']
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.email)

    #database:app8222672



user =  connection.app8222672.users.User()
user.passwors = u'password'
user.email = u'email@host.com'
user.save()

@app.route('/')
def hello():
    return render_template('registration.html')


def send_awaiting_confirm_mail(user):
    """
    send the awaiting for confirmation mail to the user.
    """
    subject = "we're waiting for your confirmation!!"
    mail_to_be_sent = Message(subject=subject, recipients=[user['email']], sender='nyddle@heroku.com')
    confirmation_url = url_for('activate_user', user_id=user['_id'], _external=True)
    mail_to_be_sent.body = "dear %s, click here to confirm: %s" % (user['email'], confirmation_url)
    from app import mail
    mail.send(mail_to_be_sent)

def send_subscription_confirm_mail(user):
    """
    send the awaiting for confirmation mail to the user.
    """
    subject = "we're waiting for your confirmation!!"
    mail_to_be_sent = Message(subject=subject, recipients=[user['email']])
    confirmation_url = url_for('activate_user', user_id=user['_id'], _external=True)
    mail_to_be_sent.body = "dear %s, click here to confirm: %s" % (user['email'], confirmation_url)
    from app import mail
    mail.send(mail_to_be_sent)


@app.route('/registration')
def registration():
    return render_template('registration.html')

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
        #elif request.form['password'] != request.form['password2']:
        #    error = 'The two passwords do not match'
        #elif get_user_id(request.form['username']) is not None:
        #    error = 'The username is already taken'
        else:
            new_user = {'_id' : 'someid', 'email' : request.form['email'], 'password' : request.form['password'] }
            send_awaiting_confirm_mail(new_user)
            #flash(messages.EMAIL_VALIDATION_SENT, 'info')
            flash('You were successfully registered and can login now')
            return render_template('login.html', error=error) 

            """
            g.db.execute('''insert into user (
username, email, pw_hash) values (?, ?, ?)''',
                [request.form['username'], request.form['email'],
                 generate_password_hash(request.form['password'])])
            g.db.commit()
            """
    flash('no luck ((')
    return render_template('registration.html', error=error)





@app.route('/activate_user/<user_id>')
def activate_user(user_id):
    """
    Activate user function.
    """
    found_user = {}### Getting user in db from id here ###*
    if not found_user:
        return abort(404)
    else:
        if found_user['status'] == 'awaiting_confirm':
            ### Setting the user status active here ###*
            send_subscription_confirmed_mail(found_user)
            flash('user has been activated', 'info')
        elif found_user['status'] == 'active':
            flash('user already activated', 'info')
        return redirect(url_for('login'))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)


