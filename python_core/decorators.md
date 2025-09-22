
# 📘 Python Decorators Cheat Sheet

**Wrapping Functions & Classes**

---

## 1. What is a Decorator?

* A **function that takes another function (or class) as input** and returns a modified/enhanced version.
* Commonly used for logging, timing, access control, caching, etc.

---

## 2. Basic Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 3. Function Decorators

| Pattern           | Example                                                                                                                                                                                                            | Use                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| Simple            | `@decorator`                                                                                                                                                                                                       | Wraps a function.            |
| With args         | `python\ndef repeat(n):\n    def decorator(func):\n        def wrapper(*a,**kw):\n            for _ in range(n): func(*a,**kw)\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef hi(): print("hi")` | Parameterized decorator.     |
| Preserve metadata | `python\nfrom functools import wraps\n\ndef deco(f):\n    @wraps(f)\n    def wrapper(*a,**kw):\n        return f(*a,**kw)\n    return wrapper`                                                                     | Keeps `__name__`, `__doc__`. |

---

## 4. Built-in Decorators

| Decorator       | Example                                                            | Purpose                          |
| --------------- | ------------------------------------------------------------------ | -------------------------------- |
| `@staticmethod` | `python\nclass A:\n    @staticmethod\n    def util(): ...`         | Method without `self`.           |
| `@classmethod`  | `python\nclass A:\n    @classmethod\n    def from_str(cls,s): ...` | Operates on class, not instance. |
| `@property`     | `python\nclass A:\n    @property\n    def val(self): return 10`    | Getter like attribute.           |

---

## 5. Common Uses

* **Logging**

```python
def log(func):
    def wrapper(*a, **kw):
        print(f"Calling {func.__name__}")
        return func(*a, **kw)
    return wrapper
```

* **Timing**

```python
import time
def timer(func):
    def wrapper(*a, **kw):
        start = time.time()
        result = func(*a, **kw)
        print("Elapsed:", time.time()-start)
        return result
    return wrapper
```

* **Caching**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n<2 else fib(n-1)+fib(n-2)
```

---

## 6. Class Decorators

```python
def add_repr(cls):
    cls.__repr__ = lambda self: f"<{cls.__name__} {self.__dict__}>"
    return cls

@add_repr
class Point:
    def __init__(self,x,y): self.x,self.y=x,y
```

---

## 7. Stacking Decorators

```python
@deco1
@deco2
def f():
    ...
# Equivalent to: f = deco1(deco2(f))
```

---

## 8. Beginner Pitfalls

* ❌ Forgetting `functools.wraps` → function metadata lost.
* ❌ Using decorators with side effects on import.
* ❌ Over-decorating — makes debugging harder.
* ❌ Mixing `@staticmethod` and `@classmethod` incorrectly.

---
