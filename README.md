**mpp**: (**m**)essage(**p**)ack (**p**)rint


#### Description:
```
writing each arg to stdout:
    messagepack(fsencode(arg)) IF sys.stdout.isatty(); ELSE repr(arg):

You are using a terminal.

IF stdout is not a terminal:
    convert each arg passed to mpp:
        from:   the terminal input encoding
        to:     the local filesystem encoding `os.fsencode(arg)`
        thento: messagepack(arg)
ELSE:
    convert each arg passed to mpp:
        from:   the terminal input encoding
        to:     the local filesystem encoding `os.fsencode(arg)`
        thento: repr(arg)

Messagepack will preserve it's type for other applications that assume messagepacked stdin;

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
