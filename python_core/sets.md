

# 📘 Python Set Cheat Sheet

**Unordered Collection of Unique Elements**

---

## 1. Creating Sets

```python
s = {1, 2, 3}
s = set([1,2,2,3])   # duplicates removed → {1,2,3}
empty = set()        # empty set (not {})
```

⚠️ `{}` creates an empty **dict**, not a set.

---

## 2. Adding & Removing Elements

| Method         | Example           | Result                               |
| -------------- | ----------------- | ------------------------------------ |
| `add(x)`       | `s.add(4)`        | `{1,2,3,4}`                          |
| `update(iter)` | `s.update([4,5])` | `{1,2,3,4,5}`                        |
| `remove(x)`    | `s.remove(2)`     | Remove item; error if missing.       |
| `discard(x)`   | `s.discard(2)`    | Remove item; no error if missing.    |
| `pop()`        | `s.pop()`         | Removes & returns arbitrary element. |
| `clear()`      | `s.clear()`       | `set()` (empty set).                 |

---

## 3. Set Operations

| Operation            | Example                                    | Result                           |               |
| -------------------- | ------------------------------------------ | -------------------------------- | ------------- |
| Union                | \`s1                                       | s2`or`s1.union(s2)\`             | All elements. |
| Intersection         | `s1 & s2` or `s1.intersection(s2)`         | Common elements.                 |               |
| Difference           | `s1 - s2` or `s1.difference(s2)`           | Elements in `s1` not in `s2`.    |               |
| Symmetric Difference | `s1 ^ s2` or `s1.symmetric_difference(s2)` | Elements in either but not both. |               |
| Subset               | `s1 <= s2` or `s1.issubset(s2)`            | True if `s1` inside `s2`.        |               |
| Superset             | `s1 >= s2` or `s1.issuperset(s2)`          | True if `s1` contains `s2`.      |               |
| Disjoint             | `s1.isdisjoint(s2)`                        | True if no overlap.              |               |

---

## 4. Copying

| Method       | Example         | Explanation       |
| ------------ | --------------- | ----------------- |
| Shallow copy | `s2 = s.copy()` | Independent copy. |

---

## 5. Built-in Functions with Sets

| Function   | Example        | Result                |
| ---------- | -------------- | --------------------- |
| `len()`    | `len(s)`       | Size of set.          |
| `max()`    | `max(s)`       | Largest element.      |
| `min()`    | `min(s)`       | Smallest element.     |
| `sum()`    | `sum({1,2,3})` | `6`                   |
| `any()`    | `any({0,1,0})` | `True`                |
| `all()`    | `all({1,2,3})` | `True`                |
| `sorted()` | `sorted(s)`    | Sorted list from set. |

---

## 6. Frozenset (Immutable Set)

```python
fs = frozenset([1,2,3])
# Same operations as sets, but cannot add/remove.
```

---

## 7. Beginner Pitfalls

* ❌ `{}` makes an **empty dict**, not a set → use `set()`.
* ❌ Sets are unordered — indexing like `s[0]` is invalid.
* ❌ Duplicates are automatically removed (`{1,1,2}` → `{1,2}`).
* ❌ `remove()` throws error if element missing → use `discard()`.

---

✅ With this, you now have the **full set methods + operations** cheat sheet.
