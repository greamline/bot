#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re 
from datetime import date
from urllib.parse import urlunsplit
#from urllib.request import urlopen
from decimal import Decimal
import urllib.request

with urllib.request.urlopen('https://www.facebook.com/login') as response:
   html = response.read()
   
print (html)