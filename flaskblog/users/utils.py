import secrets
import os
from PIL import Image
from flask_mail import Message
from flaskblog import app, mail
from flask import  url_for


def save_picture(form_picture):
    print(form_picture)
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='noreply329@demo.com', recipients=[user.email])
    msg.body = f'''to reset your password visit following link : 

{url_for('reset_token', token=token, _external=True)} 

IF YOUR DIDNT MAKE THIS REQUEST, THEN SIMPLY IGNORE THIS EMAIL AND NO CHANGES WILL BE MADE.
'''
    mail.send(msg)
