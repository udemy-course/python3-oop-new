# groups

## captured group `(<regex>)`

```sh
>>> import re
>>> s = "one,two,three"
>>> result = re.search("(\w+),(\w+)", s)
>>> result
<re.Match object; span=(0, 7), match='one,two'>
>>> result.groups()
('one', 'two')
>>> result.group(0)
'one,two'
>>> result.group(1)
'one'
>>> result.group(2)
'two'
>>> result.group
'one,two'
>>>
>>> result[0]
'one,two'
>>> result[1]
'one'
>>> result[2]
'two'
>>>
```

## named captured group  `(?P<name><regex>)`

```sh
>>> s = "Sep 2010"
>>> result = re.search("(\w+)\s(\d+)", s)
>>> result
<re.Match object; span=(0, 8), match='Sep 2010'>
>>> result[0]
'Sep 2010'
>>> result[1]
'Sep'
>>> result[2]
'2010'
>>>
```

give each group a name

```sh
>>> s = "Sep 2010"
>>> result = re.search("(?P<month>\w+)\s(?P<year>\d+)", s)
>>> result
<re.Match object; span=(0, 8), match='Sep 2010'>
>>> result.groupdict()
{'month': 'Sep', 'year': '2010'}
>>>
```
