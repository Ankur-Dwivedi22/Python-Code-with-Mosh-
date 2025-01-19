# import math
# print("Hello world")
# print("*" * 10)
# # print "Hello world"  : valid in python 2

# age: int = 20
# age = "Python"
# print(age)

# -------------------------------------------------------------------------------
# # immutable types
# x = 1
# print(id(x))
# x = x + 1
# print(id(x))

# y = False
# print(id(y))
# y = True
# print(id(y))

# x = [1, 2, 3]  # lists -> mutable
# print(id(x))
# x.append(4)
# print(id(x))

# -------------------------------------------------------------------------------
# # length function
# course = "Python"
# print(len(course))

# l = [1, 2, 3]
# print(len(l))

# -------------------------------------------------------------------------------
# # indexes
# print(l[0])
# print(l[-1])  # negative

# -------------------------------------------------------------------------------
# # slicing
# a = "Python programming"
# print(a[0:7])
# print(a[0:])
# print(a[:7])
# print(a[2:10])
# print(a[:])

# -------------------------------------------------------------------------------
# # escape sequences
# a = 'Python " s'
# print(a)
# a = "Python \" s"
# print(a)

# a = "Python\nProgramming"
# print(a)
# a = """Python
# Programming"""
# print(a)

# -------------------------------------------------------------------------------
# # concatenation of strings
# a = "Ankur"
# b = "Dwivedi"
# print(a + " " + b)

# # formatted strings
# c = F"{a} {b}"
# print(c)

# c = f"{a} is no. {0+1}"
# print(c)

# c = f"{len(a)} is the length of word \"{a}\""
# print(c)


# -------------------------------------------------------------------------------
# # methods on strings
# c = "    Python programming  "
# print(c.upper())
# print(c.lower())
# print(c.title())
# print(c.strip())
# print(c.lstrip())
# print(c.rstrip())
# print(c.find("pro"))
# print(c.find("Pro"))
# print(c.replace("P", "C"))
# print("programming" in c)
# print("programming" not in c)

# # numbers
# x = 10
# print(x)
# x = 0b10
# print(x)
# print(bin(x))
# x = 0x64
# print(x)
# print(hex(x))
# # complex number
# x = 1 + 2j
# print(x)

# -------------------------------------------------------------------------------
# # arithmetic operators
# # + , - , * , / , // , % , **

# x = 10 / 3
# print(x)
# x = 10 // 3
# print(x)
# x = 10 % 3
# print(x)
# x = 10 ** 3
# print(x)

# -------------------------------------------------------------------------------
# # augmented arithmetic operator (valid for all arithmetic operators)
# x = x + 1
# x += 1
# print(x)

# # working with numbers
# PI = -3.14  # (treated as constant , should not be modified)
# print(round(PI))
# print(abs(PI))

# print(math.floor(PI))


# -------------------------------------------------------------------------------
# # type conversion
# # x = input("x : ")
# # y = x + 1 gives error because x is string and we are adding integer to it
# # python is strongly typed language , it does not perform any impicit type conversion
# print(int(x))
# print(float(x))
# print(bool(x))

# -------------------------------------------------------------------------------
# # Falsy values
# # ""
# # 0
# # []
# # None (null)
# # all other true values

# -------------------------------------------------------------------------------
# # conditional statements
# age = 22
# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# x = 0
# if x > 1:
#     pass
# else:
#     print(f"x = {x}")


# -------------------------------------------------------------------------------
# # logical operators
# name = ""
# if not name:
#     print("name is empty")

# age = 22
# if age >= 18 and age < 65:
#     print("eligible")

# if 18 <= age < 65:
#     print("eligible")


# -------------------------------------------------------------------------------
# # ternary operator
# mssg = "Elgibile" if age >= 18 else "Not eligible"
# print(mssg)


# -------------------------------------------------------------------------------
# # for loop
# for x in "Python":
#     print(x, end=" ")
# print()

# for x in ['a', 'b', 'c']:
#     print(x)


# -------------------------------------------------------------------------------
# # range function
# for x in range(5):
#     print(x)

# for x in range(2, 5):
#     print(x)

# for x in range(0, 10, 2):
#     print(x)

# print(range(5))
# print(type(range(5)))
# print([0, 1, 2, 3, 4])


# -------------------------------------------------------------------------------
# # for-else
# names = ["john", "Mary"]
# for name in names:
#     if name.startswith('J'):
#         print("Found")
#         break
# else:
#     print("Not found")

