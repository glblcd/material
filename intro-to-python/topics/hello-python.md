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