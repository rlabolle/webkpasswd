from flask import current_app
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length
from flask_babel import lazy_gettext as _

class ChangePasswordForm(FlaskForm):
    username    = StringField(_('Username'), validators=[InputRequired()])
    oldpassword = PasswordField(_('Old password'), validators=[InputRequired()])
    newpassword = PasswordField(_('New password'), validators=[InputRequired(), Length(current_app.config['MIN_PWD_LEN'])])
    conpassword = PasswordField(_('Confirm new password'), validators=[InputRequired(), EqualTo('newpassword', message=_('Passwords must match'))])
    recaptcha   = RecaptchaField()
    submit      = SubmitField(_('Change password'))
