

# 📘 Python Crash Course – Chapter 3

**Introducing Lists Cheat Sheet**

---

## 1. Creating Lists

| Command / Concept | Syntax                | Explanation            | Example                            | Notes / Gotchas                                | Beginner Pitfalls                    |
| ----------------- | --------------------- | ---------------------- | ---------------------------------- | ---------------------------------------------- | ------------------------------------ |
| Empty list        | `[]`                  | Creates an empty list. | `cars = []`                        | Ready to append later.                         | Forgetting brackets → `cars = list`. |
| List with values  | `[item1, item2, ...]` | Store multiple items.  | `cars = ["bmw", "audi", "toyota"]` | Items can be mixed types, but not recommended. | Missing commas → `["bmw" "audi"]`.   |

---

## 2. Accessing Elements

| Command / Concept | Syntax        | Explanation          | Example                 | Notes / Gotchas   | Beginner Pitfalls                 |
| ----------------- | ------------- | -------------------- | ----------------------- | ----------------- | --------------------------------- |
| Indexing          | `list[index]` | Access by position.  | `cars[0]` → `"bmw"`     | Zero-based index. | Using `1` for first item.         |
| Negative index    | `list[-1]`    | Access from the end. | `cars[-1]` → `"toyota"` | `-1` = last item. | Using out-of-range index → error. |

---

## 3. Modifying Lists

| Command / Concept | Syntax                     | Explanation                  | Example                 | Notes / Gotchas             | Beginner Pitfalls                  |
| ----------------- | -------------------------- | ---------------------------- | ----------------------- | --------------------------- | ---------------------------------- |
| Change value      | `list[index] = new_value`  | Replaces an item.            | `cars[0] = "mercedes"`  | Overwrites only that index. | Forgetting index.                  |
| Append item       | `list.append(item)`        | Adds to the end.             | `cars.append("honda")`  | Always one item.            | Using `append` for multiple items. |
| Insert item       | `list.insert(index, item)` | Adds at a specific position. | `cars.insert(1, "kia")` | Shifts following items.     | Forgetting index argument.         |

---

## 4. Removing Elements

| Command / Concept | Syntax               | Explanation               | Example               | Notes / Gotchas               | Beginner Pitfalls                   |
| ----------------- | -------------------- | ------------------------- | --------------------- | ----------------------------- | ----------------------------------- |
| Delete by index   | `del list[index]`    | Removes permanently.      | `del cars[0]`         | Cannot retrieve deleted item. | Deleting wrong index.               |
| Pop by index      | `list.pop(index)`    | Removes and returns item. | `last = cars.pop()`   | Defaults to last item.        | Forgetting `()` → `TypeError`.      |
| Remove by value   | `list.remove(value)` | Removes first match.      | `cars.remove("audi")` | Errors if value not found.    | Expecting it to remove all matches. |

---

## 5. Sorting and Reversing

| Command / Concept | Syntax                    | Explanation                       | Example                   | Notes / Gotchas                             | Beginner Pitfalls                 |
| ----------------- | ------------------------- | --------------------------------- | ------------------------- | ------------------------------------------- | --------------------------------- |
| Permanent sort    | `list.sort()`             | Sorts alphabetically/numerically. | `cars.sort()`             | Case-sensitive: uppercase before lowercase. | Expecting to keep original order. |
| Reverse sort      | `list.sort(reverse=True)` | Sorts descending.                 | `cars.sort(reverse=True)` | —                                           | Forgetting `reverse=True`.        |
| Temporary sort    | `sorted(list)`            | Returns sorted copy.              | `sorted(cars)`            | Original unchanged.                         | Forgetting to reassign.           |
| Reverse order     | `list.reverse()`          | Flips order.                      | `cars.reverse()`          | Not the same as sorting.                    | Expecting alphabetical order.     |

---

## 6. List Length

| Command / Concept | Syntax      | Explanation   | Example           | Notes / Gotchas            | Beginner Pitfalls           |
| ----------------- | ----------- | ------------- | ----------------- | -------------------------- | --------------------------- |
| Length            | `len(list)` | Counts items. | `len(cars)` → `3` | Works with empty list too. | Using `list.len()` (wrong). |

---

## 7. Best Practices

* ✅ Use **plural nouns** for lists (`cars`, not `car`).
* ✅ Use `sorted()` if you need original order preserved.
* ⚠️ Remember **zero-based indexing**.
* ⚠️ Be careful when using `remove()` on items that may not exist.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 3**.

