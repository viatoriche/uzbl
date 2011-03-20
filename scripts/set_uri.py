#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File name:    noscript.py
# Author:       Viator (viator@via-net.org)
# License:      GPL (see http://www.gnu.org/licenses/gpl.txt)
# Created:      2010-09-27
# Description:
# TODO:

import sys
import os
from urlparse import urlparse

def xdghome(key, default):
    '''Attempts to use the environ XDG_*_HOME paths if they exist otherwise
    use $HOME and the default path.'''

    xdgkey = "XDG_%s_HOME" % key
    if xdgkey in os.environ.keys() and os.environ[xdgkey]:
        return os.environ[xdgkey]

    return os.path.join(os.environ['HOME'], default)

def get_domain(url):
    '''Return domain segment of url.'''

    if not url.startswith('http'):
        url = "http://%s" % url

    loc = urlparse(url).netloc
    if loc.startswith('www.'):
        loc = loc[4:]

    return loc

def parse_config():
    DATA_DIR = os.path.join(xdghome('DATA', '.local/share/'), 'uzbl/')
    VALIDDOMAIN = os.path.join(DATA_DIR, 'pluginon')
    try:
        domains = open(VALIDDOMAIN, 'r').read().split('\n')
    except:
        domains = []

    return domains
def cut_str(st, length):
    if type(st) != unicode:
        st = unicode(st, 'UTF-8')
    if length < len(st):
        st = '/..%s' % st[-1*length:]
        return st.encode('UTF-8')
    else:
        if st == '/':
            st = ''
        return st.encode('UTF-8')


def main(url, fifo):
    domains = parse_config()
    domain = get_domain(url)
    try:
        fh = open(fifo, "w")
    except:
        sys.stdout.write(fifo+' can\' be write')
        return
    if domain != '':
        fh.write('set cool_uri = %s%s\n' % (domain, cut_str(url.split(domain)[1], 15)))
    fh.close()

if __name__ == "__main__":
    url = sys.argv[6]
    fifo = sys.argv[4]
    #url = 'http://www.ya.ru/'
    #fifo = '/tmp/test'
    main(url, fifo)

# vi: ts=4
