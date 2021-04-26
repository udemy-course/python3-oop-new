# re.compile(<regex>, flags=0)

Compiles a regex into a regular expression object.

```
>>> import re
>>> re.search(r'\d+', 'foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>
>>>
>>> re_obj = re.compile(r'\d+')
>>> >>> type(re_obj)
<class '_sre.SRE_Pattern'>
>>>
>>> re.search(re_obj, 'foo123bar')
<_sre.SRE_Match object; span=(3, 6), match='123'>
>>>
```


with flags

```
>>> re.search('ba[rz]', 'FOOBARBAZ', flags=re.I)
<_sre.SRE_Match object; span=(3, 6), match='BAR'>
>>> re_obj = re.compile('ba[rz]', flags=re.I)
>>> re.search(re_obj, 'FOOBARBAZ')
<_sre.SRE_Match object; span=(3, 6), match='BAR'>
>>> re_obj.search('FOOBARBAZ')
<_sre.SRE_Match object; span=(3, 6), match='BAR'>
>>>
```
