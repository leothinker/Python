try:
    raise KeyboardInterrupt("This is an exception")
except Exception as e:
    print("programs go to here:")
    print(e)
