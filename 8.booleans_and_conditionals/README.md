# Boolean and Conditional logic
### Truthiness
Values that resolve to True = "Truthy", False = "falsy"

Besides False conditional checks, other values that are naturally falsy include:
- empty objects
- empty strings
- None
- Zero

### is vs "=="

Very similar comparators, however they are not the same.
Is is only True if the variables reference the same items in memory.

`==` checks values
`is` checks memory

```
a = [1, 2, 3]
b = [1, 2, 3]

a == b # True
a is b # False
```
