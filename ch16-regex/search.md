
# Searching Functions

Searching functions scan a search string for one or more matches of the specified regex:

| Function	|Description|
|-----------|------------|
| re.search()	|Scans a string for a regex match|
| re.match()	|Looks for a regex match at the beginning of a string|
| re.fullmatch()|	Looks for a regex match on an entire string|
| re.findall()	|Returns a list of all regex matches in a string|
| re.finditer()	|Returns an iterator that yields regex matches from a string|


## re.match() Looks for a regex match at the beginning of a string.

```
>>> import re
>>> s = "foo123bar"
>>> a = re.search("\d+", s)
>>> a
<re.Match object; span=(3, 6), match='123'>
>>> b = re.match("\d+", s)
>>> b
```

## re.fullmatch() Looks for a regex match on an entire string.

```
>>> print(re.fullmatch(r'\d+', '123foo'))
None
>>> print(re.fullmatch(r'\d+', 'foo123'))
None
>>> print(re.fullmatch(r'\d+', 'foo123bar'))
None
>>> re.fullmatch(r'\d+', '123')
<re.Match object; span=(0, 3), match='123'>
>>> re.search(r'^\d+$', '123')
<re.Match object; span=(0, 3), match='123'>
>>>
```

## re.findall() Returns a list of all matches of a regex in a string.

```
>>> s = "123foo456bar"
>>> re.match("\d+", s)
<re.Match object; span=(0, 3), match='123'>
>>> re.search("\d+", s)
<re.Match object; span=(0, 3), match='123'>
>>> re.fullmatch("\d+", s)
>>> re.findall("\d+", s)
['123', '456']
>>>
```

findall and group

```
>>> re.findall(r'(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')
[('foo', 'bar'), ('baz', 'qux'), ('quux', 'corge')]
>>>
```


## re.finditer() Returns an iterator that yields regex matches.

```
>>> s = "123foo456bar"
>>> a = re.finditer("\d+", s)
>>> a
<callable_iterator object at 0x7febeb482160>
>>> next(a)
<re.Match object; span=(0, 3), match='123'>
>>> next(a)
<re.Match object; span=(6, 9), match='456'>
>>> next(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

