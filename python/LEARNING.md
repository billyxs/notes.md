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
a = [4,2,5,6,3,3,9]

**Set**
a = {4,2,5,6,3,3,9}

**Tuple**
a = (4,2,5)

**Dictionary**
a = { 1: 'a', 'b':2 }



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

