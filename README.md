## Webkpasswd

This is a web interface to the kpasswd or smbpasswd protocols to change your password in an Active Directory or Samba AD environment.

## Installation

```
pip install webkpasswd[krb]

or

pip install webkpasswd[smb]
```

## Running

```
gunicorn webkpasswd:app
```

## Configuration

You can specify the configuration file path with the `FLASK_CONFIG` variable.

Example configuration file:

```
RECAPTCHA_PRIVATE_KEY = '<recaptcha or hcaptcha private key>'
RECAPTCHA_PUBLIC_KEY = '<recap or hcaptcha public key>'
RECAPTCHA_SCRIPT = 'https://hcaptcha.com/1/api.js'
RECAPTCHA_VERIFY_SERVER = 'https://hcaptcha.com/siteverify'
RECAPTCHA_DIV_CLASS = 'h-captcha'
SECRET_KEY = 'SomeRandomString'
CONTACT_EMAIL = 'support@example.com'
LOGO = '<Base64 encoded png logo>'
CHPASSWD = 'kpasswd' or 'smbpasswd'
MIN_PWD_LEN = 12
SMB_SERVER = 'dc1.example.com'
```

## License

Licensed under either of

 * Apache License, Version 2.0
   ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license
   ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
