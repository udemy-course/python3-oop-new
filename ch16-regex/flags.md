# Supported Regular Expression Flags

| Short Name	|Long Name	|Effect|
|----------------|----------|------|
| re.I|	re.IGNORECASE	|Makes matching of alphabetic characters case-insensitive|
| re.M|	re.MULTILINE|	Causes start-of-string and end-of-string anchors to match embedded newlines|
| re.S|	re.DOTALL	|Causes the dot metacharacter to match a newline|
| re.X|	re.VERBOSE	|Allows inclusion of whitespace and comments within a regular expression|
| ----|	re.DEBUG	|Causes the regex parser to display debugging information to the console|
| re.A|	re.ASCII	|Specifies ASCII encoding for character classification|
| re.U|	re.UNICODE	|Specifies Unicode encoding for character classification|
| re.L| re.LOCALE	|Specifies encoding for character classification based on the current locale|


```
>>> import re
>>> re.search("a+", "aaaAAA")
<re.Match object; span=(0, 3), match='aaa'>
>>> re.search("A+", "aaaAAA")
<re.Match object; span=(3, 6), match='AAA'>
>>> re.search("a+", "aaaAAA", re.I)
<re.Match object; span=(0, 6), match='aaaAAA'>
>>>
```

```
>>> s = 'foo\nbar\nbaz'
>>> re.search("^foo", s)
<re.Match object; span=(0, 3), match='foo'>
>>> re.search("^bar", s)
>>> re.search("bar$", s)
>>> re.search("baz$", s)
<re.Match object; span=(8, 11), match='baz'>
>>>
>>> re.search("^bar", s)
>>> re.search("^bar", s, re.MULTILINE)
<re.Match object; span=(4, 7), match='bar'>
>>>
```

```
>>> regex = r'''^               # Start of string
...             (\(\d{3}\))?    # Optional area code
...             \s*             # Optional whitespace
...             \d{3}           # Three-digit prefix
...             [-.]            # Separator character
...             \d{4}           # Four-digit line number
...             $               # Anchor at end of string
...             '''

>>> re.search(regex, '414.9229', re.VERBOSE)
<_sre.SRE_Match object; span=(0, 8), match='414.9229'>
>>> re.search(regex, '414-9229', re.VERBOSE)
<_sre.SRE_Match object; span=(0, 8), match='414-9229'>
>>> re.search(regex, '(712)414-9229', re.X)
<_sre.SRE_Match object; span=(0, 13), match='(712)414-9229'>
>>> re.search(regex, '(712) 414-9229', re.X)
<_sre.SRE_Match object; span=(0, 14), match='(712) 414-9229'>
```
