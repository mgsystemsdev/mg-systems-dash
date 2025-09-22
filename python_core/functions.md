
# 📘 Python Functions Cheat Sheet

**Defining & Using Functions**

---

## 1. Defining Functions

| Syntax      | Example                                                    | Explanation            |
| ----------- | ---------------------------------------------------------- | ---------------------- |
| Basic       | `def greet(): print("Hi")`                                 | Function with no args. |
| With params | `def greet(name): print("Hi", name)`                       | Accepts input.         |
| With return | `def add(a,b): return a+b`                                 | Returns value.         |
| Docstring   | `python\ndef f(x):\n    """Squares x."""\n    return x**2` | Documentation string.  |

---

## 2. Parameters

| Type       | Example                                    | Notes                                    |
| ---------- | ------------------------------------------ | ---------------------------------------- |
| Positional | `def f(x,y)`                               | Order matters.                           |
| Default    | `def f(x=10)`                              | Uses default if not passed.              |
| Keyword    | `f(y=2,x=1)`                               | Specify by name.                         |
| `*args`    | `def f(*nums)`                             | Collects extra positional args as tuple. |
| `**kwargs` | `def f(**opts)`                            | Collects extra keyword args as dict.     |
| Mixed      | `python\ndef f(a,b=2,*args,**kwargs): ...` | Combine all.                             |

---

## 3. Return Values

| Command         | Example      | Result          |
| --------------- | ------------ | --------------- |
| Return single   | `return 5`   | Returns value.  |
| Return multiple | `return a,b` | Returns tuple.  |
| Implicit return | No `return`  | Returns `None`. |

---

## 4. Scope & Variables

| Concept  | Example                 | Explanation                         |
| -------- | ----------------------- | ----------------------------------- |
| Local    | Defined inside          | Exists only in function.            |
| Global   | Declared outside        | Use `global` to modify.             |
| Nonlocal | Inside nested functions | Use `nonlocal` to modify outer var. |

---

## 5. Anonymous (Lambda) Functions

```python
square = lambda x: x**2
print(square(5))  # 25
```

* ✅ Useful for short throwaway functions (sorting, mapping).
* ⚠️ Avoid for complex logic → use `def`.

---

## 6. Higher-Order Functions

| Function   | Example                         | Explanation     |
| ---------- | ------------------------------- | --------------- |
| `map()`    | `map(str, [1,2])` → `["1","2"]` | Apply function. |
| `filter()` | `filter(lambda x:x>0,lst)`      | Keep if True.   |
| `reduce()` | `reduce(lambda x,y:x+y, lst)`   | Fold sequence.  |
| `sorted()` | `sorted(lst, key=len)`          | Custom sort.    |

---

## 7. Function Tools

| Tool                  | Example              | Explanation            |
| --------------------- | -------------------- | ---------------------- |
| `*` unpacking         | `f(*[1,2])`          | Expand list to args.   |
| `**` unpacking        | `f(**{"a":1,"b":2})` | Expand dict to kwargs. |
| `functools.lru_cache` | Memoization          | Cache results.         |
| `functools.partial`   | `partial(func, a=1)` | Fix arguments.         |

---

## 8. Decorators (Basics)

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Running", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name): print("Hi", name)
```

---

## 9. Beginner Pitfalls

* ❌ Forgetting `return` → function returns `None`.
* ❌ Modifying globals without `global` keyword.
* ❌ Mutable defaults (`def f(x=[])`) → shared across calls.
* ❌ Overusing lambdas instead of proper functions.

---

✅ This is the **full reference for Python functions** — from basics to advanced tools.

