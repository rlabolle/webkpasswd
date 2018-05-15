from flask_babel import lazy_gettext as _
from collections import defaultdict

class ErrorMsg(defaultdict):
    def __init__(self, d):
        super().__init__(None, d)
    def __missing__(self, key):
        return _("Unknown error code %(code)d", code=key)

changePasswordErrorMsg = ErrorMsg({
  -1765328366: _("Your account is locked out"),
  -1765328360: _("Old password incorrect"),
            4: _("The new password was rejected by the server"),
})

