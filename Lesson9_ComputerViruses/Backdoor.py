# The following format defines a basic authentication scheme:
#
# USERNAME: alice
# PASSWORD: 5!fxoP3
# These credentials are not known to the hacker, so they'd like to add a backdoor to this program,
# so that the username hacker and the password 1234 work. However, they wouldn't want to change the original file,
# so they're thinking of changing its "compiler", which takes this format and generates the following code:
#
# def authenticate(username, password):
#     return username == 'alice' and password == '5!fxoP3'


import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''


def compile_(format_):
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return CODE.format(username=username, password=password)