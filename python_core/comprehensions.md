

# 📘 Python Comprehensions Cheat Sheet

**Compact ways to create sequences & collections**

---

## 1. List Comprehensions

**Basic form:**

```python
[new_item for item in iterable if condition]
```

| Example                            | Result          |
| ---------------------------------- | --------------- |
| `[x**2 for x in range(5)]`         | `[0,1,4,9,16]`  |
| `[x for x in range(10) if x%2==0]` | `[0,2,4,6,8]`   |
| `[c.upper() for c in "abc"]`       | `['A','B','C']` |

---

## 2. Set Comprehensions

```python
{s for s in "abracadabra" if s not in "abc"}
# {'r','d'}
```

* Works same as list comprehension, but produces a **set (unique, unordered)**.

---

## 3. Dict Comprehensions

```python
{x: x**2 for x in range(3)}
# {0:0, 1:1, 2:4}
```

With conditions:

```python
{x: x for x in range(5) if x%2==0}
# {0:0, 2:2, 4:4}
```

---

## 4. Generator Expressions

* Like list comprehensions but with **()`instead of`\[]\`**.
* Lazily evaluated (saves memory).

```python
gen = (x**2 for x in range(5))
next(gen)  # 0
next(gen)  # 1
```

---

## 5. Nested Comprehensions

| Example                                       | Result                      |
| --------------------------------------------- | --------------------------- |
| `[[i*j for j in range(3)] for i in range(3)]` | `[[0,0,0],[0,1,2],[0,2,4]]` |
| `[c for word in ["hi","bye"] for c in word]`  | `['h','i','b','y','e']`     |

---

## 6. With Functions

```python
[len(word) for word in ["apple","banana"]]
# [5,6]

{word: len(word) for word in ["apple","banana"]}
# {'apple':5, 'banana':6}
```

---

## 7. Best Practices

* ✅ Use comprehensions for **clarity + brevity**.
* ✅ Use generator expressions when working with huge datasets.
* ❌ Don’t over-nest comprehensions → hurts readability. Prefer loops if it gets complex.

---

## ✅ Summary

* **List** → `[expr for x in iterable if cond]`
* **Set** → `{expr for x in iterable if cond}`
* **Dict** → `{k:v for (k,v) in iterable if cond}`
* **Generator** → `(expr for x in iterable if cond)`

