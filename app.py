import os
from flask import Flask, render_template
from flask.ext.mail import Mail
import mailing


app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def hello():
    return render_template('registration.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if form.validate_on_submit():
        ### Registering the new user here* ###
        mailing.send_awaiting_confirm_mail(new_user)
        flash(messages.EMAIL_VALIDATION_SENT, 'info')
        return redirect(url_for('index'))
    else:
        if not g.user:
            return render_template('register.html', form=form)
        else:
            return redirect(url_for('index'))

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


