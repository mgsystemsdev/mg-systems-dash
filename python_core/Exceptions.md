
# 📘 Python Exceptions Cheat Sheet

**Error Handling & Defensive Programming**

---

## 1. Basic Try/Except

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

* Catch specific errors when possible.
* Avoid bare `except:` unless truly necessary.

---

## 2. Multiple Excepts

```python
try:
    val = int("abc")
except ValueError:
    print("Bad value")
except TypeError:
    print("Wrong type")
```

---

## 3. Catching Multiple in One Block

```python
try:
    int("abc")
except (ValueError, TypeError) as e:
    print("Error:", e)
```

---

## 4. `else` and `finally`

```python
try:
    n = int("42")
except ValueError:
    print("Conversion failed")
else:
    print("Success:", n)     # runs if no exception
finally:
    print("Always runs")     # cleanup code
```

---

## 5. Raising Exceptions

| Command        | Example                                     | Explanation       |
| -------------- | ------------------------------------------- | ----------------- |
| Raise generic  | `raise Exception("error")`                  | Throw error.      |
| Raise specific | `raise ValueError("bad value")`             | Better debugging. |
| Re-raise       | `python\ntry:\n    1/0\nexcept:\n    raise` | Propagate error.  |

---

## 6. Custom Exceptions

```python
class MyError(Exception):
    pass

raise MyError("Something went wrong")
```

* Inherit from `Exception`.
* Allows domain-specific errors.

---

## 7. Assertions

```python
assert x > 0, "x must be positive"
```

* Quick checks → raises `AssertionError` if False.
* ⚠️ Assertions can be disabled with `python -O`.

---

## 8. Common Built-in Exceptions

| Exception                             | Raised when…                        |
| ------------------------------------- | ----------------------------------- |
| `ValueError`                          | Wrong type of value (`int("abc")`). |
| `TypeError`                           | Wrong type (`"a"+1`).               |
| `NameError`                           | Variable not defined.               |
| `IndexError`                          | List index out of range.            |
| `KeyError`                            | Dict key missing.                   |
| `ZeroDivisionError`                   | Divide by 0.                        |
| `FileNotFoundError`                   | File path invalid.                  |
| `ImportError` / `ModuleNotFoundError` | Module missing.                     |
| `AttributeError`                      | Attribute doesn’t exist.            |
| `RuntimeError`                        | Generic runtime problem.            |
| `AssertionError`                      | From failed `assert`.               |

---

## 9. Best Practices

* ✅ Catch **specific exceptions**, not all.
* ✅ Use `finally` for cleanup (files, network, DB).
* ✅ Raise custom exceptions for domain errors.
* ✅ Log errors before swallowing them.
* ❌ Don’t use exceptions for normal flow control.
* ❌ Avoid `except Exception:` unless debugging.

---

✅ With this, you now have the **complete exceptions reference**: try/except/else/finally, raising, custom exceptions, and pitfalls.
