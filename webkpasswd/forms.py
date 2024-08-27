from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo
from flask_babel import lazy_gettext as _

class ChangePasswordForm(FlaskForm):
    username    = StringField(_('Username'), validators=[DataRequired()])
    oldpassword = PasswordField(_('Old password'), validators=[DataRequired()])
    newpassword = PasswordField(_('New password'), validators=[InputRequired()])
    conpassword = PasswordField(_('Confirm new password'), validators=[InputRequired(), EqualTo('newpassword', message=_('Passwords must match'))])
    recaptcha   = RecaptchaField()
    submit      = SubmitField(_('Change password'))
