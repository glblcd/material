## Advanced Python
##### Global Code | 2024
![Advanced Python](/assets/img/python-360x361.png)

---
## Pip
Package manager for Python
* `pip install beautifulsoup4`
* type `pip`

Note:

A lot less material here, really we're just rounding off the topic. 

Here, the point isn't to talk about beautifulsoup, rather it's that Python comes with a rich ecosystem of open-source packages you can use in your code.

It's a good opportunity to talk about modularisation of code - functions, classes & modules in Python, and how we can expose our own functionality through these mechanisms.

+++
## Pip
* `pip show --files beautifulsoup4`
```python
from bs4 import BeautifulSoup
```
* `pip uninstall beautifulsoup4`

+++
## Pip
RTFM: https://pip.pypa.io/

---
## Map
Applies a function to list elements
```python
names = ["sam", "john", "james"]
map(len, names)
```

Note:

Feel free to extend this with discussions of:
* Big-O for time and space complexity
* The dict-ness of all python objects exposed via _.__dict__()

+++
## Map
Keep going:
```python
def sqr(x): return x ** 2
map(sqr, map(len,names))
```

---
## Lambda
A function without a name
```python
items = [1, 2, 3, 4, 5]
squares = map((lambda x: x ** 2), items)
```

+++
## Lambda
* used *loads*
* *pythonic*

Note:
What does "pythonic" mean - all programming languages expose the same fundamentals, but what makes one different from the other? Syntax & semantics, sure, but developers also like to build concensus around conventions. 

---
## Filter
Remove items from a list
```python
def too_old(x): return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
filter(too_old, ages)
```

---
## Let's do it!
![Hack](/assets/img/hack-600.png)