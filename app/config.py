import os
from base64 import b64encode
from flask_babel import lazy_gettext as _

NO_LOGO = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="

class EnvConfig(object):
    SECRET_KEY            = os.getenv('FLASK_SECRET_KEY', b64encode(os.urandom(32)).decode())
    RECAPTCHA_PUBLIC_KEY  = os.getenv('FLASK_RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.getenv('FLASK_RECAPTCHA_PRIVATE_KEY')
    CONTACT_EMAIL         = os.getenv('FLASK_CONTACT_EMAIL', _("your administrator"))
    LOGO                  = os.getenv('FLASK_LOGO', NO_LOGO)


