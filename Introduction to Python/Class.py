class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#----------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")

p1 = Person("John", 36)
p1.greet()
#----------------------------------------------------------
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)      # Output: Buddy
print(dog.species)   # Output: Dog
print(dog.breed)     # Output: Golden Retriever
dog.make_sound()     # Output: Woof!

#-------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

# Creating an instance of Student
student = Student("Alice", 20, "S12345")
student.display()
#----------------------------------------------------------------
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

for num in my_iter:
    print(num)
#------------------------------------------------------------
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Using polymorphism
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
#-------------------------------------------------------------
class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def move(self):
        print("Dog runs")

class Bird(Animal):
    def move(self):
        print("Bird flies")

# Using polymorphism
animals = [Dog(), Bird()]

for animal in animals:
    animal.move()
