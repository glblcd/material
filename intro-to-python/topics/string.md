## String
Use "" or '', doesn't matter:
```sh
>>> print "hello" == 'hello'
True
```

+++
##String
...or Unicode (with care!)
```sh
>>> command = "⌘"
>>> command
'\xe2\x8c\x98'
>>> print command
⌘
```

+++
##String
Some *builtin* functions work with variables:
```sh
>>> len("hello")
5
```

https://docs.python.org/3/library/functions.html