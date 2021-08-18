# Modules
Modules keep python files small, reusable code

### Builtin Modules
Different ways to import
```
import random

random.choice(["apple","banana","cherry"])

# Can rename or shorten to the name as well
import randomm as rand
rand.shuffle(["apple","banana","cherry"])
```

Import parts of a Module
* import only the functions that you require using `from`
* can import everything if required
```
from random import choice, shuffle
from random import *

from random import choice as gimme_one, shuffle as mix_up
print(gimme_one(["apple","banana","cherry"]))
print(mix_up(["apple","banana","cherry"]))
```

### Custom Modules

Import own code as a module from a file
* see example from fruits.py

### External Modules
To use external modules, need to install using pip
`python3 -m pip install NAME_OF_PACKAGE`

Then import in the same way as other modules.
See `colors.py` and `ascii_art.py` for examples

### autpep8 package to cleanup code
Applies autopep style guide to you code, has different levels off aggressiveness in terms of what it will change.
`python3 -m pip install autopep8`
* default is mainly whitespace changes, adding multiple `-a` will change syntax eg.
```
yes: if greeting:
No: if greeting == True:
No: if greeting is True:
```
```
$ autopep8 -d 22.Modules/apples.py
--- original/22.Modules/apples.py
+++ fixed/22.Modules/apples.py
@@ -1,5 +1,6 @@
 def offer():
-	return "Hey do you like apples?"
+    return "Hey do you like apples?"
+

 def bake():
-	return "Mmmm, pie..."
\ No newline at end of file
+    return "Mmmm, pie..."
```

### The __name__ variable

Every Python file has its own __name__ variable
- by default if the file is the main file being run, its __name__ value is `__main__`
- otherwise, its value is the file name (eg. if its being imported)

When you import using python,
- Tries to find the module (throws an error if it fails)
- Runs the code inside of the module being imported

Ignoring code on import
```
if __name__ == "__main__":
  # this code will only runs
  # if the file is the main file
```
