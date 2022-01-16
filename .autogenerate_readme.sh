#!/bin/sh

# if stdout is a tty (aka terminal):
#tty:
mpp 'a'

# if stdout is not a tty
mpp 'a' | od -tx1 -v
