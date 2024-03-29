# Journey

## 2022-02-10

- [Get keys from unbound TypedDict](https://stackoverflow.com/questions/61943545/python-get-keys-from-unbound-typeddict)
More inline with what I need
```python
class Jim(TypedDict):
    name: str
    age: int

print(Jim.__annotations__)
{'name': <class 'str'>, 'age': <class 'int'>}
```

- [How to get a list of class attributes in python](https://www.geeksforgeeks.org/how-to-get-a-list-of-class-attributes-in-python/)
Not necessarily what I was looking for as the attributes aren't set on the class until instantiated. I would like to read the available keys on a TypedDict from the class itself, not an instance
```python
class Jim(TypedDict):
    name: str
    age: int

# With  dir
dir(Jim)

# With inspect
# Need to filter out private and protected methods
for i in inspect.getmembers(Jim)

# with __dict__.keys()
Jim.__dict__.keys()
dict_keys(['__module__', '__new__', '__dict__', '__weakref__', '__doc__', '__annotations__', '__total__'])
```


## 2022-02-09
- [TypedDict vs dataclasses in Python — Epic typing BATTLE!](https://dev.to/meeshkan/typeddict-vs-dataclasses-in-python-epic-typing-battle-onb)
  - Dataclasses advantage: matching -
    - Determining an object's class when there is a Union of serveral classes.
    - With `isinstance` one can discriminate between types.
    - TypedDicts can't leverage `isinstance` and will need to inspect the entire object to see if it is a "duck". Slow for large objects.
  - Dataclasses advantage: validation
    - cast won't catch an error if a TypedDict has a value that is not the correct type.

## 2019-06-26
- [Facts and myths about Python names and values](https://nedbatchelder.com/text/names.html)
- [Regular expressions](http://pycon2017.regex.training/)

## 2019-06-04

- [cmath for complex numbers](https://docs.python.org/3/library/cmath.html)
- [Decimal class](https://docs.python.org/3/library/decimal.html)

## 2019-06-03

- [Dataclasses - Python 3.7](https://docs.python.org/3/library/dataclasses.html)
- [Ultimate guide to data classes in python 3.7](https://realpython.com/python-data-classes/)
- [Python Questions and Topics](http://net-informations.com/python/iq/pfaq.htm)
- [Timeit in Python with Examples - performance testing](https://www.geeksforgeeks.org/timeit-python-examples/)
- [Ternary operators for python](http://book.pythontips.com/en/latest/ternary_operators.html)

## 2019-06-02

- [Reverse list](https://www.programiz.com/python-programming/methods/list/reverse)
- [Double ended queue - deque - "decks"](https://pymotw.com/3/collections/deque.html)
- [Full Python Programming Course | Python Tutorial for Beginners | Learn Python (2019)](https://www.youtube.com/watch?v=bZ6NL59FMoc&t=2538s)


## 2019-06-01

- [Itertools - groupby](https://docs.python.org/2/library/itertools.html)


## 2019-05-30

- [JSON plus](https://pypi.org/project/jsonplus/)
  - helped to dump dynamodb response to stdout in a readable way
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  - aws sdk for python - need was to query dynamodb
- [Interacting with Dynamodb via boto3](https://martinapugliese.github.io/interacting-with-a-dynamodb-via-boto3/)

## 2018-12-12

- [Lerner Consulting Blog](http://blog.lerner.co.il/)
- [Python weekly](https://www.pythonweekly.com)


## 2018-12-06

- [Python glossary](https://docs.python.org/3/glossary.html#term-duck-typing)
- [Tensorflow introduction](https://www.sohamkamani.com/blog/2018/01/07/tensorflow-introduction/)

## 2018-12-03

- [Multiple assignment and tuple unpacking improve Python code readability](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/)

## 2018-12-01
- [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839)
- [Python Design Patterns: For Sleek And Fashionable Code](https://www.toptal.com/python/python-design-patterns)
- [An Introduction to Mocking in Python](https://www.toptal.com/python/an-introduction-to-mocking-in-python)
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Senior Python Developer interview questions](https://resources.workable.com/senior-python-developer-interview-questions)

## 2018

- https://www.programiz.com/python-programming#tutorial
- https://github.com/joaoventura/full-speed-python
- http://chrispenner.ca/posts/python-tail-recursion
- https://developers.google.com/edu/python/
- Vim ALE Python linting
  - http://liuchengxu.org/posts/use-vim-as-a-python-ide/
  - https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2
- https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593
- https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python/
- [Asterisks in Python: what they are and how to use them](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/)
- [Python morsels](https://www.pythonmorsels.com)
