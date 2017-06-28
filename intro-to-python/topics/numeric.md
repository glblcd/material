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

>>> float(1)
1.0

>>>int(3.999999999)
3
```

+++
## Float
```sh
>>> import math

>>>math.floor(3.99999)
3.0

>>>math.ceil(3.99999)
4.0
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