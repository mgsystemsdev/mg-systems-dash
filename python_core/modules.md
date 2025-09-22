

# 📘 Python Imports & Modules Cheat Sheet

**Organizing, Importing, and Using Code**

---

## 1. Creating & Importing a Module

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"

# main.py
import mymodule
print(mymodule.greet("Alice"))
```

---

## 2. Import Variations

| Syntax                 | Example                                 | Explanation           |
| ---------------------- | --------------------------------------- | --------------------- |
| Import whole module    | `import math`                           | Use `math.sqrt(9)`    |
| Import with alias      | `import numpy as np`                    | Shorter name          |
| Import specific        | `from math import sqrt`                 | Direct use: `sqrt(9)` |
| Multiple import        | `from math import sqrt, pi`             | Import several        |
| Import all ⚠️          | `from math import *`                    | Pollutes namespace    |
| Import inside function | `python\ndef f():\n    import random\n` | Local scope           |

---

## 3. Module Search Path

Python looks for modules in:

```python
import sys
print(sys.path)
```

* Current directory
* `PYTHONPATH` env var
* Site-packages (installed libs)

---

## 4. Packages (Modules in Folders)

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

```python
import mypackage.module1
from mypackage import module2
```

* `__init__.py` makes folder a package.
* Can be empty or used for package setup.

---

## 5. Relative Imports (inside packages)

```python
# in module2.py
from . import module1         # relative import
from ..subpackage import mod  # go up a level
```

⚠️ Works only inside packages, not in standalone scripts.

---

## 6. Standard Library

Python comes with 200+ built-in modules. Common ones:

* `math`, `random`, `statistics` → math
* `os`, `sys`, `pathlib`, `shutil` → system/files
* `datetime`, `time`, `calendar` → dates/times
* `json`, `csv`, `sqlite3` → data handling
* `re` → regex
* `itertools`, `functools`, `collections` → advanced tools

---

## 7. Installing External Packages

```bash
pip install requests
```

```python
import requests
```

⚠️ Keep dependencies inside a **virtual environment** (`venv`, `conda`, or `poetry`).

---

## 8. Best Practices

* ✅ Use aliases for big libs (`numpy as np`).
* ✅ Import only what you need (`from math import sqrt`).
* ✅ Group imports:

  1. Standard library
  2. Third-party libs
  3. Local modules
* ✅ Use absolute imports in larger projects.
* ❌ Avoid `from module import *` (namespace pollution).

---

✅ With this, you have the **full cheat sheet for imports & modules**: from basics to packages, relative imports, and best practices.

