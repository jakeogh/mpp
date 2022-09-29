**mpp**: (**m**)essage(**p**)ack (**p**)rint


#### Description:
```
writing each arg to stdout:
    messagepack(fsencode(arg)) IFF sys.stdout.isatty(); else repr(arg):

You are using a terminal.
You want to convert each arg you passed to mpp,
from the terminal input encoding,
to the local filesystem encoding.
Then you want to take each arg (which is now a typed python object),
and wrap it in messagepack.
Messagepack will preserve it's type for other applications that assume messagepacked stdin;
IFF stdout is not a terminal.
IFF stdout is a terminal, write a human readable representation of the result to it.

In most setups, this means you enter unicode and write it's UTF-8 byte
representation (messagepacked) to the pipe, or it's unicode repr() back to the terminal.
```

#### pyPsudocode:
```
stdin: not read from, explicitely closed on startup
env (`man 1p export`): not explicitly used
args: N <= `getconf ARG_MAX`
stdout:
    args = map(os.fsencode, sys.argv[1:])
    for arg in args:
        if tty:
            print(repr(arg))
        else:
            print(messagepack(arg))
```
#### Examples:
```
$ mpp
Usage: mpp [ARG]...

$ # if stdout is a tty (aka terminal):
$ mpp 'a'
b'a'

$ # if stdout is not a tty:
$ mpp 'a' | od -tx1 -v
0000000 c4 01 61
0000003

$ # where c4 01 61 is:
$ #  c4: bin8 https://github.com/msgpack/msgpack/blob/master/spec.md#bin-format-family
$ #  01: one byte long
$ #  61: a

$ # compared to:
$ echo -n 'a' | od -tx1 -v
0000000 61
0000001

```
