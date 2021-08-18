## File.io

### Reading files

Use the `open` function
- open returns a file object to you
- if the file cant be opened, returns OSError

### Cursor movement
Python reads files by using a Cursor
This is like the cursor you see when youre typing.
After opening and reading a file, the cursor stops at the end.

```
>>> f = open("/Users/steve.sowerbutts/udemy/python3_bootcamp/30.file.io/story.txt")
>>> f.read()
'This short story is really short\n'
>>> f.read()
''
```

To move the cursor you can use `seek`
```
>>> f.seek(0)
0
>>> f.read()
'This short story is really short\n'
>>> f.seek(1)
1
>>> f.read()
'his short story is really short\n'
```

### Closing a file
Always need to close a file once finished, python keeps files open by default.
Use the `close` method
Check if a file is closed with the `closed` attribute
Once closed, a file cant be read again

```
>>> f.closed
False
>>> f.close()
>>> f.closed
True
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### with Blocks
Using `with open()` automatically closes the file after.

```
>>> with open("/Users/steve.sowerbutts/udemy/python3_bootcamp/30.file.io/story.txt") as file:
...     file.read()
...
'This short story is really short\n'
>>> file.closed
True
```

### Writing to Text files
Have to use the open function to write to a file
Specify the `w` as the second argument.
  - Whenever you write to a file using the `w` argument, the original contents are overwritten
```
>>> with open('write.txt') as file:
...     file.read()
...
'Original write.txt\n'

>>> with open('write.txt', 'w') as file:
...     file.write('New lines for write.txt ')
...     file.write('New lines for write.txt')
...
>>> with open('write.txt') as file:
...     file.read()
...
'New lines for write.txt New lines for write.txt'
```

You can also write to a non existing file and it will be created.


### Modes for opening files
r - Read a file
w - Write to a file (previous contents removed)
a - Append to a file (keeps previous content)
    - This only ever appends to the end of the file
r+ - By default starts at the beginning of the file,
    - overwrites content if exists
    - Can move the cursor around using seek to add at different points of the file
    - This only works for existing files
