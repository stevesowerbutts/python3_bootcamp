# Using regex with python

Use the `re` module https://docs.python.org/3/library/re.html

```
import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

>>> pattern.search("12343243 jfk") # No matches

>>> res = pattern.search("call 310 445-1234") # Match object
>>> res
<re.Match object; span=(5, 17), match='310 445-1234'>

# To extract the match:
res.group()
'310 445-1234'
```

The `r` means its using a raw string. (would have to escape the slashes otherwise. eg. `\\d`)

`pattern.search` -  Scan through string looking for the first location where this regular expression produces a match

`pattern.findall` - Return all non-overlapping matches of pattern in string, as a list of strings

You can also use re directly to to regex search without compiling first .. however this will compile the pattern each time (ok for a one off):
```
re.search(r'\d{3} \d{3}-\d{4}', "call 310 445-1234").group()
'310 445-1234'
```

*Best practice*

Is to compile your regex pattern first
- extra line, but generally better option
- Only compile once and then use that pattern multiple times.

see phone.py

### Parsing Urls with regex
See url.py for example regex

```
url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
```

Can split the match into groups of matches, which can be used separately
In above example, items wrapped in `()` or grouped together.
- match.groups() - all groups.
  `('https', 'www.my-website.com', '/bio?data=blah&dog=yes')`
- match.group() - produces whole match (same as `match.group(0)`)
  `'https://www.my-website.com/bio?data=blah&dog=yes'`
- match.group(1) - First group
  `'https'`

You can also label the groups to make matching easier, using syntax `?P<label>`:
```
name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
matches = name_regex.search('Mr. Bob James')

print(matches.group('first'))
>>> Bob
```

### Compilation flags
https://docs.python.org/3/howto/regex.html#compilation-flags

See docs for full list, but some useful options:

- IGNORECASE, I - Do case-insensitive matches.

- MULTILINE, M - Multi-line matching, affecting ^ and $.

- VERBOSE, X (for ‘extended’) - Enable verbose REs, which can be organized more cleanly and understandably.* (see ../flags.py)
  ```
  # pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

  # Can use re.VERBOSE (or re.X) to write the above regex over multiple lines, for easier reading
  pat = re.compile(r"""
  	^([a-z0-9_\.-]+)	#first part of email
  	@					        #single @ sign
  	([0-9a-z\.-]+)		#email provider
  	\.					      #single period
  	([a-z\.]{2,6})$		#com, org, net, etc.
  """, re.VERBOSE)
  ```
You can use multiple flags by piping them together `re.VERBOSE | re.IGNORECASE`

### Regex substitutions
Another common task is to find all the matches for a pattern, and replace them with a different string. The `sub()` method takes a replacement value, which can be either a string or a function, and the string to be processed.

There’s also a syntax for referring to named groups as defined by the (?P<name>...) syntax. `\g<name>` will use the substring matched by the group named name, and `\g<number>`. eg. `\g<1>` will match the first group.

```
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)

# Last night Mrs. D and Mr. w murdered Ms. C
```

You could also use `.sub()` to swap the order of the groups. See books.py
```
>>> result = pattern.sub("\g<2> \g<1>", text)
>>> result
'Last night D Mrs. and w Mr. murdered C Ms.'
```
