

# 📘 Python `if` Statement Cheat Sheet

**Conditionals & Flow Control**

---

## 1. Basic `if`

```python
if condition:
    # code runs if condition is True
```

Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## 2. `if-else`

```python
if condition:
    # runs if True
else:
    # runs if False
```

Example:

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 3. `if-elif-else`

```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```

Example:

```python
if x > 10:
    print("Big")
elif x == 10:
    print("Equal")
else:
    print("Small")
```

---

## 4. Nested `if`

```python
if x > 0:
    if x < 10:
        print("Between 1 and 9")
```

---

## 5. One-liners

| Syntax       | Example                                  |
| ------------ | ---------------------------------------- |
| Inline `if`  | `print("Yes") if x > 5 else print("No")` |
| Simple check | `if x: print("Not zero")`                |

---

## 6. Boolean Logic in Conditions

| Operator    | Example               | Explanation        |
| ----------- | --------------------- | ------------------ |
| `and`       | `if a > 0 and b > 0:` | Both must be true. |
| `or`        | `if a > 0 or b > 0:`  | At least one true. |
| `not`       | `if not done:`        | Negates condition. |
| `in`        | `if "a" in word:`     | Membership test.   |
| Comparisons | `if 0 < x < 10:`      | Chain comparisons. |

---

## 7. Truthy & Falsy

Falsy values in Python:

* `False`
* `None`
* `0`, `0.0`, `0j`
* `""` (empty string)
* `[]`, `{}`, `set()`, `range(0)` (empty collections)

Example:

```python
if []:
    print("Not empty")   # won’t run
```

---

## 8. Beginner Pitfalls

* ❌ Using `=` instead of `==` (`if x = 5:` → error).
* ❌ Forgetting indentation → `IndentationError`.
* ❌ Over-nesting; prefer `elif` to deep nesting.
* ❌ Relying on `== True` (unnecessary: `if cond:` is enough).

---

✅ With this, you have the **complete `if` reference**: basic, elif, nesting, one-liners, boolean logic, truthy/falsy rules, and pitfalls.

