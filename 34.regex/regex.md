# Regular expressions

A way of describing patterns within search strings
Can test regx here: https://regexr.com/
http://www.rexegg.com/regex-quickstart.html
https://pythex.org/

## Validating email addresses

Starts with 1 or more `letter, number, +, _, -, .` then
A single `@` sign then
1 or more `letter, number or -` then
a single dot `.` then
ends with 1 or more `leter, number, .`

(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)


`^` - Beginning. Matches the Beginning of the string
`[]` - Character set. Match any character in the set (ranges of characters)
`+` - Quantifier. Match 1 or more of the preceding token.
`$` - End. Matches the end of the string
`\.` - Escaped Character. Matches "." character


*More Regex characters*:

`\d` digit 0-9
`\w` letter, digit or underscore
`\s` whitespace character
`\D` not digit
`\W` not word
`\S` not a whitespace character
`.` any character except line break
`!` not a character
`[^xy]` One character that is not x or y
*Quantifiers*

`+` - Quantifier. Match 1 or more of the preceding token.
`{x}` - Exactly x times. {3} - 3 times
`{3,5}`- Three to five times
`{4,}` - Four or more times
`*` - Zero or more times
`?` - Zero or one time

*Anchors and Boundaries*
`^` - Beginning. Matches the Beginning of the string
`$` - End. Matches the end of the string
`\b` - word boundary - need at start and end ( `\b\w+\b` - matches only whole words)

*Logical OR (pipe character)*

`|` - used for or

`\d{3}\)|\d{3}` - would match `(123)` OR `123` - anything after the `|` is included in the OR statement

`(\(\d{3}\)|\d{3}) \d{3}` - need to wrap in `()` to create a group so that the OR only statement only applies to characters matched in that group.
  - this would match
  ```
  (413) 123
  413 123
  ```

`()` - are really useful for creating groups or components of matches

`([a-zA-Z]+?://)([a-zA-Z]+\.[a-zA-Z]+)` - matches http://google.com & https://yahoo.com
Match 1 has 2 groups  `http://` and `google.com`
Match 2 has 2 groups `https://` and `yahoo.com`

these groups can then be used by python
