#defining function
def greeting(name):
    print(f"Hello {name}")
#calling function
greeting("Bob")

#Function arguments
#(*args)
def fruits (*args):
    for fruit in args:
        print(fruit)
fruits ("apple", "banana", "cherry")

#(**kwargs)
def namedic (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
namedic(apple="1", banana="2", cherry="3")

#Lambda function
add = lambda x, y: x + y
print(add(1, 2))

#Nested function
def outer_function():
    def inner_function():
        print( "Hello Word!" )
    inner_function()
outer_function()

def outer(x):
    def inner(y):
        return x + y
    return inner
sum = outer(2)
print(sum(5))

#Decorators
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
