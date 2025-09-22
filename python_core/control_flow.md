
# 📘 Python Control Flow Cheat Sheet

**Conditionals, Loops, and Flow Modifiers**

---

## 1. Conditionals (`if` statements)

```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

| Form           | Example                                       |
| -------------- | --------------------------------------------- |
| Basic `if`     | `if x > 0: print("Positive")`                 |
| `if-else`      | `if x%2==0: print("Even") else: print("Odd")` |
| `if-elif-else` | Multi-branch decision.                        |
| One-liner      | `print("Yes") if flag else print("No")`       |

---

## 2. Boolean Logic

| Operator | Example               | Explanation                 |
| -------- | --------------------- | --------------------------- |
| `and`    | `if a > 0 and b > 0:` | Both must be True.          |
| `or`     | `if a > 0 or b > 0:`  | At least one True.          |
| `not`    | `if not done:`        | Negates condition.          |
| `in`     | `if "a" in word:`     | Membership test.            |
| Chained  | `if 0 < x < 10:`      | More readable range checks. |

---

## 3. Loops (`for`, `while`)

### For loop

```python
for item in iterable:
    print(item)
```

* Works with lists, tuples, dicts, sets, strings.
* Often used with `range()`.

### While loop

```python
while condition:
    ...
```

* Runs until condition is False.

---

## 4. Loop Modifiers

| Keyword          | Example                                                             | Effect                      |
| ---------------- | ------------------------------------------------------------------- | --------------------------- |
| `break`          | `if x==5: break`                                                    | Exit loop immediately.      |
| `continue`       | `if x%2==0: continue`                                               | Skip to next iteration.     |
| `pass`           | `if cond: pass`                                                     | Do nothing (placeholder).   |
| `else` with loop | `python\nfor x in [1,2,3]:\n    ...\nelse:\n    print("No break!")` | Runs if loop wasn’t broken. |

---

## 5. Useful Functions in Loops

| Function      | Example                       | Explanation         |
| ------------- | ----------------------------- | ------------------- |
| `range()`     | `for i in range(5)`           | 0 → 4 loop.         |
| `enumerate()` | `for i,val in enumerate(lst)` | Index + value.      |
| `zip()`       | `for a,b in zip(lst1,lst2)`   | Iterate pairs.      |
| `reversed()`  | `for x in reversed(lst)`      | Backwards loop.     |
| `sorted()`    | `for x in sorted(set)`        | Iteration in order. |

---

## 6. Pattern Matching (Python ≥3.10)

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case _:
        print("Unknown")
```

* Similar to `switch` in other languages.
* Can match constants, variables, types, and structures.

---

## 7. Beginner Pitfalls

* ❌ Using `=` instead of `==` in conditions.
* ❌ Forgetting indentation → `IndentationError`.
* ❌ Infinite loops with `while True` and no break.
* ❌ Over-nesting (`if` inside `if` inside loops). Prefer `elif`.
* ❌ Confusing `pass` (placeholder) with `continue` (skip iteration).

---

✅ With this, you have the **complete control flow reference**: conditionals, loops, modifiers, pattern matching, and best practices.

Would you like me to now create the **Exceptions cheat sheet** (all `try`, `except`, `finally`, `raise`, `assert`) — since that’s the next big piece of control flow in Python?
