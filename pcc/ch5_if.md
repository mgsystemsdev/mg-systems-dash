

# 📘 Python Crash Course – Chapter 5

**if Statements Cheat Sheet**

---

## 1. Basic if Statements

| Command / Concept | Syntax                    | Explanation                        | Example                                                                                      | Notes / Gotchas               | Beginner Pitfalls              |
| ----------------- | ------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------ |
| Simple if         | `if condition:`           | Runs block if condition is `True`. | `python\nif age >= 18:\n    print("Adult")\n`                                                | Indentation is required.      | Forgetting colon `:`.          |
| if-else           | `if condition: ... else:` | Choose between two blocks.         | `python\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")\n`                     | Both blocks must be indented. | Misaligning indentation.       |
| if-elif-else      | `if ... elif ... else:`   | Chains multiple conditions.        | `python\nif age < 4:\n    price = 0\nelif age < 18:\n    price = 5\nelse:\n    price = 10\n` | Runs first true branch only.  | Expecting all branches to run. |

---

## 2. Conditional Tests

| Command / Concept | Syntax               | Explanation            | Example         | Notes / Gotchas          | Beginner Pitfalls            |
| ----------------- | -------------------- | ---------------------- | --------------- | ------------------------ | ---------------------------- |
| Equality          | `==`                 | True if values match.  | `car == "bmw"`  | Case-sensitive.          | `"BMW" == "bmw"` → False.    |
| Inequality        | `!=`                 | True if values differ. | `car != "audi"` | —                        | Confusing `=` with `==`.     |
| Greater / Less    | `>`, `<`, `>=`, `<=` | Numeric comparisons.   | `age >= 18`     | Works with numbers only. | Using on incompatible types. |

---

## 3. Logical Operators

| Command / Concept | Syntax            | Explanation                   | Example                 | Notes / Gotchas                   | Beginner Pitfalls                   |   |                     |
| ----------------- | ----------------- | ----------------------------- | ----------------------- | --------------------------------- | ----------------------------------- | - | ------------------- |
| and               | `cond1 and cond2` | True if both are True.        | `age > 18 and age < 65` | Short-circuits if first is False. | Using `&` instead of `and`.         |   |                     |
| or                | `cond1 or cond2`  | True if at least one is True. | `age < 18 or age > 65`  | Short-circuits if first is True.  | Using \`                            |   | \` (not in Python). |
| not               | `not cond`        | Negates condition.            | `not banned`            | —                                 | Forgetting parentheses when needed. |   |                     |

---

## 4. Membership Tests

| Command / Concept | Syntax             | Explanation            | Example             | Notes / Gotchas                   | Beginner Pitfalls              |
| ----------------- | ------------------ | ---------------------- | ------------------- | --------------------------------- | ------------------------------ |
| In                | `item in list`     | Checks if item exists. | `"bmw" in cars`     | Works for lists, strings, tuples. | Forgetting quotes for strings. |
| Not in            | `item not in list` | Checks if item absent. | `"kia" not in cars` | —                                 | Reversing logic accidentally.  |

---

## 5. Boolean Values

| Command / Concept | Syntax          | Explanation                     | Example              | Notes / Gotchas      | Beginner Pitfalls               |
| ----------------- | --------------- | ------------------------------- | -------------------- | -------------------- | ------------------------------- |
| True / False      | `True`, `False` | Python’s two boolean constants. | `game_active = True` | Must be capitalized. | Using lowercase `true` → error. |

---

## 6. Best Practices

* ✅ Keep conditions simple and readable.
* ✅ Use **`in` / `not in`** for membership checks instead of long `and` chains.
* ⚠️ Remember: Python comparisons are **case-sensitive**.
* ⚠️ Don’t confuse **assignment (`=`)** with **equality (`==`)**.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 5**.

