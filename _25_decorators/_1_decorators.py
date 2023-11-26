def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_hello():
    print("Hello!")


my_decorator(say_hello)()


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello(*, name: str):
    print(f"Hello, {name}!")


say_hello(name="Sasha")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers...")
    return a + b


result = add_numbers(a=10, b=5)
print(f"The result is {result}")
