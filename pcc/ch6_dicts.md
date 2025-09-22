

# 📘 Python Crash Course – Chapter 6

**Dictionaries Cheat Sheet**

---

## 1. Creating Dictionaries

| Command / Concept      | Syntax              | Explanation                     | Example                                   | Notes / Gotchas      | Beginner Pitfalls                  |
| ---------------------- | ------------------- | ------------------------------- | ----------------------------------------- | -------------------- | ---------------------------------- |
| Empty dictionary       | `{}`                | Starts with no key-value pairs. | `alien = {}`                              | Ready to add later.  | Forgetting braces → `[]` (list).   |
| Dictionary with values | `{key: value, ...}` | Stores key–value pairs.         | `alien = {"color": "green", "points": 5}` | Keys must be unique. | Missing quotes around string keys. |

---

## 2. Accessing Values

| Command / Concept | Syntax                   | Explanation                          | Example                      | Notes / Gotchas                      | Beginner Pitfalls          |
| ----------------- | ------------------------ | ------------------------------------ | ---------------------------- | ------------------------------------ | -------------------------- |
| Get value by key  | `dict[key]`              | Retrieves value for a key.           | `alien["color"]` → `"green"` | Key must exist or raises `KeyError`. | Using wrong key spelling.  |
| `.get()` method   | `dict.get(key, default)` | Returns value or default if missing. | `alien.get("speed", "slow")` | Prevents crash if key missing.       | Forgetting to set default. |

---

## 3. Adding & Modifying Values

| Command / Concept | Syntax                  | Explanation               | Example                     | Notes / Gotchas                         | Beginner Pitfalls               |
| ----------------- | ----------------------- | ------------------------- | --------------------------- | --------------------------------------- | ------------------------------- |
| Add new key-value | `dict[key] = value`     | Creates or updates entry. | `alien["x_pos"] = 0`        | Updates if key already exists.          | Accidentally overwriting value. |
| Modify value      | `dict[key] = new_value` | Updates existing value.   | `alien["color"] = "yellow"` | Key must exist or it creates a new one. | Confusing update vs. add.       |

---

## 4. Removing Key-Value Pairs

| Command / Concept | Syntax                   | Explanation                 | Example               | Notes / Gotchas            | Beginner Pitfalls                     |
| ----------------- | ------------------------ | --------------------------- | --------------------- | -------------------------- | ------------------------------------- |
| Delete with `del` | `del dict[key]`          | Removes entry permanently.  | `del alien["points"]` | Key must exist.            | Deleting non-existent key → error.    |
| `.pop(key)`       | `dict.pop(key, default)` | Removes and returns value.  | `alien.pop("points")` | Default avoids `KeyError`. | Forgetting parentheses.               |
| `.popitem()`      | `dict.popitem()`         | Removes last inserted item. | `alien.popitem()`     | Useful for stacks.         | Unpredictable in old Python versions. |

---

## 5. Looping Through Dictionaries

| Command / Concept  | Syntax                        | Explanation                       | Example                                                             | Notes / Gotchas                  | Beginner Pitfalls                   |
| ------------------ | ----------------------------- | --------------------------------- | ------------------------------------------------------------------- | -------------------------------- | ----------------------------------- |
| Loop keys & values | `for k, v in dict.items():`   | Iterates through key–value pairs. | `python\nfor key, value in alien.items():\n    print(key, value)\n` | Order preserved (Python 3.7+).   | Forgetting `.items()`.              |
| Loop keys          | `for key in dict.keys():`     | Iterates keys only.               | `for key in alien.keys():`                                          | Same as `for key in dict:`.      | Assuming it gives values.           |
| Loop values        | `for value in dict.values():` | Iterates values only.             | `for color in alien.values():`                                      | Use `set()` to avoid duplicates. | Expecting unique values by default. |

---

## 6. Nesting Dictionaries

| Command / Concept            | Syntax                   | Explanation                       | Example                                                                          | Notes / Gotchas             | Beginner Pitfalls                                          |
| ---------------------------- | ------------------------ | --------------------------------- | -------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------- |
| Dictionary inside dictionary | `{key: {subkey: value}}` | Stores multiple dicts inside one. | `python\nusers = {\n  'aeinstein': {'first': 'albert', 'last': 'einstein'}\n}\n` | Common for structured data. | Forgetting nested indexing: `users['aeinstein']['first']`. |
| List of dictionaries         | `[{}, {}, ...]`          | Multiple dicts stored in a list.  | `python\naliens = [alien_0, alien_1]\n`                                          | Great for grouped data.     | Mixing up list vs dict syntax.                             |

---

## 7. Best Practices

* ✅ Use `.get()` when unsure if key exists.
* ✅ Loop with `.items()` when you need both key and value.
* ⚠️ Remember that keys must be **immutable types** (strings, numbers, tuples).
* ⚠️ Be cautious with nesting — keep structure readable.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 6**.

