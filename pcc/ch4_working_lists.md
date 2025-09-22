

# 📘 Python Crash Course – Chapter 4

**Working with Lists Cheat Sheet**

---

## 1. Looping Through Lists

| Command / Concept     | Syntax                         | Explanation                                        | Example                                      | Notes / Gotchas                    | Beginner Pitfalls                          |
| --------------------- | ------------------------------ | -------------------------------------------------- | -------------------------------------------- | ---------------------------------- | ------------------------------------------ |
| For loop              | `for item in list:`            | Iterates through each element.                     | `python\nfor car in cars:\n    print(car)\n` | Indentation is required in Python. | Forgetting colon (`:`).                    |
| Using a variable name | `for singular in plural_list:` | Best practice: singular for item, plural for list. | `for dog in dogs:`                           | Improves readability.              | Using unclear names like `for x in list:`. |

---

## 2. Creating Number Lists

| Command / Concept | Syntax                                | Explanation                               | Example                            | Notes / Gotchas                  | Beginner Pitfalls              |
| ----------------- | ------------------------------------- | ----------------------------------------- | ---------------------------------- | -------------------------------- | ------------------------------ |
| `range()`         | `range(start, stop)`                  | Generates a sequence (stop not included). | `range(1, 5)` → `[1,2,3,4]`        | Convert with `list(range(...))`. | Expecting stop to be included. |
| Step in range     | `range(start, stop, step)`            | Counts by step size.                      | `range(2, 11, 2)` → `[2,4,6,8,10]` | Works with negatives too.        | Forgetting third argument.     |
| Min, Max, Sum     | `min(list)`, `max(list)`, `sum(list)` | Quick math on lists.                      | `sum([1,2,3])` → `6`               | Works only with numbers.         | Applying to mixed-type lists.  |

---

## 3. List Comprehensions

| Command / Concept | Syntax                          | Explanation                     | Example                                        | Notes / Gotchas                | Beginner Pitfalls                     |
| ----------------- | ------------------------------- | ------------------------------- | ---------------------------------------------- | ------------------------------ | ------------------------------------- |
| Basic             | `[expression for item in list]` | Compact way to create new list. | `[x**2 for x in range(1,6)]` → `[1,4,9,16,25]` | Readable alternative to loops. | Making them too complex → unreadable. |

---

## 4. Slicing Lists

| Command / Concept | Syntax                | Explanation                           | Example                        | Notes / Gotchas                        | Beginner Pitfalls                     |
| ----------------- | --------------------- | ------------------------------------- | ------------------------------ | -------------------------------------- | ------------------------------------- |
| Slice             | `list[start:end]`     | Extracts part of list (end excluded). | `cars[0:2]` → `['bmw','audi']` | Omit start → from beginning.           | Expecting end to be included.         |
| Negative indices  | `list[-n:]`           | Slice from end.                       | `cars[-2:]`                    | Useful for last elements.              | Miscounting negative indexes.         |
| Copy list         | `list_copy = list[:]` | Makes full copy.                      | `new_cars = cars[:]`           | Avoids two vars pointing to same list. | Doing `new_cars = cars` (just alias). |

---

## 5. Tuples (Immutable Lists)

| Command / Concept | Syntax                 | Explanation               | Example                   | Notes / Gotchas                 | Beginner Pitfalls                          |
| ----------------- | ---------------------- | ------------------------- | ------------------------- | ------------------------------- | ------------------------------------------ |
| Create tuple      | `(item1, item2)`       | Like lists but immutable. | `dimensions = (200, 50)`  | Use parentheses or no brackets. | Forgetting comma in 1-item tuple → `(5,)`. |
| Access values     | `tuple[index]`         | Same as list indexing.    | `dimensions[0]` → `200`   | Cannot reassign elements.       | Trying `dimensions[0] = 250`.              |
| Reassign tuple    | `tuple = (new1, new2)` | Replace entire tuple.     | `dimensions = (400, 100)` | Not modifying, but rebinding.   | Confusing with list behavior.              |

---

## 6. Best Practices

* ✅ Use **for loops** for readability; comprehensions only when simple.
* ✅ Always copy lists with `[:]` if you want independence.
* ⚠️ Remember tuples are **immutable**.
* ⚠️ `range()` stops **one before** the number given.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 4**.

