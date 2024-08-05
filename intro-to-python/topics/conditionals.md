## Conditionals
* if | else | elif
* allows us to affect the *flow of control*
```python
sam = ("Sam Moorhouse", 1984)
(name, yob) = sam
if yob < 1990:
    print (name + " is an old dude")
else:
    print (name + "must still be pretty young")
```
+++
## Conditionals
* notice that colon
* and the indentation!
```python
yob = int(input( "Enter the year you were born: " ))
now = 2024
if (now - yob) < 18:
    print ("you're still a child")
elif (now - yob) < 25:
    print ("whoa! Still learning!")
else:
    print ("OLD!")
```

Note:
* We cast the result of `raw_input` to `int`
* What happens if we enter something that's not an `int`
+++
### Conditional Operators

Changing the flow of control based on different conditions

* '>'
* '>'
* '=='
* '!='
* '<='
* '>=' 
We can also combine different conditions using the logical operators
* and,  or

+++
## Conditionals
* conditions are *evaluated in order*
* `print` is an inbuilt *function*
* we can attempt to *cast* one data type to another
  * Why should we cast data types?
  * Does it always work?
  try 
  ```
  some_string = int("caststring")
  ```
  * Should it?!

+++
## Conditionals
* `if` in an *expression*
  * it evaluates to a value
```python
yob = int(input("Enter the year you were born:"))
now = 2024
status = "young" if (now - yob) < 30 else "old"
print (status)
```