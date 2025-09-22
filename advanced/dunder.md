

# 📘 Python Dunder (Magic) Methods Cheat Sheet

**Special Methods for Custom Class Behavior**

---

## 1. Object Construction & Representation

| Method                   | Purpose                      | Example                |
| ------------------------ | ---------------------------- | ---------------------- |
| `__init__(self, …)`      | Constructor                  | `obj = MyClass(x)`     |
| `__new__(cls, …)`        | Low-level constructor (rare) | Custom immutable types |
| `__del__(self)`          | Destructor (on GC)           | Cleanup resources      |
| `__repr__(self)`         | Official string (debug)      | `repr(obj)`            |
| `__str__(self)`          | User-friendly string         | `print(obj)`           |
| `__format__(self, spec)` | Formatting                   | `f"{obj:spec}"`        |
| `__bytes__(self)`        | Convert to `bytes`           | `bytes(obj)`           |

---

## 2. Attribute Access

| Method                           | Purpose                  | Example         |
| -------------------------------- | ------------------------ | --------------- |
| `__getattr__(self, name)`        | Called if attr not found | `obj.missing`   |
| `__getattribute__(self, name)`   | Called on every lookup   | Use carefully   |
| `__setattr__(self, name, value)` | Assign attribute         | `obj.x = 5`     |
| `__delattr__(self, name)`        | Delete attribute         | `del obj.x`     |
| `__dir__(self)`                  | Customize `dir(obj)`     | List attributes |

---

## 3. Containers & Iteration

| Method                        | Purpose     | Example           |
| ----------------------------- | ----------- | ----------------- |
| `__len__(self)`               | `len(obj)`  | Must return int   |
| `__getitem__(self, key)`      | Indexing    | `obj[key]`        |
| `__setitem__(self, key, val)` | Assign item | `obj[key]=val`    |
| `__delitem__(self, key)`      | Delete item | `del obj[key]`    |
| `__iter__(self)`              | Iterator    | `for x in obj`    |
| `__next__(self)`              | Next item   | `next(iter(obj))` |
| `__contains__(self, item)`    | Membership  | `x in obj`        |

---

## 4. Numeric Operations

| Method         | Operator   | Example        |
| -------------- | ---------- | -------------- |
| `__add__`      | `+`        | `a + b`        |
| `__sub__`      | `-`        | `a - b`        |
| `__mul__`      | `*`        | `a * b`        |
| `__truediv__`  | `/`        | `a / b`        |
| `__floordiv__` | `//`       | `a // b`       |
| `__mod__`      | `%`        | `a % b`        |
| `__pow__`      | `**`       | `a ** b`       |
| `__neg__`      | Unary `-`  | `-a`           |
| `__abs__`      | `abs(a)`   | Absolute value |
| `__round__`    | `round(a)` | Rounding       |

➡️ Right-hand versions: `__radd__`, `__rsub__`, etc.
➡️ In-place versions: `__iadd__`, `__imul__`, etc.

---

## 5. Comparisons & Truthiness

| Method     | Operator    | Example                |
| ---------- | ----------- | ---------------------- |
| `__eq__`   | `==`        |                        |
| `__ne__`   | `!=`        |                        |
| `__lt__`   | `<`         |                        |
| `__le__`   | `<=`        |                        |
| `__gt__`   | `>`         |                        |
| `__ge__`   | `>=`        |                        |
| `__bool__` | `bool(obj)` | Default: `__len__ > 0` |

---

## 6. Context Managers

```python
class MyCtx:
    def __enter__(self): print("Enter"); return self
    def __exit__(self, exc_type, exc_val, exc_tb): print("Exit")

with MyCtx():  # triggers __enter__ / __exit__
    print("inside")
```

---

## 7. Callable & Functional Behavior

| Method                      | Purpose                              | Example        |
| --------------------------- | ------------------------------------ | -------------- |
| `__call__(self, …)`         | Make object callable                 | `obj()`        |
| `__hash__(self)`            | Hashable → usable as dict key        | `hash(obj)`    |
| `__copy__` / `__deepcopy__` | Control `copy.copy`, `copy.deepcopy` | Custom cloning |

---

## 8. Class Behavior

| Method              | Purpose                  |
| ------------------- | ------------------------ |
| `__class__`         | Instance’s class         |
| `__mro__`           | Method resolution order  |
| `__subclasses__()`  | Get subclasses           |
| `__instancecheck__` | Customize `isinstance()` |
| `__subclasscheck__` | Customize `issubclass()` |

---

## 9. File-Like Interfaces

| Method                   | Example             |
| ------------------------ | ------------------- |
| `__enter__` / `__exit__` | File context        |
| `__iter__`               | File iteration      |
| `__next__`               | Read line iteration |

---

## 10. Beginner Pitfalls

* ❌ Overriding `__getattribute__` without care → infinite recursion.
* ❌ Forgetting to return `NotImplemented` in comparison/numeric dunders.
* ❌ Misusing `__del__` → not guaranteed when program exits.
* ❌ Over-engineering → only implement methods that match your use case.

---

✅ With this, you have the **full dunder/magic methods reference**: construction, attributes, containers, math, comparisons, context managers, and callable behavior.

---

