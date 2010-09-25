#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File name:    book2html.py
# Author:       Viator (viator@via-net.org)
# License:      GPL (see http://www.gnu.org/licenses/gpl.txt)
# Created:      2010-09-24
# Description:
# TODO:

import sys
import os

def main():
    home = os.environ['HOME']
    dest = '%s/.config/uzbl/history' % home
    bm = open(dest, 'r').read().split('\n')
    bm = bm[-100:]
    for b in bm:
        bl = b.split(' ')
        try:
            # <p>{DESC}<br />
            # {URL}</p>
            sys.stdout.write('<p>%s - %s<br><a href="%s">%s</a></p>\n' % (' '.join(bl[0:2]), ' '.join(bl[3:]), bl[2], bl[2]))
        except:
            pass
    return 0

if __name__ == "__main__":
    main()

# vi: ts=4
