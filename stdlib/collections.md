

# 📘 Python Collections Cheat Sheet

**Efficient Data Structures for Everyday Use**

---

## 1. Counter

Count hashable objects quickly.

```python
from collections import Counter

c = Counter("abracadabra")
print(c)        # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

| Method             | Example              | Result                              |
| ------------------ | -------------------- | ----------------------------------- |
| `c.most_common(n)` | `c.most_common(2)`   | `[('a', 5), ('b', 2)]`              |
| `c.elements()`     | `list(c.elements())` | `['a','a','a','a','a','b','b',...]` |
| `c.update("aaa")`  |                      | Adds counts                         |
| `c.subtract("ab")` |                      | Subtract counts                     |
| Arithmetic         | `c1 + c2`, `c1 - c2` | Combine or subtract counts          |

✅ Best for: word counts, frequency analysis.

---

## 2. defaultdict

Dictionary with automatic default values.

```python
from collections import defaultdict

dd = defaultdict(int)   # default value 0
dd["x"] += 1            # no KeyError → 1
```

| Factory | Example             | Default |
| ------- | ------------------- | ------- |
| `int`   | `defaultdict(int)`  | 0       |
| `list`  | `defaultdict(list)` | `[]`    |
| `set`   | `defaultdict(set)`  | `set()` |

```python
groups = defaultdict(list)
groups["fruit"].append("apple")
print(groups)   # {'fruit': ['apple']}
```

✅ Best for: grouping, counting, adjacency lists.

---

## 3. deque (Double-Ended Queue)

Fast appends and pops from both ends.

```python
from collections import deque

dq = deque([1,2,3])
dq.append(4)      # [1,2,3,4]
dq.appendleft(0)  # [0,1,2,3,4]
dq.pop()          # → 4
dq.popleft()      # → 0
```

| Method             | Example                 | Result                       |
| ------------------ | ----------------------- | ---------------------------- |
| `append(x)`        | Add right               |                              |
| `appendleft(x)`    | Add left                |                              |
| `pop()`            | Remove right            |                              |
| `popleft()`        | Remove left             |                              |
| `extend(iter)`     | `dq.extend([4,5])`      | Add multiple right           |
| `extendleft(iter)` | `dq.extendleft([0,-1])` | Add multiple left (reversed) |
| `rotate(n)`        | `dq.rotate(1)`          | Rotate right by 1            |
| `maxlen`           | `dq = deque(maxlen=3)`  | Fixed-size queue             |

✅ Best for: queues, stacks, sliding windows.

---

## 4. Beginner Pitfalls

* ❌ Using a normal `dict` when you need `defaultdict` → messy `if key not in dict` checks.
* ❌ Forgetting `deque.extendleft()` reverses input order.
* ❌ Using `Counter` for sorted results — you must call `.most_common()`.

---

✅ With this, you have the **collections essentials**:

* **Counter** → counting & frequencies
* **defaultdict** → grouping & safe defaults
* **deque** → fast, flexible queues

---