# # while loop
# guess = 0
# ans = 5

# while ans != guess:
#     guess = int(input("Guess : "))
# else:
#     pass


# -------------------------------------------------------------------------------
# functions
# def increment(number, by):
#     pass  # returns None without a return statement


# print(increment(2, 3))


# def increment2(number, by=1):  # default values to parameters
#     return number+by


# print(increment2(2, 3))
# print(increment2(2, by=3))  # keyword arguments to make code more readable
# print(increment2(2))  # second argument taken by default value

# # using annotations to specify data type


# def increment3(number: int, by: int = 1) -> tuple:
#     return (number, number+by)


# print(increment3(2, 4))

# -------------------------------------------------------------------------------

# variable arguments
# def multiply(*list):
#     product = 1
#     for num in list:
#         product *= num
#     return product


# print(multiply(2, 3, 4, 5))

# def save_user(**user):
#     print(user)
#     print(user["id"])
#     print(user["name"])


# save_user(id=1, name="admin")

# -------------------------------------------------------------------------------

# scope of variables
# mssg = "a"


# def func():
#     mssg = "b"
#     print(mssg)


# def func2():
#     global mssg
#     mssg = "b"


# # func()
# func2()
# print(mssg)

# -------------------------------------------------------------------------------
# fizz buzz exercise

# def fizz_buzz(num):
#     if (num % 3 == 0 and num % 5 == 0):
#         print("FizzBuzz")
#     elif (num % 3 == 0):
#         print("Fizz")
#     elif (num % 5 == 0):
#         print("Buzz")
#     else:
#         print(num)


# for i in range(1, 20):
#     fizz_buzz(i)

# -------------------------------------------------------------------------------

# data structures in python
# lists
# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 100
# print(letters)
# print(matrix)
# print(zeros)
# combined = zeros + letters
# print(combined)
# multiple = ["a", 1, True]
# print(multiple)
# numbers = list(range(20))
# print(numbers)
# chars = list("Hello World")
# print(len(chars))

# -------------------------------------------------------------------------------
# accessing items in lists
# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0])
# print(letters[-1])
# print(letters[0:3])
# print(letters[0:])
# print(letters[:3])
# print(letters[:])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers[::-1])

# -------------------------------------------------------------------------------
# list unpacking
# num = [1, 2, 3]
# a, b, c = num
# print(a, b, c)

# num2 = [1, 2, 3, 4, 3, 4, 5, 6, 8]
# a, b, *other = num2
# print(a, b)
# print(other)
# first, *other, last = num2
# print(first)
# print(other)
# print(last)
# -------------------------------------------------------------------------------

# loop over list
# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)
# for tpl in enumerate(letters):
#     print(tpl)
# for ind, letter in enumerate(letters):
#     print(ind, letter)

# -------------------------------------------------------------------------------
# adding or removing items

# add
# letters.append("d")
# letters.append("d")
# letters.append("d")
# letters.append("d")
# letters.insert(0, "-")
# print(letters)

# # remove
# letters.pop()  # removes from last
# print(letters)
# letters.pop(0)  # removes from index specified
# print(letters)
# letters.remove("b")  # removes first occurence of that value
# print(letters)
# del letters[-1]  # removes element at that index
# print(letters)
# # deletes a range of elements whereas pop deletes only one element
# del letters[0:3]
# print(letters)
# letters.clear()  # deletes everything
# print(letters)

# -------------------------------------------------------------------------------

# finding items in list
# letters = ["a", "b", "c"]
# print(letters.count("a"))
# if "d" in letters:
#     print(letters.index("d"))
# else:
#     print(-1)

# -------------------------------------------------------------------------------

# sorting lists
# num = [1, 5, 2, 6, 3, 4]
# num.sort()  # modifies original list and sort it in ascending order
# print(num)
# num.sort(reverse=True)  # same but in reverse order
# print(num)

# print(sorted(num))  # creates another list and sorts it
# print(sorted(num, reverse=True))

# -------------------------------------------------------------------------------

# sorting complex list
# items = [
#     ("P1", 9),
#     ("P2", 10),
#     ("P3", 7)
# ]
# items.sort()  # python won't be able to sort as list is complex
# print(items)
# we need to define our own sorting function which basically tells the basis on which the list must be sorted


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# -------------------------------------------------------------------------------

