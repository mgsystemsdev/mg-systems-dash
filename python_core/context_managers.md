

# 📘 Python Context Managers Cheat Sheet

**Managing Resources Safely**

---

## 1. What is a Context Manager?

* A construct that handles **setup and teardown** automatically.
* Most common example: **file handling**.

```python
with open("file.txt","r") as f:
    data = f.read()
# file automatically closed
```

---

## 2. The `with` Statement

General form:

```python
with context_manager as var:
    # use var
```

* Ensures cleanup happens (close file, release lock, rollback DB, etc.).
* Works with anything implementing `__enter__` and `__exit__`.

---

## 3. Writing a Custom Context Manager (Class)

```python
class MyContext:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        return False  # re-raise exceptions if any

with MyContext():
    print("Inside")
```

---

## 4. Writing with `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def my_manager():
    print("Setup")
    yield "resource"
    print("Teardown")

with my_manager() as r:
    print("Using", r)
```

---

## 5. Useful `contextlib` Tools

| Tool                           | Example                                                                                                                                                          | Use                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `@contextmanager`              | See above                                                                                                                                                        | Write managers with `yield`.           |
| `contextlib.closing()`         | `python\nfrom contextlib import closing\nwith closing(open("file.txt")) as f: ...`                                                                               | Ensure close method called.            |
| `contextlib.suppress()`        | `python\nfrom contextlib import suppress\nwith suppress(FileNotFoundError):\n    os.remove("temp.txt")`                                                          | Ignore specific exceptions.            |
| `contextlib.redirect_stdout()` | `python\nfrom contextlib import redirect_stdout\nwith open("out.txt","w") as f:\n    with redirect_stdout(f):\n        help(len)`                                | Redirect output.                       |
| `ExitStack`                    | `python\nfrom contextlib import ExitStack\nwith ExitStack() as stack:\n    f1 = stack.enter_context(open("a.txt"))\n    f2 = stack.enter_context(open("b.txt"))` | Manage multiple resources dynamically. |

---

## 6. Nested Contexts

Python ≥3.1 allows **multiple contexts in one line**:

```python
with open("a.txt") as f1, open("b.txt") as f2:
    ...
```

---

## 7. Common Built-in Context Managers

* `open()` → files
* `threading.Lock()` → synchronization
* `decimal.localcontext()` → temporary math precision
* `sqlite3.connect()` → database connections
* `tempfile.TemporaryFile()` → auto-clean temp files

---

## 8. Beginner Pitfalls

* ❌ Forgetting `with` → resources may leak.
* ❌ Returning `True` from `__exit__` unintentionally → suppresses exceptions.
* ❌ Not using `contextlib.suppress()` properly → hides real bugs if overused.
* ❌ Writing complex logic inside `__enter__/__exit__` instead of focusing on setup/teardown.

---
