"""
In Python, the concept of functional interfaces is closely related to the use of functional programming features.
While Python doesn't have the strict concept of a functional interface like Java does,
it does support many functional programming constructs and features.

1. First-Class Functions:
   In Python, functions are first-class citizens, which means they can be passed around as arguments to other functions,
   returned as values from other functions, and assigned to variables.
2. Lambda Functions:
    Python supports anonymous functions using the lambda keyword.
    Lambda functions are often used for short, simple operations.

"""
from functools import reduce
from itertools import chain, filterfalse

square = lambda x: x ** 2
print('square: ', square(5))

# 3. Higher-Order functions:
# Functions that take other functions as arguments or return functions are called higher-order functions.
# Common higher-order functions in Python include map, filter, and reduce.

# Map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Filter
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)

# Reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)


# Closures:
# Python supports closures, where a function can refer to variables from its containing (enclosing) scope even after
# the scope has finished execution.

def outer_functions(x):
    def inner_function(y):
        return x + y

    return inner_function


closure = outer_functions(10)
result = closure(5)
print(result)


# Decorators:
# Decorators are a way to modify or extend the behavior of functions or methods. T
# hey are functions that take a function as an argument and return a new function.
def my_decorator(function):
    def wrapper():
        print("Something is happening before the function is called.")
        function()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()

"""
6. Functional Programming Libraries:
   Python has libraries that provide functional programming tools, such as itertools and functools, 
   which include functions for working with iterators, creating decorators, and more.

These topics collectively contribute to the functional programming style in Python, 
allowing you to write more expressive and concise code. 
While Python is not purely functional, it does support functional programming features, 
making it versatile for different programming paradigms.

"""

# Generators
squared_generator = (x ** 2 for x in numbers)
print(list(squared_generator))

# Itertools module
# `Itertools` module provides a collection of fast, memory-efficient tools for working with iterators.
combined_iterable = chain(numbers, ['a', 'b'])
print(list(combined_iterable))