# lambda function
# items.sort(key=lambda item: item[1])
# print(items)

# -------------------------------------------------------------------------------

# map functions
# items = [
#     ("P1", 9),
#     ("P2", 10),
#     ("P3", 7)
# ]

# price = []
# for item in items:
#     price.append(item[1])
# print(price)

# x = map(lambda item: item[1], items) #creates a map object which is iterable
# for it in x:
#     print(it)

# lst = list(map(lambda item: item[1], items))
# print(lst)

# -------------------------------------------------------------------------------

# filter function -> returns a filter object which is also iterable
# items = [
#     ("P1", 9),
#     ("P2", 10),
#     ("P3", 7)
# ]

# x = list(filter(lambda item: item[1] >= 9, items))
# print(x)

# -------------------------------------------------------------------------------

# list comprehension
# items = [
#     ("P1", 9),
#     ("P2", 10),
#     ("P3", 7)
# ]
# # prices1 & prices2 produce same result
# prices1 = list(map(lambda item: item[1], items))
# prices2 = [item[1] for item in items]

# print(prices1)
# print(prices2)

# filtered1 = list(filter(lambda item: item[1] >= 9, items))
# filtered2 = [item for item in items if item[1] >= 9]

# print(filtered1)
# print(filtered2)

# -------------------------------------------------------------------------------
# zip function

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# print(list(zip(l1, l2)))
# print(list(zip("abc", l1, l2)))

# -------------------------------------------------------------------------------
# stack(lifo)

# st = []
# st.append(1)
# st.append(2)
# st.append(3)
# while (st):
#     top = st[-1]
#     print(top)
#     st.pop()

# -------------------------------------------------------------------------------
# queue(fifo)

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# while (queue):
#     print(queue.popleft())

# -------------------------------------------------------------------------------
# tuples(read only list , can not be modified)

# point = (1, 2)
# print(point)

# point = 1, 2  # also tuple, if only one element add trailing comma
# print(point)

# # concatenation of tuples
# t = (1, 2) + (3, 4)
# print(t)

# t = (1, 2) * 3
# print(t)

# t = tuple([1, 2])
# print(t)

# t = tuple("Hello")
# print(t)

# t = 1, 2, 3
# print(t[0], t[1])
# print(t[0:2])

# x, y, z = t
# print(x, y, z)
# if 1 in t:
#     print("exists")

# -------------------------------------------------------------------------------
# swapping variables

# x = 1
# y = 2
# x,y = y,x
# print(x,y)

# -------------------------------------------------------------------------------
# arrays

# from array import array

# num = array("i", [1, 2, 3])
# num.append(4)
# num.insert(0, 1)
# print(num[0])
# print(num)

# num[1] = 1.0 # will give type error as array has fixed data type

# -------------------------------------------------------------------------------
# sets

# num = [1, 2, 3, 2, 3, 4, 5, 5]
# uni = set(num)
# print(uni)

# st = {1, 2}
# st.add(3)
# st.remove(1)
# print(st)
# print(len(st))

# print(uni | st)
# print(uni & st)
# print(uni-st)
# print(uni ^ st)  # elements that are either in uni or st but not in both
# # print(st[0]) #set are unordered so no indexing , will give runtime error

# if 1 in uni:
#     print("yes")

# -------------------------------------------------------------------------------
# dictionary

# p = {"x": 1, "y": 2}
# print(p)
# p = dict(x=1, y=2)
# print(p)

# p['x'] = 10
# p['z'] = 20
# print(p)
# # print(p['a']) #value error as key not in dict
# # use these instead

# if "a" in p:
#     print(p['a'])
# print(p.get('a'))  # gives None if key not present in dict
# print(p.get('a', 0))  # return default value given when key not present

# del p['z']
# print(p)

# for key in p:
#     print(key, p[key])

# for x in p.items():
#     print(x)

# -------------------------------------------------------------------------------
# dictionary comprehension

# val = [x*2 for x in range(5)]  # list
# st = {x*2 for x in range(5)}  # set
# print(val)
# print(st)

# d = {x: x*2 for x in range(5)} #dict
# print(d)

# t = (x*2 for x in range(5)) #not a tuple -> generator object

# -------------------------------------------------------------------------------
# generator object -> used when we are dealing with large set of numbers which occupy a lot of memory
# it not stores values rather generates

# from sys import getsizeof

# t = (x*2 for x in range(5))
# print(t)
# for x in t:
#     print(x)

