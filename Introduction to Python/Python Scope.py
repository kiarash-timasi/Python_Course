# 4 type of scope in python(Local ,Enclosing ,Global ,Built-in)
#Local:
def my_function():
    x = 10  # Local variable
    print(x)
my_function()  # Output: 10
#print(x)   Error: NameError: name 'x' is not defined

#Enclosing Scope:
def outer_function():
    x = 20  # Enclosing variable
    def inner_function():
        print(x)  # Accessing enclosing variable
    inner_function()
outer_function()  # Output: 20

#Global:
x = 30  # Global variable
def my_function():
    print(x)  # Accessing global variable
my_function()  # Output: 30
print(x)  # Output: 30

#Built-in:
print(len("Hello"))  # len is a built-in function

