#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import sys
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal

import msgpack

signal(SIGPIPE, SIG_DFL)


# since this is py3.8+, sys.argv: list[str]
def main():
    if len(sys.argv) < 2:
        print("Usage: mpp [PATH]...", file=sys.stderr)
        sys.exit(1)

    tty = sys.stdout.isatty()
    # https://docs.python.org/3/library/os.html#python-utf-8-mode
    # https://vstinner.github.io/pep-383.html
    # https://github.com/python/cpython/blob/3.10/Lib/os.py#L804
    # def fsencode():
    #  filename.encode(encoding, errors)
    #  filename.encode('utf8', 'surrogateescape')
    # argvb = list(map(os.fsencode, sys.argv[1:]))
    argvb = map(os.fsencode, sys.argv[1:])
    found_arg = False
    for arg in argvb:
        if len(arg) == 0:
            continue
        found_arg = True
        if tty:
            sys.stdout.write(repr(arg) + "\n")
            continue
        sys.stdout.buffer.write(msgpack.packb(arg))
    return not found_arg
