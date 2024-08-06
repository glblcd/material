## Dictionary
A hash table -- what does that mean?
* An *association* -- a *key* is associated with a *value*
* Like a dictionary that translates between languages
* A basic data structure
* Can be thought of as a list of pairs
* Elements aren't ordered though

+++
## Dictionary
```sh
>>> people = {"robert": 33, "john": 23, "steve": 44 }
>>> people["robert"]
33

>>> people["janet"] = 25
>>>
```

+++
## Dictionary
```sh
>>> del people["steve"]
>>> people
{"robert": 33, "john": 23, "janet": 25 }
]
```

+++
## Dictionary
```sh
>>> people.keys()
['robert', 'john', 'janet']
```
> keys()

```sh
>>> people.values()
[33, 23, 25]
```
> values()

* items()
  * try it!
