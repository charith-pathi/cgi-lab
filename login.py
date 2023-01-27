#!/usr/bin/env python3

import cgi
import cgitb
from pickle import NONE
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import json
import secret
from http.cookies import SimpleCookie

# Initialize login form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# Initialize cookie to save username and password
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None

# Tests if form username and password are equivalent to the username and
# and password on secret.py
form_ok = username == secret.username and password == secret.password

if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# Test if cookie username and password is correct
if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_ok:
   print(f"Set-Cookie: username={username}")
   print(f"Set-Cookie: password={password}")

print()

# Load login page. If username and password matches, show the secret page
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    # Otherwise, show the incorrect login page
    print(login_page())
    print(after_login_incorrect())