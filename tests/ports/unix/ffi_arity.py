try:
    import ffi
except ImportError:
    print("SKIP")
    raise SystemExit


def ffi_open(names):
    for name in names:
        try:
            return ffi.open(name)
        except OSError:
            pass
    print("SKIP")
    raise SystemExit


libc = ffi_open(("libc.so", "libc.so.6", "libc.so.0", "libc.so.7", "libc.dylib"))
puts = libc.func("i", "puts", "s")

for args, kwargs in (((), {}), (("one", "two"), {}), ((), {"string": "one"})):
    try:
        puts(*args, **kwargs)
    except TypeError:
        print("TypeError")
