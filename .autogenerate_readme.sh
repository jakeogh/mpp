#!/bin/sh

# if stdout is a tty (aka terminal):
#tty:
mpp 'a'

# if stdout is not a tty
mpp 'a' | od -tx1 -v

# where c4 01 61 is:
#  c4: bin8 https://github.com/msgpack/msgpack/blob/master/spec.md#bin-format-family
#  01: one byte long
#  61: a


# compared to
echo -n 'a' | od -tx1 -v
