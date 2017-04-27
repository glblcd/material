---
## Python
##### IoT in Africa | 2017
![Python](../assets/img/python-360x361.png)

---
## What is Python?
* A programming language!
* Built-in data types
* Control flow
* Modules
* Loads of open-source (free!) code you can use

---
## Hello, Python!
hello.py:
```python
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
```

+++
## Hello, Python!
Can be executed from a file:
```sh
$ python hello.py
x is 1
```

+++
## Hello, Python!
Or interpreted using the REPL:
```sh
$ python
>>> print("hello, Python!")
hello, Python!
>>> ^D
$
```
Useful for experimenting. Try it!

+++
## Hello, Python!
Or using UNIX's shebang syntax:
```python
#!/usr/bin/python

print("hello from Python!")
```
---
## Data types
Every variable has a type...
```sh
>>> type("hello")
<type 'str'>
>>> type(3)
<type 'int'>
```
...that describes *what it is*

+++
## Data types
  * String, Numeric
  * List
  * Dictionary
  * Tuple

---
## String
Use "" or '', doesn't matter:
```sh
>>> print("hello" == 'hello')
True
```

+++
##String
...or Unicode (with care!)
```sh
>>> command = "⌘"
>>> command
'\xe2\x8c\x98'
>>> print(command)
⌘
```

+++
##String
Some *builtin* functions work with variables:
```sh
>>> len("hello")
5
```

---
## Numeric
* int & long
* float
* complex

+++
## Integer
Math, as you'd expect:
```sh
>>> x = 250
>>> print type(x)
<type 'int'>
>>> x -= 1
>>> print x
249
```

+++
## Integer
Can also represent integers as hex
```sh
>>> x = 0x23
>>> x
35
```
* Find out how to do octal representation

+++
## Long
Unlimited precision for massive numbers:
```sh
>>> x = 100000000000000000000000000000000000000000001
>>> type(x)
<type 'long'>
>>> x += 1
>>> x
100000000000000000000000000000000000000000002L
```

+++
## Float
```sh
>>> 3.2e4
32000.0
```

+++
## Complex
```sh
>>> imaginary = 3 + 2j
>>> type(imaginary)
<type 'complex'>
>>> imaginary += 1
>>> imaginary
(4+2j)
>>> imaginary += 4j
>>> imaginary
(4+6j)
```

---
## List
Collections of data
```sh
>>> names = ["John", "Paul", "George", "Ringo"]
>>> print(names)
['John', 'Paul', 'George', 'Ringo']
```

+++
## List
Another example
```python
names = ["John", "Paul", "George", 3]
```
Wait, what?

---
## Dynamic typing
* The *type* of a variable is determined at runtime
* Not compile time
* What's the difference?

+++
## Dynamic typing
* Useful for writing code quickly
* Fewer compiler errors
* Where do the errors go?

+++
## Dynamic typing
Sometimes they go nowhere:
```sh
>>> print(names)
['John', 'Paul', 'George', 3]
```

+++
## Dynamic typing
Sometimes things break:
```sh
>>> len(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
```

---
##Dictonary
A hash table
* sequence of key-value pairs
* efficient lookup & insertion
* elements aren't ordered

+++
##Dictionary
```sh
>>> people = {"robert": 33, "john": 23, "steve": 44 }
>>> people["robert"]
33

>>> people["janet"] = 25
>>>
```

+++
##Dictionary
```sh
>>> del people["steve"]
>>> people
{"robert": 33, "john": 23, "janet": 25 }
]
```

+++
##Dictionry
* keys()

```sh
>>> people.keys()
['robert', 'john', 'janet']
```

* values()

```sh
>>> people.keys()
[33, 23, 25]
```

* items()
  * try it!
---

## Tuple
A way to join related data:
```python
hostport = ("accdev1", 3213)
```

+++
## Tuple
Data elements don't have names
```python
sam = ("Sam Moorhouse", 1984)
```
* What does *1984* refer to? (Careful!)
* Is there a better way?

---
## Conditionals
* if | else | elif
* allows us to affect the *flow of control*
```python
sam = ("Sam Moorhouse", 1984)
name, yob = sam
if yob < 1990:
    print(name + " is an old dude")
else:
    print(name + "must still be pretty young)
```

+++
## Conditionals
* notice that colon
* and the indentation!
```python
yob = (int)(raw_input ( "Enter the year you were born: " ))
now = 2017
if (now - yob) < 18:
    print("you're still a child")
elif (now - yob) < 25:
    print("whoa! Still learning!")
else:
    print("OLD!")
```

+++
## Conditionals
* conditions are *evaluated in order*
* `print` is a *function*
* we can attempt to *cast* one data type to another
  * Does it always work?
  * Should it?!

+++
## Conditionals
* `if` in an *expression*
  * it evaluates to a value
```python
yob = (int)(raw_input ( "Enter the year you were born: " ))
now = 2017
status = ("young" if (now - yob) < 30 else "old")
print(status)
```

---
## Loops
```python
names = ["John", "Paul", "George", "Ringo"]
for beatle in names:
    print(beatle)
```
    John
    Paul
    George
    Ringo

+++
## Loops
Also tuples:
```python
hostport = ("accdev1", 3213)
for item in hostport:
    print(item),
```
    "accdev1"  3213
* "," supresses the newline!

+++
## Loops
* nested *control flow statements*
```python
names = ["John", "Paul", "George", "Ringo"]
for beatle in names:
    if len(beatle) > 4:
        print(beatle),
```
    George Ringo

+++
## Loops
`while` loops until condition returns false
```python
num = 0
while num < 5:
    num = num + 1 #++?
    print(num),
```
    1 2 3 4 5

---
## Functions
* 'Containers' for code
* Named, reusable
* `def` defines a function:
```python
def sayHello():
    print("hello")
```

+++
## Functions
functions can take arguments:
```python
def say(what):
    print(what)

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

print(tellMeASecret())
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
createTuple('lndev1')
```
---
## Modules
* Functions are organised into *modules* and *packages*
  * Reusable units of code
  * `reusability == good`!
* Each *file* is a *module*
* Each *directory* is a *package*

+++
## Modules
* `import package.subpackage.module`
* e.g *Talk.py*:
```python
def get
```

+++
## Functions
* We're working mostly with functions
* Python has *much* more
  * Classes and objects
  * Inheritance
