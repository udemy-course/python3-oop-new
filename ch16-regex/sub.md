# Substitution Functions

|Function	| Description|
|-----------|-------------|
|re.sub()	|Scans a string for regex matches, replaces the matching portions of the string with the specified replacement string, and returns the result|
|re.subn()	|Behaves just like re.sub() but also returns information regarding the number of substitutions made|


```
>>> s = 'foo.123.bar.789.baz'
>>>
>>> re.sub(r'\d+', '#', s)
'foo.#.bar.#.baz'
>>>
>>> re.sub('[a-z]+', '*', s)
'*.123.*.789.*'
>>>
>>> re.subn('[a-z]+', '*', s)
('*.123.*.789.*', 3)
>>>
```

with captured groups

```
>>> s = r"123abc456"
>>>
>>> re.search("(\d+)[a-z]+(\d+)", s)
<re.Match object; span=(0, 9), match='123abc456'>
>>> re.search("(\d+)[a-z]+(\d+)", s).groups()
('123', '456')
>>> re.sub(r"(\d+)[a-z]+(\d+)", r"\2abc\1", s)
'456abc123'
>>>
```

Substitution by Function

```
>>> def foo(match_object):
...     s = match_object.group(0)
...     if s.isdigit():
...         return str(int(s) * 10)
...     else:
...         return s.upper()
...
>>>
>>> re.sub(r"\w+", foo, 'foo.10.bar.20.baz.30')
'FOO.100.BAR.200.BAZ.300'
>>>
```

Limiting the Number of Replacements

```
>>> re.sub(r"\w+", foo, 'foo.10.bar.20.baz.30')
'FOO.100.BAR.200.BAZ.300'
>>> re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux')
'xxx.xxx.xxx.xxx'
>>> re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2)
'xxx.xxx.baz.qux'
>>>
```
