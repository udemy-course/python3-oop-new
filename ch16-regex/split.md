# split

## re.split(<regex>, <string>, maxsplit=0, flags=0)

Splits a string into substrings.

with string split

```
>>> s = 'foo, bar, baz,qux, quux,     corge'
>>> [a.strip() for a in s.split(',')]
['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>>
```

with re.split()

```
>>> s = 'foo, bar, baz,qux, quux,     corge'
>>> re.split(r",\s*", s)
['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>>
>>> re.split(r',\s*', s, maxsplit=3)
['foo', 'bar', 'baz', 'qux, quux, corge']
>>>
```
