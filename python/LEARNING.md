# Python / Learning

## Comments and Documentation

**Comment and multiline comment**
```python
# Comment line
"""Multiline
comment does
this thing"""
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
a = 2
```


**Float**
```python
a = 2.0
```

**Complex**
```python
a = i+2j
```

**List**
```python
a = [4,2,5,6,3,3,9]
```


**Set**

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

## len() - Length

```python
length = len([5,3,4,5,3,7])
```

## append() - Add to list

```python
li = [5,3,4,5,3,7]
li.append(22)
# [5,3,4,5,3,7,22]
```

## remove() - Remove value from list

```python
li = [5,3,4,5,3,7]
li.remove(7)
# [5,3,4,5,3]
```

## del - Remove from list by index

```python
li = [5,3,4,5,3,7]
del li[1]
# [5,4,5,3,7]
```

## pop() - Take value from the end of the list

```python
li = [5,3,4,5,3,7]
item = li.pop()
# item has value 7
# [5,3,4,5,3]
```

## Adding lists together

```python
li = [1,2]
li2 = [3,4]
newli = li + li2
# newli is [1,2,3,4]
```

## slice() - get list subset

```python
li = [1,2,3,4]
sub = li[1:2]
# sub -> [2,3]
```

## sort() - order the list

```python
li = [2,3,1,6,5]
li.sort()
# li -> [1,2,3,5,6]
```

## reverse() - reverse the list order

```python
li = [2,3,1,6,5]
li.reverse()
# li -> [5,6,1,3,2]
```

## index() - get value by index of list

```python
li = [2,3,1,6,5]
item = li.index(1)
# item -> 3
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


