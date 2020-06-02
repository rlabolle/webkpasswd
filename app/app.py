#!/usr/bin/env python3
import os
import logging
from base64 import b64decode
from flask import Flask, render_template, flash, request, make_response
from flask_babel import Babel
from flask_babel import lazy_gettext as _
from kerberos import changePassword, PwdChangeError
from errors import changePasswordErrorMsg
from forms import ChangePasswordForm
from config import EnvConfig
import pwnedpasswords

app = Flask(__name__)
app.config.from_object(EnvConfig)
app.config.from_envvar('FLASK_CONFIG')
app.logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)
app.logger.setLevel(logging.INFO)

babel = Babel(app)
@babel.localeselector
def get_locale():
    supported = ['fr', 'en']
    default = 'fr'
    if 'lang' in request.args and request.args['lang'] in supported:
        return request.args['lang']
    return request.accept_languages.best_match(supported, default)


@app.route("/", methods=["GET","POST"])
def index():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        try:
            changePassword(form.username.data,form.oldpassword.data,form.newpassword.data)
        except PwdChangeError as e:
            while isinstance(e.args,tuple) and len(e.args) == 1:
                e.args = e.args[0]
            flash(changePasswordErrorMsg[e.args[1]], 'error')
            if e.args[1] == 4:
                try:
                    seen = pwnedpasswords.check(form.newpassword.data, plain_text=True)
                    if seen > 0:
                        flash(_("This password has been seen %(value)d times before", value=seen), 'error')
                        flash(_("This password has previously appeared in a data breach and should never be used"), 'warning')
                except:
                    pass
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
    app.run()

