# Ints and Floats
Int is a whole number: 1, 2 etc
Float is a decimal number: 1.0, 99.12345

## Order hierarchy

*PEMDAS*
Parentheses
Exponents
Multiplication
Division
Addition
Subtraction

`1 + 2 * 5 / 3 = 4.33334` (Multiplication first, then Division, then addition)

`(1 + 2) * 5 / 3 = 5` (Parentheses first, then Multiplication, then Division)

## Weirder Operators

### Modulo `%`
It returns the remainder of dividing the left hand operand by right hand operand.
It's used to get the remainder of a division problem.
Primary use case is for figuring out if a number is even or odd.
eg.
  13 / 2 = 1 (Odd number)
  12 / 2 = 0 (Even number)

### Integer Division `//`
Floor division, ignores everything after the decimal and always returns an integer.

```
>>> 234 / 35
6.685714285714286
>>> 234 // 35
6
```
