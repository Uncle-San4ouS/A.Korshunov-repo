import re

def email_check(email):
    email_re = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not email_re.match(email):
        raise ValueError(f'wrong format: {email}')
    print(email_re.match(email).groupdict())

try:
    email_check('unclesan4ous@ya.ru')
    email_check('uncle$an4ous@yaru')
    email_check('UncleSan4ouS@yaru')
except ValueError as err:
    print(err)