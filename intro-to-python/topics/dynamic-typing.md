
## Dynamic typing
* Variables are storage that hold *values*
* Should variables care what sort of values they hold?
* This is another philosphical difference -- no right/wrong answers
* Statically-typed languages: You have to say what sort of data variables can hold
* Dynamically-typed: Variables can hold anything & can change their mind
* Python is (mostly) dynamically-typed

+++

## Dynamic typing
* Useful for writing code quickly
* Fewer compiler errors
* Where do the errors go?
* Are there any problems that come from dynamic typing?

+++
## Dynamic typing
Sometimes problems can hide:
```sh
>>> print (names)
['John', 'Paul', 'George', 3]
```

+++
## Dynamic typing
Sometimes incorrect types break things:
```sh
>>> len(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
```
The Traceback shows where the error occurred, and what sort of error it is