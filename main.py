#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re 
from datetime import date
from urllib.parse import urlunsplit
from urllib.request import urlopen
from decimal import Decimal


#url = "https://www.facebook.com/login"
url = "https://ya.ru/"

f = urlopen(url)
#urlopen(_url_courses( cur_symbol, beg, end))
print (f)