# print(getsizeof(t))  # bytes of memory -> remains same
# print(len(t))  # gives error

# -------------------------------------------------------------------------------
# unpacking operator -> can unpack any iterable

# num = [1, 2, 3]
# print(num)
# print(*num)

# val = list(range(5))
# print(val)
# val = [*range(5), *"Hello"]
# print(val)

# l1 = [1, 2]
# l2 = [3]
# val = [*l1, *l2]
# print(val)

# d1 = {"x": 1}
# d2 = dict(x=10, y=2)
# d = {**d1, **d2}
# print(d)

# -------------------------------------------------------------------------------
# exercise

# s = "This is a common interview question"
# d = {}
# for c in s:
#     if c in d:
#         d[c] = d[c] + 1
#     else:
#         d[c] = 1

# mx = 0
# c = ''
# for x in d:
#     if d[x] > mx:
#         mx = d[x]
#         c = x

# print(c, mx)

# -------------------------------------------------------------------------------
# exceptions

# numbers = [1, 2]
# # error that terminates the execution of program -> exception
# print(numbers[3])
# # caused bcz of programmer

# if input is not int then error -> exception caused bcz of user
# age = int(input("Age: "))

# -------------------------------------------------------------------------------
# handling exception

# try:
#     age = int(input("Age: "))
# except:
#     print("Wrong input")
# else:
#     print("No exceptions..")
# print("Execution continues..")

# -------------------------------------------------------------------------------
# cleaning up

# try:
#     file = open("hello.py")
#     age = int(input("Age: "))
#     xFactor = 10 / age
# except:
#     print("Exception")
# else:
#     print("No exception")
# finally:
#     file.close()

# -------------------------------------------------------------------------------
# classes
# class : blueprint for creating new objects -> human
# object : instance of class -> ram , sita

# creating classes
# class Point:
#     def draw(self):
#         print("Draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))
# point.draw()

# -------------------------------------------------------------------------------
# constructor(magic method)
# methods defined in class should always have one parameter that is self


# class Point:
#     default_color = "red"  # class attribute -> shared with all instsances of a class

#     def __init__(self, x, y):  # self is a reference to current point object
#         self.x = x
#         self.y = y

#     @classmethod  # decorator
#     def zero(cls):  # cls is a reference to the class itself
#         return cls(0, 0)  # => Point(0,0)

#     def draw(self):
#         print(f"Point ({self.x} , {self.y})")


# point = Point(2, 3)
# print(point.x, point.y)
# point.draw()
# # objects in python are dynamic that means
# # we can create parameters for our object outside of constructor like this
# # instance attributes (x,y,z) : these values can be different for different objects
# point.z = 1
# print(point.z)

# print(point.default_color)
# print(Point.default_color)

# # class vs instance methods
# # class method can be used without object

# point = Point(0, 0)
# point.draw()
# point = Point.zero()

# ---------------------------------------------------------------------------------------
# Magic methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x} , {self.y})")


# point = Point(1, 2)
# print(point.__str__)  # inherited by our object but we can create our own
# print(point)
# print(str(point))

# ---------------------------------------------------------------------------------------
# Comapring objects

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(1, 2)
# other = Point(1, 2)
# # this is equality operator which basically compares memory addresses
# print(point == other)
# # after eq magic method gives true
# # magic method can be used to compare objects

# # print(point > other) -> error
# # after gt
# print(point > other)
# # python automatically figures out less than after this
# print(point < other)

# ---------------------------------------------------------------------------------------
# Arithmetic operations on objects
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x+other.x, self.y+other.y)


# point = Point(10, 20)
# other = Point(1, 2)
# combined = point + other
# print(combined.x, combined.y)

# ---------------------------------------------------------------------------------------
# Making custom containers
# container like list ,string , dictionary

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         # iter is a built in function which returns one item at a time
#         return iter(self.__tags)


# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")  # we are handling casing so not counted different
# cloud.add("Python")
# cloud.add("Python")
# # print(cloud.__tags)

# print(cloud["python"])
# cloud["python"] = 0
# print(cloud["python"])
# print(len(cloud))

# for key in cloud:
#     print(key, cloud[key])

# # Private members
# print(cloud["PYTHON"])

# # print(cloud.tags["PYTHON"]) -> THIS GIVES ERROR AS TAGS DOES NOT HAVE PYTHON
# # the problem here is that we have access to tags outside class

