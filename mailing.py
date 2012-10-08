from flaskext.mail import Message

def send_awaiting_confirm_mail(user):
    """
    Send the awaiting for confirmation mail to the user.
    """
    subject = "We're waiting for your confirmation!!"
    mail_to_be_sent = Message(subject=subject, recipients=[user['email']])
    confirmation_url = url_for('activate_user', user_id=user['_id'], _external=True)
    mail_to_be_sent.body = "Dear %s, click here to confirm: %s" % (user['email'], confirmation_url)
    from app import mail
    mail.send(mail_to_be_sent)

