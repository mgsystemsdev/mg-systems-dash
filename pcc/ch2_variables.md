
# 📘 Python Crash Course – Chapter 2

**Variables and Simple Data Types Cheat Sheet**

---

## 1. Variables

| Command / Concept    | Syntax                                       | Explanation                              | Example             | Notes / Gotchas                                            | Beginner Pitfalls                                         |
| -------------------- | -------------------------------------------- | ---------------------------------------- | ------------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| Assigning a variable | `variable_name = value`                      | Stores a value under a name.             | `message = "Hello"` | Names should be lowercase with underscores (`snake_case`). | Forgetting quotes around strings → `message = Hello` (❌). |
| Reassigning          | `variable_name = new_value`                  | Updates variable’s value.                | `message = "Hi"`    | Overwrites old value.                                      | Forgetting that old value is lost.                        |
| Naming rules         | Use letters, numbers, underscores; no spaces | Variables must start with letter or `_`. | `user_age = 25`     | Avoid Python keywords (`class`, `for`, etc.).              | Using invalid names like `2user` or `user-age`.           |

---

## 2. Strings

| Command / Concept       | Syntax                                       | Explanation                            | Example                                   | Notes / Gotchas                              | Beginner Pitfalls                                               |
| ----------------------- | -------------------------------------------- | -------------------------------------- | ----------------------------------------- | -------------------------------------------- | --------------------------------------------------------------- |
| String declaration      | `"text"` or `'text'`                         | Create a string.                       | `name = "Alice"`                          | Both quotes work, but must match.            | Mixing quote types: `"Alice'`.                                  |
| Concatenation           | `str1 + str2`                                | Joins two strings.                     | `"Hello, " + "World!"`                    | Use `f-strings` for readability.             | Forgetting space: `"Hello,"+"World!"` → no gap.                 |
| f-Strings               | `f"text {var}"`                              | Embed variables inside strings.        | `f"Hello, {name}!"`                       | Python ≥3.6 required.                        | Missing `f`: `"Hello, {name}"`.                                 |
| `.title()`              | `string.title()`                             | Capitalizes first letter of each word. | `"ada lovelace".title()` → `Ada Lovelace` | Use for formatting names.                    | Expecting it to change original string (strings are immutable). |
| `.upper()` / `.lower()` | `string.upper()` / `string.lower()`          | Converts to all caps / all lowercase.  | `"Python".upper()` → `PYTHON`             | Often used for case-insensitive comparisons. | Forgetting to reassign if you want the change stored.           |
| Whitespace stripping    | `string.strip()` / `.lstrip()` / `.rstrip()` | Removes whitespace (all/left/right).   | `" Python ".strip()` → `"Python"`         | Useful for cleaning user input.              | Expecting original string to change automatically.              |

---

## 3. Numbers

| Command / Concept | Syntax  | Explanation             | Example          | Notes / Gotchas                                           | Beginner Pitfalls                                 |
| ----------------- | ------- | ----------------------- | ---------------- | --------------------------------------------------------- | ------------------------------------------------- |
| Integers          | `int`   | Whole numbers.          | `2`, `-5`, `100` | No decimal point.                                         | Writing `02` is invalid in Python 3.              |
| Floats            | `float` | Decimal numbers.        | `0.1`, `3.14`    | May show rounding issues (`0.2+0.1=0.30000000000000004`). | Expecting exact decimal precision.                |
| Addition          | `+`     | Adds numbers.           | `2 + 3` → `5`    | Works with ints & floats.                                 | Adding string and number causes error: `"2" + 2`. |
| Subtraction       | `-`     | Subtracts numbers.      | `5 - 3` → `2`    | —                                                         | Using string minus number.                        |
| Multiplication    | `*`     | Multiplies numbers.     | `2 * 4` → `8`    | —                                                         | Forgetting `*`: writing `2x4`.                    |
| Division          | `/`     | Produces float.         | `5 / 2` → `2.5`  | Always float, even if evenly divisible.                   | Expecting integer.                                |
| Floor Division    | `//`    | Divides, keeps integer. | `5 // 2` → `2`   | Drops remainder.                                          | Confusing `/` vs `//`.                            |
| Modulo            | `%`     | Returns remainder.      | `5 % 2` → `1`    | Useful for even/odd check.                                | Forgetting `%` is remainder, not percent.         |
| Exponent          | `**`    | Raises power.           | `2 ** 3` → `8`   | Right-associative: `2 ** 3 ** 2 = 512`.                   | Expecting left-to-right.                          |

---

## 4. Combining Numbers & Strings

| Command / Concept        | Syntax                       | Explanation                    | Example                        | Notes / Gotchas                       | Beginner Pitfalls                       |
| ------------------------ | ---------------------------- | ------------------------------ | ------------------------------ | ------------------------------------- | --------------------------------------- |
| Convert number to string | `str(number)`                | Needed when joining with text. | `age = 23; "I am " + str(age)` | Always convert number → string.       | Forgetting conversion: `"I am " + age`. |
| Convert string to number | `int("23")`, `float("3.14")` | Parse number from string.      | `int("10") + 5` → `15`         | Only works if string is valid number. | Trying `int("ten")` → error.            |

---

## 5. Best Practices

* ✅ Use **descriptive variable names**: `user_age`, `total_price`.
* ✅ Keep **strings consistent** (stick with either `'` or `"`).
* ✅ Use **f-strings** for cleaner output.
* ⚠️ Be careful with **float rounding issues**.
* ⚠️ Always convert types before mixing (`str()`, `int()`, `float()`).

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 2**.

