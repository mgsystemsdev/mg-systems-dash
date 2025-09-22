
# 📘 Python `itertools` Cheat Sheet

**Efficient Iteration Utilities**

```python
import itertools as it
```

---

## 1. Infinite Iterators

| Function                    | Example          | Output     |
| --------------------------- | ---------------- | ---------- |
| `it.count(start=0, step=1)` | `it.count(10,2)` | 10,12,14,… |
| `it.cycle(iterable)`        | `it.cycle("AB")` | A,B,A,B,…  |
| `it.repeat(elem, n)`        | `it.repeat(5,3)` | 5,5,5      |

---

## 2. Iterators Terminating on Shortest Input

| Function                             | Example                                  | Result                  |
| ------------------------------------ | ---------------------------------------- | ----------------------- |
| `it.accumulate(iter, func)`          | `it.accumulate([1,2,3])`                 | 1,3,6                   |
|                                      | `it.accumulate([1,2,3], func=mul)`       | 1,2,6 (running product) |
| `it.chain(*iterables)`               | `it.chain("ABC","DEF")`                  | A,B,C,D,E,F             |
| `it.chain.from_iterable(list)`       | `it.chain.from_iterable([[1,2],[3]])`    | 1,2,3                   |
| `it.compress(data, selectors)`       | `it.compress("ABC",[1,0,1])`             | A,C                     |
| `it.dropwhile(pred, iter)`           | `it.dropwhile(lambda x:x<3,[1,2,3,4])`   | 3,4                     |
| `it.takewhile(pred, iter)`           | `it.takewhile(lambda x:x<3,[1,2,3,4])`   | 1,2                     |
| `it.filterfalse(pred, iter)`         | `it.filterfalse(lambda x:x%2,[1,2,3,4])` | 2,4                     |
| `it.islice(iter, start, stop, step)` | `it.islice("ABCDEFG",2,5)`               | C,D,E                   |
| `it.starmap(func, iter)`             | `it.starmap(pow,[(2,5),(3,2)])`          | 32,9                    |
| `it.tee(iter, n=2)`                  | `a,b = it.tee([1,2,3])`                  | Independent copies      |
| `it.zip_longest(a,b,fillvalue)`      | `it.zip_longest("AB","12X")`             | (A,1),(B,2),(None,X)    |

---

## 3. Combinatoric Iterators

| Function                                    | Example                                    | Result            |
| ------------------------------------------- | ------------------------------------------ | ----------------- |
| `it.product(iter, repeat=n)`                | `it.product("AB", repeat=2)`               | AA,AB,BA,BB       |
| `it.permutations(iter, r)`                  | `it.permutations("ABC",2)`                 | AB,AC,BA,BC,CA,CB |
| `it.combinations(iter, r)`                  | `it.combinations("ABC",2)`                 | AB,AC,BC          |
| `it.combinations_with_replacement(iter, r)` | `it.combinations_with_replacement("AB",2)` | AA,AB,BB          |

---

## 4. Common Use Cases

```python
from itertools import product, permutations, combinations, accumulate, groupby

# Cartesian product
list(product([1,2],[3,4]))   # [(1,3),(1,4),(2,3),(2,4)]

# All permutations
list(permutations([1,2,3],2))   # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# Combinations
list(combinations("ABC",2))     # [('A','B'),('A','C'),('B','C')]

# Accumulation
list(accumulate([1,2,3,4]))     # [1,3,6,10]

# Grouping
data = [("even",2),("odd",1),("even",4)]
for k,g in groupby(sorted(data),key=lambda x:x[0]):
    print(k,list(g))
# even [(even,2),(even,4)]
# odd [(odd,1)]
```

---

## 5. Beginner Pitfalls

* ❌ Using `itertools` functions without wrapping with `list()` or `for` → results are iterators, not stored lists.
* ❌ Forgetting `itertools` is **lazy** → won’t compute until consumed.
* ❌ Using `tee()` heavily on huge iterators → duplicates in memory.

---

✅ With this, you now have the **complete `itertools` reference**: infinite iterators, filters, combinatorics, accumulation, and grouping.