# # print(cloud.__tags) #gives error now as tags is private

# # but still we can acess it
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)  # acessed private member

# ---------------------------------------------------------------------------------------
# properties

# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value


# product = Product(-50) #raises value error

# to implement this above method we can use properties
# a property is an object that sits in front of attribute and sets or gets its value
# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # here price is property
#     price = property(get_price, set_price)


# product = Product(10)
# print(product.price)
# product.price = 12
# print(product.price)

# in the above code we have property but still we can acess setter and getter
# one solution is to declare them private
# another solution -> use decorators

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value


# product = Product(10)
# print(product.price)
# ---------------------------------------------------------------------------------------
# Inheritance

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")
# # Animal : parent or base class
# # Mammal : child or sub class


# class Mammal(Animal):
#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# m = Mammal()
# m.eat()
# print(m.age)

# print(isinstance(m, Animal))  # m is also an instance of parent class of mammal
# # the object class
# # It is base class for all classes in python

# print(isinstance(m, object))
# o = object()  # built-in
# print(issubclass(Mammal, Animal))
# print(issubclass(Mammal, object))
# ---------------------------------------------------------------------------------------
# Method overriding -> overriding some method in base class by method in child class

# class Animal:
#     def __init__(self):
#         self.age = 1


# class Mammal(Animal):
#     def __init__(self): # this overrides constructor of base class
#         self.weight = 2


# m = Mammal()
# print(m.weight)
# print(m.age)

# to use base class constructor
# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1


# class Mammal(Animal):
#     def __init__(self):  # this overrides constructor of base class
#         super().__init__()
#         print("Mammal Constructor")
#         self.weight = 2


# m = Mammal()
# print(m.weight)
# print(m.age)
# ---------------------------------------------------------------------------------------
# Multi level inheritance
# class Animal:
#     def eat(self):
#         print("eat")

# class Bird(Animal):
#     def fly(self):
#         print("fly")

# class Chicken(Bird):
#     pass

# ---------------------------------------------------------------------------------------
# Multiple Inheritance
# class Employee:
#     def greet(self):
#         print("Hello emp")


# class Person:
#     def greet(self):
#         print("Hello person")


# class Manager(Employee, Person):
#     pass


# class SDE(Person, Employee):
#     pass


# m = Manager()
# m.greet()
# s = SDE()
# s.greet()
# ---------------------------------------------------------------------------------------
# A good example of inheritance
# class InvalidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("STream already opened")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")
# ---------------------------------------------------------------------------------------
# Abstarct Base Class
# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("STream already opened")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# # here memoryStream becomes abstract class as it has not defined read which was
# # abstract method, for a class to become child of abstract class it must define abstract methods
# # this implements consistency in codebase


# class MemoryStream(Stream):
#     pass

# # stream = Stream() -> error as abstract class can not be instanciated
# ---------------------------------------------------------------------------------------

# Polymorphism
# from abc import ABC, abstractmethod

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")

# class DropDown(UIControl):
#     def draw(self):
#         print("DropDown")

# def draw(control):
#     control.draw()

# dd = DropDown()
# tb = TextBox()
# draw(dd)
# draw(tb)
# ---------------------------------------------------------------------------------------
# Duck typing -> it does not check type of object , just check its existence
# so we do need abstract base class for polymorphism
# not a good practice
# class TextBox:
#     def draw(self):
#         print("TextBox")


# class DropDown:
#     def draw(self):
#         print("DropDown")


# def draw(control):
#     control.draw()


# dd = DropDown()
# tb = TextBox()
# draw(dd)
# draw(tb)

# ---------------------------------------------------------------------------------------
# Extending built-in types

# class Text(str):
#     def duplicate(self):
#         return self+self


# # it has all methods of strings + our own created methods
# text = Text("Pyhton")
# print(text.lower())
# print(text.duplicate())


# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)


# l = TrackableList()
# l.append(4)
# print(l)

# ---------------------------------------------------------------------------------------
# Data classes
# we use classes to bundle methods and data but some classes only have data
# these classes are called data classes

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)  # compares addresses but after eq compares values
# print(id(p1))
# print(id(p2))

# if we are dealing with classes that only have data use namedtuple like this:
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)
# named tiples are immutable
# p1.x = 10 error
p2 = Point(x=1, y=2)
print(p1 == p2)
print(id(p1))
print(id(p2))
# ---------------------------------------------------------------------------------------
