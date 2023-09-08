from flask_babel import lazy_gettext as _
from collections import defaultdict

class ErrorMsg(defaultdict):
    def __init__(self, d):
        super().__init__(None, d)
    def __missing__(self, key):
        return _("Unknown error code %(code)d", code=key)

class ChangePasswordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
