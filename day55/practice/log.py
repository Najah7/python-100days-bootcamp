def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}{args}")
        print(f"It returned {func(*args, **kwargs)}")
    return wrapper

@logging_decorator
def add(x, y):
    return x + y

add(1, 2)
