## Dictionary
A hash table
* sequence of key-value pairs
* efficient lookup & insertion
* elements aren't ordered

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
