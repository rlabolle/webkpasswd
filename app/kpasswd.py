from flask_babel import lazy_gettext as _
from errors import ErrorMsg, ChangePasswordError
from kerberos import changePassword, PwdChangeError
import pwnedpasswords

changePasswordErrorMsg = ErrorMsg({
  -1765328366: _("Your account is locked out"),
  -1765328360: _("Old password incorrect"),
            4: _("The new password was rejected by the server"),
})

def chgpasswd(username, oldpassword, newpassword):
    try:
        changePassword(username,oldpassword,newpassword)
    except PwdChangeError as e:
        while isinstance(e.args,tuple) and len(e.args) == 1:
            e.args = e.args[0]
        errmsg = changePasswordErrorMsg[e.args[1]]
        if e.args[1] == 4:
            try:
                seen = pwnedpasswords.check(form.newpassword.data, plain_text=True)
                if seen > 0:
                    errmsg = _("This password has been seen %(value)d times before in data breaches", value=seen)
            except:
                pass
        raise ChangePasswordError(errmsg, e)
    except Exception as e:
        raise ChangePasswordError(changePasswordErrorMsg[0], e)
