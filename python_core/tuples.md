

# 📘 Python Tuple Cheat Sheet

**Immutable Sequences**

---

## 1. Creating Tuples

```python
t = (1, 2, 3)          # regular tuple
t = (1,)               # single-element tuple (note the comma!)
t = tuple([1,2,3])     # from list
```

---

## 2. Properties

* ✅ Ordered
* ✅ Immutable (cannot modify in place)
* ✅ Can store mixed types
* ✅ Supports nesting (`t = (1, (2, 3), 4)`)

---

## 3. Accessing Data

| Command        | Example  | Result       |
| -------------- | -------- | ------------ |
| Indexing       | `t[0]`   | `1`          |
| Negative index | `t[-1]`  | Last element |
| Slicing        | `t[1:3]` | Sub-tuple    |

---

## 4. Tuple Methods (only 2!)

| Method     | Example              | Result |
| ---------- | -------------------- | ------ |
| `count(x)` | `(1,2,2,3).count(2)` | `2`    |
| `index(x)` | `(1,2,3).index(2)`   | `1`    |

---

## 5. Built-in Functions (work with tuples)

| Function   | Example           | Result    |
| ---------- | ----------------- | --------- |
| `len()`    | `len(t)`          | Length    |
| `max()`    | `max((1,2,3))`    | `3`       |
| `min()`    | `min((1,2,3))`    | `1`       |
| `sum()`    | `sum((1,2,3))`    | `6`       |
| `any()`    | `any((0,1,0))`    | `True`    |
| `all()`    | `all((1,2,3))`    | `True`    |
| `sorted()` | `sorted((3,1,2))` | `[1,2,3]` |

---

## 6. Operations

| Operation   | Example         | Result          |
| ----------- | --------------- | --------------- |
| Concatenate | `(1,2) + (3,4)` | `(1,2,3,4)`     |
| Repeat      | `(1,2) * 3`     | `(1,2,1,2,1,2)` |
| Membership  | `3 in (1,2,3)`  | `True`          |

---

## 7. Tuple Packing & Unpacking

```python
# Packing
t = 1, 2, 3  

# Unpacking
a, b, c = t    # a=1, b=2, c=3

# Extended unpacking
a, *rest = (1,2,3,4)   # a=1, rest=[2,3,4]
```

---

## 8. Named Tuples (advanced)

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
p = Point(10, 20)

print(p.x, p.y)   # 10 20
```

---

## 9. Beginner Pitfalls

* ❌ Forgetting comma for single-element tuple → `(5)` is `int`, `(5,)` is `tuple`.
* ❌ Trying to modify tuple items (`t[0] = 10` → `TypeError`).
* ❌ Confusing immutability: tuple can hold **mutable elements** (`([1,2],3)` allows modifying the list inside).

---

✅ Tuples are **lightweight, immutable lists**. Use them for fixed collections, dictionary keys, or when you need sequence safety.

---

