#!/usr/bin/env python3
import os
import logging
from base64 import b64decode
from flask import Flask, render_template, flash, request, make_response
from flask_babel import Babel
from flask_babel import lazy_gettext as _
from errors import ChangePasswordError
from forms import ChangePasswordForm
from config import EnvConfig

app = Flask(__name__)
app.config.from_object(EnvConfig)
app.config.from_envvar('FLASK_CONFIG')

match app.config.get('CHPASSWD'):
    case 'kpasswd':
        from kpasswd import chgpasswd
    case 'smbpasswd':
        from smbpasswd import chgpasswd

def get_locale():
    supported = ['fr', 'en']
    default = 'fr'
    if 'lang' in request.args and request.args['lang'] in supported:
        return request.args['lang']
    return request.accept_languages.best_match(supported, default)

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

@app.route("/", methods=["GET","POST"])
def index():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        try:
            chgpasswd(form.username.data,form.oldpassword.data,form.newpassword.data)
        except ChangePasswordError as e:
            errmsg = e.message
            app.logger.info(f'[UserError] {form.username.data}: {errmsg} ({e.internalerror})')
            flash(errmsg,'error')
        else:
            flash(_("Password successfully changed"),'success')
            return render_template("success.html")
    return render_template("index.html", form=form, contact_email=app.config.get('CONTACT_EMAIL'))

@app.route("/logo.png")
def logo():
    response=make_response(b64decode(app.config.get('LOGO')))
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route("/healthz")
def healthz():
    return "ok"

if __name__ == "__main__":
    app.testing = True
    app.logger.setLevel(logging.DEBUG)
    app.run()
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

