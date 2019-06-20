## Bytes & Byte Arrays

* Bytes objects are immutable sequences of single bytes. 

* It uses a b prefix with normal string syntax  b'python'. 

```python
>>> x = b"Bytes objects are immutable sequences of single bytes" 
>>> print(x) 
b'Bytes objects are immutable sequences of single bytes'
>>>
 
```

+++

## bytes()
* Returns a new "bytes" object 
* It's range is 0 <= x < 256

* Prints as ASCII characters when displayed.

```
Syntax

bytes([source[, encoding[, errors]]])

```

+++

## bytearray()

* Return a new array of bytes. 
* The bytearray type is a mutable sequence of integers in the range 0 <= x < 256. 

```
Syntax:

bytearray([source[, encoding[, errors]]])

```


+++

## Converts Bytes to Strings

  
```
#create a bytes object
x = b'El ni\xc3\xb1o come camar\xc3\xb3n' 
print(x) 

```

Output:

```
b'El ni\xc3\xb1o come camar\xc3\xb3n' 

```

+++

```
# create a string using the decode() method of bytes.
 #This method takes an encoding argument, such as UTF-8, and optionally an errors argument.
 x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
 s = x.decode()
 print(type(s))
print(s) 

```


Output:

```
El niño come camarón

```