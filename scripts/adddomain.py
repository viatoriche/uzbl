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

def get_filename(filename):
    data_dir = os.path.join(xdghome('DATA', '.local/share/'), 'uzbl/')
    return os.path.join(data_dir, filename)

def parse_config(filename):
    filename = get_filename(filename)
    try:
        domains = open(filename, 'r').read().split('\n')
    except:
        domains = []

    return domains

def main(url, filename):
    domains = parse_config(filename)
    domain = get_domain(url)
    filename = get_filename(filename)

    if domain not in domains:
        try:
            fh = open(filename, "a")
        except:
            fh = open(filename, "w")
        fh.write('%s\n' % domain)
        fh.close()

if __name__ == "__main__":
    url = sys.argv[6]
    filename = sys.argv[8]
    #url = 'http://www.ya.ru/'
    #fifo = '/tmp/test'
    main(url, filename)

# vi: ts=4
