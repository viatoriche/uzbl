#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File name:    cutstr.py
# Author:       Viator (viator@via-net.org)
# License:      GPL (see http://www.gnu.org/licenses/gpl.txt)
# Created:      2010-10-09
# Description:
# TODO:

def cut_str(st, length):
    if type(st) != unicode:
        st = unicode(st, 'UTF-8')
    if length < len(st):
        st = '%s...' % st[:length]
        return st.encode('UTF-8')
    else:
        return st.encode('UTF-8')


def main():
    import sys
    try:
        text = sys.argv[1]
    except:
        sys.stderr.write('text params need')
        return 0
    try:
        length = sys.argv[2]
        length = int(length)
    except:
        length = 20
    sys.stdout.write(cut_str(text, length))
    return 0

if __name__ == "__main__":
    main()

# vi: ts=4
