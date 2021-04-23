# Python Regular Expression's Cheat Sheet (borrowed from pythex)

## Special Characters

- `\` escape special characters
- `.` matches any character
- `^` matches beginning of string
- `$` matches end of string
- `[5b-d]` matches any chars '5', 'b', 'c' or 'd'
- `[^a-c6]` matches any char except 'a', 'b', 'c' or '6'
- `R|S` matches either regex R or regex S
- `()` creates a capture group and indicates precedence

## Quantifiers

- `*` 0 or more (append ? for non-greedy)
- `+` 1 or more (append ? for non-greedy)
- `?` 0 or 1 (append ? for non-greedy)
- `{m}` exactly mm occurrences
- `{m, n}` from m to n. m defaults to 0, n to infinity
- `{m, n}?` from m to n, as few as possible

## Special sequences

- `\A` start of string
- `\b` matches empty string at word boundary (between \w and \W)
- `\B` matches empty string not at word boundary
- `\d` digit
- `\D` non-digit
- `\s` whitespace: [ \t\n\r\f\v]
- `\S` non-whitespace
- `\w` alphanumeric: [0-9a-zA-Z_]
- `\W` non-alphanumeric
- `\Z` end of string
- `\g<id>` matches a previously defined group

## Extensions

- `(?iLmsux)` Matches empty string, sets re.X flags
- `(?:...)` Non-capturing version of regular parentheses
- `(?P<name>...)` Creates a named capturing group.
- `(?P=name)` Matches whatever matched previously named group
- `(?#...)` A comment; ignored.
- `(?=...)` Lookahead assertion: Matches without consuming
- `(?!...)` Negative lookahead assertion
- `(?<=...)` Lookbehind assertion: Matches if preceded
- `(?<!...)` Negative lookbehind assertion
- `(?(id)yes|no)` Match 'yes' if group 'id' matched, else 'no'

## (1) `.` Matches any single character except newline

```
>>> s = "foo.123.bar"
>>> re.search(".", s)
<re.Match object; span=(0, 1), match='f'>
>>>
>>> re.search('\.', s)
<re.Match object; span=(3, 4), match='.'>
>>>
```

## (2) `^` Anchors a match at the start of a string

```
>>> s = "foo123bar"
>>> re.search('^f', s)
<re.Match object; span=(0, 1), match='f'>
>>>
```

## (3) `$` Anchors a match at the end of a string

```
>>> s = 'foo123oof'
>>> re.search('f', s)
<re.Match object; span=(0, 1), match='f'>
>>> re.search('f$', s)
<re.Match object; span=(8, 9), match='f'>
>>>
```

## (4) `*` Matches zero or more repetitions

```
>>> s = 'foo123'
>>> re.search('fo*', s)
<re.Match object; span=(0, 3), match='foo'>
>>> s = 'f123'
>>> re.search('fo*', s)
<re.Match object; span=(0, 1), match='f'>
>>>
```

## (5) `+` Matches one or more repetitions

```
>>> s = 'foo123'
>>> re.search('fo+', s)
<re.Match object; span=(0, 3), match='foo'>
>>> s = 'f123'
>>> re.search('fo+', s)
>>>
```

## (6) `{}` Matches an explicitly specified number of repetitions

```
>>> s = 'foo'
>>> re.search('o{1,2}', s)
<re.Match object; span=(1, 3), match='oo'>
>>> re.search('o{1}', s)
<re.Match object; span=(1, 2), match='o'>
>>>
```

## (7) `\` Escapes a metacharacter of its special meaning

```
>>> s = 'foo123bar'
>>>
>>> re.search('\d+', s)
<re.Match object; span=(3, 6), match='123'>
>>> re.search('\D+', s)
<re.Match object; span=(0, 3), match='foo'>
>>>
```

## (8) `[]` Specifies a character class

```
>>> s = 'foo123bar'
>>> re.search('[0-9]{3}', s)
<re.Match object; span=(3, 6), match='123'>
>>> re.search('[a-z]*', s)
<re.Match object; span=(0, 3), match='foo'>
```
