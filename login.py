#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re 
from datetime import date
from urllib.parse import urlunsplit
#from urllib.request import urlopen
from decimal import Decimal
import urllib.request
import urllib

#WWW-Authenticate: Basic realm="cPanel Users"

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

username = "user"
password = "password"

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
a_url = "http://example.com/"
# use the opener to fetch a URL
opener.open(a_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
print (urllib.request.install_opener(opener))