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


^ - Beginning. Matches the Beginning of the string
[] - Character set. Match any character in the set
+ - Quantifier. Match 1 or more of the preceding token.
$ - End. Matches the end of the string
\. - Escaped Character. Matches "." character


*More Regex characters*:

`\d` digit 0-9
`\w` letter, digit or underscore
`\s` whitespace character
`\D` not digit
`\W` not word
`\S` not a whitespace character
`.` any character except line break
