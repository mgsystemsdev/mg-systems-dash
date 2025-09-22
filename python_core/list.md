

# 📘 Python List Methods Cheat Sheet

**All Built-in `list` Methods**

---

## 1. Creating Lists

```python
lst = [1, 2, 3]
lst = list((1, 2, 3))  # from tuple
```

---

## 2. Adding Elements

| Method         | Example             | Result        |
| -------------- | ------------------- | ------------- |
| `append(x)`    | `lst.append(4)`     | `[1,2,3,4]`   |
| `insert(i, x)` | `lst.insert(1,"a")` | `[1,"a",2,3]` |
| `extend(iter)` | `lst.extend([4,5])` | `[1,2,3,4,5]` |
| `+` operator   | `lst + [4,5]`       | `[1,2,3,4,5]` |

---

## 3. Removing Elements

| Method      | Example         | Result                      |
| ----------- | --------------- | --------------------------- |
| `remove(x)` | `lst.remove(2)` | Removes first `2`.          |
| `pop(i)`    | `lst.pop(1)`    | Returns & removes at index. |
| `pop()`     | `lst.pop()`     | Removes last.               |
| `clear()`   | `lst.clear()`   | `[]` (empty list).          |

---

## 4. Searching & Counting

| Method     | Example        | Result             |
| ---------- | -------------- | ------------------ |
| `index(x)` | `lst.index(3)` | Returns position.  |
| `count(x)` | `lst.count(2)` | Count occurrences. |
| Membership | `2 in lst`     | Boolean check.     |

---

## 5. Sorting & Reversing

| Method               | Example                  | Result                   |
| -------------------- | ------------------------ | ------------------------ |
| `sort()`             | `lst.sort()`             | Sort ascending.          |
| `sort(reverse=True)` | `lst.sort(reverse=True)` | Descending.              |
| `sort(key=len)`      | `lst.sort(key=len)`      | Sort by function.        |
| `reverse()`          | `lst.reverse()`          | Reverse in place.        |
| `sorted(lst)`        | `sorted(lst)`            | Returns new sorted list. |

---

## 6. Copying

| Method      | Example              | Result        |
| ----------- | -------------------- | ------------- |
| `copy()`    | `lst2 = lst.copy()`  | Shallow copy. |
| Slicing     | `lst2 = lst[:]`      | Shallow copy. |
| `list(lst)` | Convert to new list. |               |

---

## 7. Iteration & Comprehensions

| Syntax      | Example                       | Result              |
| ----------- | ----------------------------- | ------------------- |
| For loop    | `[x*2 for x in lst]`          | List comprehension. |
| Conditional | `[x for x in lst if x>0]`     | Filter.             |
| Nested      | `[x+y for x in a for y in b]` | Nested loops.       |

---

## 8. Utilities

| Method     | Example        | Result |
| ---------- | -------------- | ------ |
| `len(lst)` | `len([1,2,3])` | `3`    |
| `max(lst)` | `max([1,2,3])` | `3`    |
| `min(lst)` | `min([1,2,3])` | `1`    |
| `sum(lst)` | `sum([1,2,3])` | `6`    |
| `any(lst)` | `any([0,1,0])` | `True` |
| `all(lst)` | `all([1,2,3])` | `True` |

---

## 9. Packing & Unpacking

```python
a, b, *rest = [1, 2, 3, 4]
# a=1, b=2, rest=[3,4]
```

---

## ✅ Final Count

Python `list` has **11 built-in methods** (append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort).
Other functions (`len`, `max`, `min`, etc.) are **built-ins**, not methods — but commonly used with lists.

---

