# Function

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

