# Python / Learning

##

Programming as Guido ~~intended~~ **indented** it.

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## REPL

**help()**

Access documentation via the REPL using `help()`

```python
>>> import math
>>> help(math)
>>> help(math.sqrt)
```

## import

import the whole library

```python
import math
math.factorial(5) # 120
```

import the function from the library

```python
from math import factorial
factorial(5) # 120
```

import the function from the library and rename

```python
from math import factorial as fac
fac(5) # 120
```


## Comments, Templates, and Documentation

**Comment and multiline comment**

```python
# Comment line
"""Multiline
comment does
this thing"""
```

**Templates**

```python
x = 12
f"x is equal to {x}"
# outputs "x is equal to 12"
```

**Docstring**
```python
# Docstring
def double(num)
    """Function to double the value"""
    return 2*n

# get docstring - documentation string
print(double.__doc__)

```


## Data Types

**String**
```python
myStr = "Hello"
myStr = 'Hello'
```

**Multiline String**
```python
myStr = '''Hello
you long string```
```

**Integer**

```python
# Assign an integer
a = 2

# binary
0b10 # 2

# Octal
0o10 # 8

# Hexidecimal
0x10 # 16

# Cast as integer
int("496") # 496
int("1000", 3) # 81
```


**Float**

64 bit precisiont - 53 bits of precision and 15-16 bits of decimal precision

```python
a = 2.0

3e8 # 300000000.0

1.616e-35 # Plank's constant

# Cast
float("1000") # 1000.0
float(nan) # nan
float(inf) # infinity
float(-inf) # negative infinity
```

**Complex**
```python
a = i+2j
```

**None**

Python's null value.

**Bool**

```python
True
False

bool(0) # False
bool(0.0) # False

bool(0.027) # True
bool(2) # True
bool(-1) # True

bool([]) # False
bool([1]) # True

bool("") # False
bool("Spam") # True
bool("False") # True
```


**Bytes and Byte Arrays - bytes / bytearray**


**List**
```python
a = [4,2,5,6,3,3,9]
```


**Set and Frozen Set**

+ mutable
+ unordered
+ unique

```python
a = {4,2,5,6,3,3,9}
```

**Tuple**

+ immutable - once created, can't be modified
+ ordered
+ unique
+ faster than a list

```python
a = (4,2,5)
```

**Dictionary**

+ unordered collection of key/value pairs

```python
a = { 1: 'a', 'b':2 }
```



## Lists

```python
li = [5,3,4,5,3,7]
```

### len() - Length

```python
length = len([5,3,4,5,3,7])
```

### append() - Add to list

```python
li = [5,3,4,5,3,7]
li.append(22)
# [5,3,4,5,3,7,22]
```

### remove() - Remove value from list

```python
li = [5,3,4,5,3,7]
li.remove(7)
# [5,3,4,5,3]
```

### del - Remove from list by index

```python
li = [5,3,4,5,3,7]
del li[1]
# [5,4,5,3,7]
```

### pop() - Take value from the end of the list

```python
li = [5,3,4,5,3,7]
item = li.pop()
# item has value 7
# [5,3,4,5,3]
```

### Adding lists together

```python
li = [1,2]
li2 = [3,4]
newli = li + li2
# newli is [1,2,3,4]
```

### slice() - get list subset

```python
li = [1,2,3,4]
sub = li[1:2]
# sub -> [2,3]
```

### sort() - order the list

```python
li = [2,3,1,6,5]
li.sort()
# li -> [1,2,3,5,6]
```

### reverse() - reverse the list order

```python
li = [2,3,1,6,5]
li.reverse()
# li -> [5,6,1,3,2]
```

### index() - get value by index of list

```python
li = [2,3,1,6,5]
item = li.index(1)
# item -> 3
```

## Dictionary

```python
student = {
  "first_name": "Jim",
  "age": 20,
}

student['first_name'] # output "Jim"
student['last_name'] # output Key Error as it does not exist

