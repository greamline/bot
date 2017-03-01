#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re 
from datetime import date
from urllib.parse import urlunsplit
from urllib.request import urlopen
from decimal import Decimal

_CUR_CODES = {
    'EUR': 'R01239'
}


def _url_courses( cur_symbol, beg, end):

    request = {
        'VAL_NM_RQ' :_CUR_CODES [cur_symbol],
        'date_req1' :beg.strftime('%d.%m.%Y'),
        'date_req2' :end.strftime('%d.%m.%Y'),
        'rt'        : '1',
        'mode'      : '1',
    }

    
    url = (
        'http',
        'www.cbr.ru',
        'currency_base/dynamics.aspx',
        '&'.join(('{0}={1}'.format(k , v) for k, v in request.items() )),
        '',
    )



    return urlunsplit(url)


def _read_lines ( source, *, encoding='utf-8', chunk=1024 ): 
    rest = int(source.getheader('Content-length'))
    Buffer = b'' #Байтовая строка
    while rest > 0:
        while rest > 0 and not ( b'\n' in Buffer ):
            A = source.read( min(chunk,rest) )
            if not A: break
            Buffer += A
            rest -= len(A)
        if b'\n' in Buffer: 
            #(Значит файл до конца не дочитан)
            while b'\n' in Buffer:
                line, Buffer = Buffer.split(b'\n', maxsplit=1)
                yield line.decode(encoding)
            continue
        elif Buffer:
            yield Buffer.decode(encoding)
            break
            
            
           
_DATA = re.compile (r'''
                    <td>
                    (\d\d).\(d\d).\(d\d\d\d)  
                    </td><td>
                    (\d+)
                    </td><td>
                    (\d+(?:,\d+)?)
                    </td>
                    ''' , re.VERBOSE )
                   
                   # \d' - нетерминальный символ означающий цифру, '.' - вообще любой символ. , re.VERBOSE - расширенный регулярных выражений
                   
def get_courses (cur_symbol, beg, end ):
    
    #source = urlopen(_url_courses( cur_symbol, beg, end))
    
    with urlopen(_url_courses( cur_symbol, beg, end)) as source:
    
        for line in _read_lines(source , encoding=('utf-8')):
            M = _DATA.search( line )
            if not M: continue
            day, month, year, count, course = M.groups()
            dt = date( int(year), int(month), int(day) )
            count = int(count)
            course = Decimal( '.'.join( course.split('.')))
            yield (dt, count, course)
 
    #source.close()