def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)
# named({"name": "Bob", "age": 25})  # Error, the dictionary is actually a positional argument.


named(**{"name": "Bob", "age": 25})


# -- Unpacking and repacking --
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)  # Unpack the dictionary into keyword arguments.
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# -- Both args and kwargs --


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)



# -- Error when unpacking --


def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error
