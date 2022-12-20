def alarm(callback):
    def wrapper(*args, **kwargs):
        print("SQUEAK")
        callback(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
    @alarm
    def any_func():
        print("THis function has a decorator and that decorator screams so loud, be careful")

    
    any_func()
