# Control Flow


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

