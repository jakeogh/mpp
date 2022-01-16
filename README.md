mpp: (m)essage(p)ack (p)rint

```
stdin: none
args: N <= `getconf ARG_MAX`
stdout:
    if tty:
        print(messagepack(arg))
    else:
        print(repr(arg))
```
```
$ mpp
Usage: mpp PATH...

$ # if stdout is a tty (aka terminal):
$ mpp 'a'
b'a'

$ # if stdout is not a tty
$ mpp 'a' | od -tx1 -v
0000000 c4 01 61
0000003

```
