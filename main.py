#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re 
import datetime
from datetime import date
from urllib.parse import urlunsplit
#from urllib.request import urlopen
from decimal import Decimal
import urllib.request

cur = 'R01010'
beg = '20.01.2016'
end = '27.01.2017'

url = 'https://www.cbr.ru/currency_base/dynamics.aspx?VAL_NM_RQ=' + cur + '&date_req1=' + beg + '&date_req2=' + end + '&rt=1&mode=1'


with urllib.request.urlopen(url) as response:
   html = response.read()

value =  re.findall(r'(?i)<td.*?>([^<]+)</td.*?>', str(html))




  
for line in value : 
    print ('value1 : ' , line)
        
            
            
            
            
#TD =    re.findall(r'(?i)<td.*?>([^<]+)</td.*?>', html)
   
#print (html)