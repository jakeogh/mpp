#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

import os
import sys
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal

import msgpack

signal(SIGPIPE, SIG_DFL)


def main():
    if len(sys.argv) < 2:
        print('Usage: mpp PATH...', file=sys.stderr)
        sys.exit(1)

    tty = sys.stdout.isatty()
    argvb = list(map(os.fsencode, sys.argv[1:]))
    found_arg = False
    for arg in argvb:
        if len(arg) == 0:
            continue
        found_arg = True
        if tty:
            sys.stdout.write(repr(arg) + '\n')
            continue
        sys.stdout.buffer.write(msgpack.packb(arg))
    return not found_arg
