

# 📘 Python Dictionary Cheat Sheet

**Key-Value Mapping Type**

---

## 1. Creating Dictionaries

```python
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)             # keyword args
d = dict([("a",1),("b",2)])    # from list of tuples
d = {}                         # empty dict
```

---

## 2. Dictionary Methods (All)

| Method         | Example                      | Result                        |
| -------------- | ---------------------------- | ----------------------------- |
| `clear()`      | `d.clear()`                  | Remove all items.             |
| `copy()`       | `d.copy()`                   | Shallow copy.                 |
| `fromkeys()`   | `dict.fromkeys(["a","b"],0)` | `{"a":0,"b":0}`               |
| `get()`        | `d.get("a",0)`               | Value or default.             |
| `items()`      | `d.items()`                  | Pairs view.                   |
| `keys()`       | `d.keys()`                   | Keys view.                    |
| `values()`     | `d.values()`                 | Values view.                  |
| `pop()`        | `d.pop("a")`                 | Remove & return value.        |
| `popitem()`    | `d.popitem()`                | Remove last pair.             |
| `setdefault()` | `d.setdefault("c",0)`        | Get value, insert if missing. |
| `update()`     | `d.update({"c":3})`          | Merge dicts.                  |

---

## 3. Accessing Data

| Command       | Example                 | Result      |
| ------------- | ----------------------- | ----------- |
| Indexing      | `d["a"]`                | `1`         |
| Safe access   | `d.get("x", "missing")` | `"missing"` |
| Membership    | `"a" in d`              | `True`      |
| Missing check | `"z" not in d`          | `True`      |

---

## 4. Iterating

```python
for k in d:            # keys
    print(k)

for v in d.values():   # values
    print(v)

for k,v in d.items():  # key-value
    print(k, v)
```

---

## 5. Dictionary Comprehensions

```python
squares = {x: x*x for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}
```

With condition:

```python
even = {x: x*x for x in range(5) if x%2==0}
# {0:0, 2:4, 4:16}
```

---

## 6. Built-in Functions

| Function          | Example                 | Result              |
| ----------------- | ----------------------- | ------------------- |
| `len(d)`          | `len({"a":1,"b":2})`    | `2`                 |
| `sorted(d)`       | `sorted({"b":2,"a":1})` | `["a","b"]`         |
| `max(d)`          | `max({"a":1,"b":2})`    | `"b"` (key compare) |
| `min(d)`          | `min(d)`                | `"a"`               |
| `sum(d.values())` | `sum(d.values())`       | Sum of values.      |

---

## 7. Merging Dictionaries (Python ≥ 3.9)

```python
d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}
merged = d1 | d2         # {"a":1, "b":3, "c":4}
d1 |= d2                 # in-place update
```

---

## 8. Nested Dictionaries

```python
users = {
  "alice": {"age":25, "city":"NY"},
  "bob": {"age":30, "city":"LA"}
}
print(users["alice"]["city"])   # NY
```

---

## 9. Beginner Pitfalls

* ❌ Keys must be **hashable** (e.g. lists not allowed).
* ❌ `d["missing"]` raises `KeyError` → use `get()`.
* ❌ `dict.copy()` is shallow → nested dicts still reference same objects.
* ⚠️ `popitem()` removes **last item** (since Python 3.7).

---

✅ Python `dict` has **11 methods** plus powerful comprehension and merging features.
It’s the **most common data structure** for fast key-value lookups.

---
