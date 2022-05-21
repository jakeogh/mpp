**mpp**: (**m**)essage(**p**)ack (**p**)rint

#### Psudocode:
```
stdin: closed
env: not explicitly used
args: N <= `getconf ARG_MAX`
stdout:
    for arg in args:
        if tty:
            print(repr(arg))
        else:
            print(messagepack(arg))
```
#### Examples:
```
$ mpp
Usage: mpp [PATH]...

$ # if stdout is a tty (aka terminal):
$ mpp 'a'
b'a'

$ # if stdout is not a tty
$ mpp 'a' | od -tx1 -v
0000000 c4 01 61
0000003

$ # where c4 01 61 is:
$ #  c4: bin8 https://github.com/msgpack/msgpack/blob/master/spec.md#bin-format-family
$ #  01: one byte long
$ #  61: a
```
