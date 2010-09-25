#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File name:    getcb.py
# Author:       Viator (viator@via-net.org)
# License:      GPL (see http://www.gnu.org/licenses/gpl.txt)
# Created:      2010-09-24
# Description:
# TODO:

import os
import sys

# \u0418\u043C\u043F\u043E\u0440\u0442\u0438\u0440\u043E\u0432\u0430\u043D\u043D\u044B\u0435 \u0438\u0437 Firefox
def decode_unicode(txt):
    res = ''
    try:
        ln = len(txt)
        i = 0
        while True:
            if i >= ln: break
            if (txt[i] + txt[i+1]) == '\u':
                c = ''
                i += 1
                for j in range(4):
                    i += 1
                    c = c + txt[i]
                c = unichr(int(c, 16)).encode('UTF-8')
                res = res + c
            else:
                res = res + txt[i]
            i += 1
        return res
    except:
        return res

# @class bookmarks
class bookmarks():
    def __init__(self):
        # Initialization
        self.login = os.environ['HOME']
        self.dest = '%s/.config/chromium/Default/Bookmarks' % (self.login)
        self.bmarks = {}

    def read(self):
        try:
            bm = open(self.dest, 'r').read().split('\n')
            for b in bm:
                if b.find('"name":') != -1:
                    name = b.replace('"','')
                    name = name.replace('name:','')
                    name = name.strip()
                    name = decode_unicode(name)
                if b.find('"url":') != -1:
                    url = b.replace('"','')
                    url = url.replace('url:','')
                    url = url.strip()
                    self.bmarks[url] = name

        except:
            sys.stdout.write('Error read %s\n' % (self.dest))

    def show(self):
        #sys.stderr.write('Show all bookmarks:\n')
        for i in self.bmarks:
            sys.stdout.write('%s %s\n' % (i, self.bmarks[i]))

def main():
    b = bookmarks()
    b.read()
    b.show()

if __name__ == "__main__":
    main()

# vi: ts=4