```

**Add a key to or change a key's value the dictionary**

```python
# Add
student['id'] = 22322

# Change
student['age'] = 21
```

**Delete the key value pair**

Deleting a key that doesn't exist will throw a `Key Error`

```python
del student['age']
```


### get()

Get a value by key and provide a default to avoid an error

```python
student.get('first_name') # output "Jim"
student.get('last_name', 'Unknown') # output "Unknown"

```

### keys()

```python
student.keys() # output ['first_name', 'age']
```

### values()

```python
student.values() # output ['Jim', 20]
```


## Mathmatical Operations

| Operator   | Meaning                                 | Example       |
|------------|-----------------------------------------|---------------|
| +          | Add two operands                        | x + y or +2   |
| -          | Subtract two operands                   | x - y or -2   |
| *          | Multiply two operands                   | x * y         |
| /          | Divide left by right operand            | x / y         |
| //         | Floor Division                          | 15 // 4 = 3   |
| %          | Modulus - division remainder            | 11 % 2 = 1    |
| **         | Exponent                                | 2**3 = 8      |


## Comparison Operations

| Operator   | Meaning                                                    | Example                  |
|------------|------------------------------------------------------------|--------------------------|
| >          | Greater than - True if left is greater than right operand  | 3 > 2 = True             |
| <          | Less than - True if left is less than right operand        | 2 < 3 = True             |
| ==         | Equal to - True if operands are equal                      | 3 == 3 = True            |
| !=         | Not equal to - True if operands are not equal              | 2 != 3 = True            |
| >=         | Greater than or equal to                                   | 3 >= 2, 3 >=3 = True     |
| <=         | Less than or equal to                                      | 2 <= 3, 2 <=2 = True     |


## Logical Operations

| Operator   | Meaning                                                    | Example                  |
|------------|------------------------------------------------------------|--------------------------|
| and        | True if both operands are true                             | x and y                  |
| or         | True if one operand is true                                | x or y                   |
| not        | True if operand is false                                   | not x                    |



## Control Flow


```python

number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

py = False
if not py:
    print("py is False")


if number == 5 and not py:
    print("Number is 5 and py is False")
```

## Exception handling - try/except

Handle exceptions with try and except, and chain as many exception cases as needed

** handling a dictionary `Key Error` and `Type Error` for bad addition

```python
try:
    # could result in Key Error
    last_name = student[`last_name`]
    # results in Type Error
    age_and_last_name = last_name + 20
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("Error, can't add these two properties")
    print(error)
execpt Exception:
    print("Handle unknown errors")


```


## Functions

```python
persons = []

def get_persons():
    return persons

def add_person(person):
    persons.append(person)

```

** Default argument values
```python
def add_person(name, age=0):
add_person("Sara")
# Adds person with name "Sara" and age 0
```

** **args - Handle variable number of args
```python
def var_args(greeting, **args):
var_args("hello", "yes", True)
# output
# hello
# ("yes", True)
```

** **kwargs - Handle variable number of named args
```python
def add_person(**kwargs):
    print(kwargs['name'], kwargs[age])
add_person(name="Chris", age="12", enrolled=True)
# output
# Chris 12
```


## Generators


```python
def read_file(f):
    for line in f:
        yield line

```


## Lambda Function

Anonymous functions to help reduce our function footprint

```python
# double lambda
double = lambda x: x * 2

# Same as
def double(num):
    return x * 2

# Multiple arguments
add = lambda x,y: x + y
```

## Class

```python
# Parent class of HighSchoolStudent below
class Student:
    # static property
    school_name = "Sprinfield Elementary"

    # constructor
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.namej

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# Inherit class
class HighSchoolStudent(Student):
    # override static property
    school_name = "Springfield High"

    # override parent method
    def get_school_name(self):
        return "This is a High School Student"

    # call parent method with super()
    def get_name_capitalize(self):
        orig_value = super().get_name_capitalize()
        return orig_value + "HS"

```


