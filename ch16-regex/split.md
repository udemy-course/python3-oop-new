# split

## re.split(<regex>, <string>, maxsplit=0, flags=0)

Splits a string into substrings.

```
>>> import re
>>> s = 'foo, bar, baz, qux, quux, corge'
>>>
>>> re.split(r",\s*", s)
['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>>
>>> re.split(r',\s*', s, maxsplit=3)
['foo', 'bar', 'baz', 'qux, quux, corge']
>>>
```
