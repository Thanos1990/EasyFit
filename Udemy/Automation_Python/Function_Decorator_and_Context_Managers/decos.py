def greet(func):
    def decorated_func(*args, **kwargs):
        print("Hello!")
        return func(*args, **kwargs)
    return decorated_func

