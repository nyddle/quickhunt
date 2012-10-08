import os
from flask import Flask, render_template
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash
from flask.ext.mail import Mail
#import mailing
from werkzeug import check_password_hash, generate_password_hash




app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def hello():
    return render_template('registration.html')

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
            mailing.send_awaiting_confirm_mail(new_user)
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
            mailing.send_subscription_confirmed_mail(found_user)
            flash('user has been activated', 'info')
        elif found_user['status'] == 'active':
            flash('user already activated', 'info')
        return redirect(url_for('login'))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


