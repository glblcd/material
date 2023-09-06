## Tuple
A way to join related data:
```python
hostport = ("accdev1", 3213)
```

Tuple is immutable unlike python list 

+++
## Tuple
Data elements don't have names
```python
sam = ("Sam Moorhouse", 1984)
```
* What does *1984* refer to? (Careful!)
* Is there a better way?


+++ 
## Tuple creation and destructuring

Destructuring the tuple means getting the values from the tuple in separate variables

```
ho_techical = ("Ghana", 5000, "Engineering") 

(location, no_student, type_ofcollege) = ho_technical

# print college location
print(location)
 
# print no of student
print(no_student)

# print type of college
print(type_ofcollege)
```