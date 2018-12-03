# Python / Learning

## Data Types

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
+ Immutable sequences of bytes


