## Conditionals
* if | else | elif
* allows us to affect the *flow of control*
```python
sam = ("Sam Moorhouse", 1984)
name, yob = sam
if yob < 1990:
    print name + " is an old dude"
else:
    print name + "must still be pretty young"
```

@[1-2](Tuple creation and deconstruction)

Note:
* Tuple construction and deconstruction
* We use `<` which is an _operator_ which returns _boolean_. 

+++
## Conditionals
* notice that colon
* and the indentation!
```python
yob = (int)(raw_input ( "Enter the year you were born: " ))
now = 2018
if (now - yob) < 18:
    print "you're still a child"
elif (now - yob) < 25:
    print "whoa! Still learning!"
else:
    print "OLD!"
```

Note:
* We cast the result of `raw_input` to `int`

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
now = 2018
status = "young" if (now - yob) < 30 else "old"
print status
```