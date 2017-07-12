## Functions
* 'Containers' for code
* Named, reusable
* `def` defines a function:
```python
def sayHello():
    print "hello"
```

+++
## Functions
functions can take arguments:
```python
def say(what):
    print what

say("hello")
say(1)  # ?
say([1])
```

+++
## Functions
...and return values:
```python
def tellMeASecret():
    return "$eCr3t"

print tellMeASecret()
```

+++
## Functions
...and return *multiple* values!
```python
def getHostPort():
    return ("nydev1", 3123)

host, port = getHostPort()
```

+++
## Functions
Functions can have *default* arguments:
```python
def getHostPort(host='nydev1', port=8000):
    return (host, port)
getHostPort('lndev1')
```