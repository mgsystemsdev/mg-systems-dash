


# 📘 Python Iterators & Generators Cheat Sheet

**Lazy Evaluation & Custom Iteration**

---

## 1. Iterables vs Iterators

| Concept       | Example                    | Notes                 |
| ------------- | -------------------------- | --------------------- |
| Iterable      | `for x in [1,2,3]: ...`    | Has `__iter__()`.     |
| Iterator      | `it = iter([1,2,3])`       | Has `__next__()`.     |
| Next item     | `next(it)`                 | Returns next element. |
| StopIteration | Raised when no more items. |                       |

---

## 2. Built-in Iterator Tools

| Function      | Example                     | Result            |
| ------------- | --------------------------- | ----------------- |
| `iter()`      | `it = iter([1,2])`          | Create iterator.  |
| `next()`      | `next(it)`                  | Get next element. |
| `enumerate()` | `for i,v in enumerate(lst)` | Index + value.    |
| `zip()`       | `for a,b in zip(lst1,lst2)` | Pair elements.    |
| `reversed()`  | `for x in reversed(lst)`    | Iterate backward. |
| `sorted()`    | `for x in sorted(set)`      | Sorted iteration. |

---

## 3. Creating Custom Iterators

```python
class CountDown:
    def __init__(self,n): self.n=n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n+1
```

```python
for x in CountDown(3): print(x)  
# 3,2,1
```

---

## 4. Generators (with `yield`)

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3): print(x)
```

* Lazily produces values one by one.
* Uses **`yield`** instead of `return`.
* Keeps state between calls.

---

## 5. Generator Expressions

```python
squares = (x**2 for x in range(5))
next(squares)  # 0
```

* Similar to list comprehension but with `()` → memory efficient.

---

## 6. Generator Utilities

| Function  | Example              | Explanation                   |
| --------- | -------------------- | ----------------------------- |
| `send()`  | `g.send(val)`        | Send value into generator.    |
| `throw()` | `g.throw(Exception)` | Raise error inside generator. |
| `close()` | `g.close()`          | Stop generator.               |

---

## 7. Itertools (Standard Library)

```python
import itertools as it
```

| Tool                        | Example                | Use                   |
| --------------------------- | ---------------------- | --------------------- |
| `it.count(10,2)`            | 10,12,14…              | Infinite counter.     |
| `it.cycle("AB")`            | A,B,A,B…               | Infinite cycle.       |
| `it.repeat(5,3)`            | 5,5,5                  | Repeat N times.       |
| `it.accumulate([1,2,3])`    | 1,3,6                  | Running totals.       |
| `it.chain(a,b)`             | Concatenate iterables. |                       |
| `it.combinations("ABCD",2)` | AB, AC, AD…            | Choose pairs.         |
| `it.permutations("ABC",2)`  | AB, AC, BA, BC…        | Ordered arrangements. |
| `it.product([1,2],[3,4])`   | Cartesian product.     |                       |

---

## 8. Best Practices

* ✅ Use **generators** for large datasets → save memory.
* ✅ Prefer `yield` for streaming data.
* ✅ Use `itertools` for complex iteration patterns.
* ❌ Don’t overuse custom iterators — most cases solved by generators.

---

✅ With this, you have the **full Iterators & Generators toolkit**: from built-in iteration, to custom iterators, to generators and `itertools`.

