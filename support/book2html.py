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
    dest = '%s/.config/uzbl/bookmarks_with_chromium' % home
    bm = open(dest, 'r').read().split('\n')
    for b in bm:
        bl = b.split(' ')
        try:
            # <p>{DESC}<br />
            # {URL}</p>
            sys.stdout.write('<p>%s<br><a href="%s">%s</a></p>\n' % (' '.join(bl[1:]), bl[0], bl[0]))
        except:
            pass
    return 0

if __name__ == "__main__":
    main()

# vi: ts=4
