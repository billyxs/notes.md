# Dictionary

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
