## Advanced Python
##### Global Code | 2018
![Advanced Python](/assets/img/course-logo.png)

---
## Pip
Package manager for Python
* `pip install beautifulsoup4`
* type `pip`

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


THINGS TO COVER

* PIP
* filter, map
* list comprehensions