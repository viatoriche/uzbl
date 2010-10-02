#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File name:    cmd.py
# Author:       Viator (viator@via-net.org)
# License:      GPL (see http://www.gnu.org/licenses/gpl.txt)
# Created:      2010-10-01
# Description:
# TODO:
import os

def run(cmd, args, uri, fifo):
    if cmd == '!':
        os.system(' '.join(args))
    if (cmd == 'quit') or (cmd == 'exit') or (cmd == 'q'):
        os.system('echo exit > %s' % fifo)
    if (cmd == 'w') or (cmd == 'write'):
        os.system('echo event SAVE_REQUEST > %s' % fifo)
    if (cmd == 'u') or (cmd == 'uri') or (cmd == 'o') or (cmd == 'open'):
        os.system('echo uri %s > %s' % (' '.join(args), fifo))

def main():
    import sys, os
    uri = sys.argv[6]
    fifo = sys.argv[4]
    cmd = sys.argv[8].strip()

    if cmd[0] == '!':
        if len(cmd) <= 1:
            return
        cmd = cmd[1:].strip()
        cmd = '! ' + cmd

    cmd = cmd.split(' ')
    if len(cmd) == 1:
        cmd.append('')
    #os.sustem('xmessage %s' % cmd)
    run(cmd[0], cmd[1:], uri, fifo)
    return 0

if __name__ == "__main__":
    main()

# vi: ts=4
