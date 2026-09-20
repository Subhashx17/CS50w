def announce(f):
    def wrapper():
        print("About to run the fucntion....\n")
        f()
        print("\nDone with the function saar")
    return wrapper


@announce
def hello():
    print("Hello world")

hello()