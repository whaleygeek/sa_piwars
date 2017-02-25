import microbit # will auto connect

while True:
    msg = microbit.read()
    if msg is not None:
        print(msg)

