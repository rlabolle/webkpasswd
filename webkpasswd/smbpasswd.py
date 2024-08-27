from flask import current_app
from flask_babel import lazy_gettext as _
from impacket.dcerpc.v5 import transport, samr
from pprint import pprint
import pwnedpasswords

from .errors import ErrorMsg, ChangePasswordError

changePasswordErrorMsg = ErrorMsg({
   0xc000006A: _("Old password incorrect or wrong username"),
   0xc000006B: _("The new password was rejected by the server"),
   0xC000006C: _("The new password was rejected by the server"),
})

def chgpasswd(username, oldpassword, newpassword):
    try:
        rpctransport = transport.SMBTransport(current_app.config['SMB_SERVER'], filename=r'\samr')
        rpctransport.set_credentials(username='', password='', domain='', lmhash='', nthash='', aesKey='')
        dce = rpctransport.get_dce_rpc()
        dce.connect()
        dce.bind(samr.MSRPC_UUID_SAMR)
        resp = samr.hSamrUnicodeChangePasswordUser2(dce, '\x00', username, oldpassword, newpassword)
        dce.disconnect()
    except samr.DCERPCSessionError as e:
        errmsg = changePasswordErrorMsg[e.error_code]
        if e == 0xC000006C:
            try:
                seen = pwnedpasswords.check(form.newpassword.data, plain_text=True)
                if seen > 0:
                    errmsg = _("This password has been seen %(value)d times before in data breaches", value=seen)
            except:
                pass
        raise ChangePasswordError(errmsg, e)
    except Exception as e:
        raise ChangePasswordError(changePasswordErrorMsg[0], e)
