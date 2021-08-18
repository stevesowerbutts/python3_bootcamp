# List comprehensions

Like slices list comprehensions also start with []

```
# capitalize the first letter of each friend
[friend.capitalize() for friend in ['ashley', 'matt', 'michael']]

['Ashley', 'Matt', 'Michael']
```

# conditionals in list comprehensions

1. assign even numbers from a list to a variable:

```
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
answer2 == [2, 4, 6]
```

2. Use slicing in list comprehension to reverse and make lower case
```
answer2 = [n[::-1].lower() for n in ['Elie', 'Tim', 'Matt']]
answer2 == ['eile', 'mit', 'ttam']
```

3. Find numbers between 1-100 that are divisible by 12
```
[a for a in range(1,101) if a % 12 ==0]
[12, 24, 36, 48, 60, 72, 84, 96]
```

# Nested lists

You can also use list comprehension in nested lists

1. create 3 lists of [0,1,2]
```
[[a for a in range(0,3)] for num in range(0,3)]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```
