**mpp**: (**m**)essage(**p**)ack (**p**)rint


#### Description:
```
writing each arg to stdout:
    messagepack(fsencode(arg)) IFF sys.stdout.isatty(); else repr(arg):

You are on a terminal.
You want to write the args you passed to mpp to stdout,
after converting them from the terminal input encoding to the filesystem encoding,
and then wrapping them in the messagepack encoding to preserve their type,
IFF stdout is not a terminal.
Otherwise, write a human readable representation of the result to stdout.

In most setups, this means you enter unicode and write it's UTF-8 byte
representation to the pipe, or it's unicode repr() back to the terminal.
```

#### Psudocode:
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
