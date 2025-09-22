

# 📘 Python Variables Cheat Sheet

**All Commands & Concepts Related to Variables**

---

## 1. Declaring Variables

| Command             | Syntax              | Explanation              | Notes / Gotchas               |
| ------------------- | ------------------- | ------------------------ | ----------------------------- |
| Basic assignment    | `x = 5`             | Assigns value.           | No type declaration needed.   |
| Multiple assignment | `a, b, c = 1, 2, 3` | Assign multiple at once. | Lengths must match.           |
| Same value          | `a = b = c = 0`     | Assign same value.       | Independent after assignment. |
| Swap values         | `a, b = b, a`       | Swap without temp var.   | Pythonic way.                 |

---

## 2. Variable Types

| Type    | Example          | Notes                |
| ------- | ---------------- | -------------------- |
| Integer | `x = 42`         | Whole numbers.       |
| Float   | `pi = 3.14`      | Decimals.            |
| String  | `name = "Alice"` | Text in quotes.      |
| Boolean | `flag = True`    | `True` / `False`.    |
| None    | `val = None`     | Represents no value. |
| Complex | `z = 2 + 3j`     | Real + imaginary.    |

---

## 3. Checking & Casting Types

| Command         | Syntax              | Explanation                   |
| --------------- | ------------------- | ----------------------------- |
| Type check      | `type(x)`           | Shows type.                   |
| Instance check  | `isinstance(x,int)` | Check class.                  |
| Casting → int   | `int("5")`          | Convert to integer.           |
| Casting → float | `float("3.14")`     | Convert to float.             |
| Casting → str   | `str(123)`          | Convert to string.            |
| Casting → bool  | `bool(0)`           | False if `0`, empty, or None. |

---

## 4. Variable Naming Rules

* ✅ Must start with letter or `_`
* ✅ Can contain letters, numbers, `_`
* ❌ Cannot start with number
* ❌ Cannot be a Python **keyword** (`for`, `if`, `class`, etc.)

---

## 5. Constants (By Convention)

| Command     | Syntax                 | Explanation                      |
| ----------- | ---------------------- | -------------------------------- |
| Constant    | `PI = 3.14159`         | Uppercase → treated as constant. |
| Typing hint | `MAX_USERS: int = 100` | Adds type annotation.            |

---

## 6. Scope

| Scope            | Example                                                                                   | Explanation                      |
| ---------------- | ----------------------------------------------------------------------------------------- | -------------------------------- |
| Local            | Inside function                                                                           | Visible only inside.             |
| Global           | Defined outside function                                                                  | Visible everywhere.              |
| Global keyword   | `python\nglob_var = 10\n\ndef func():\n    global glob_var\n    glob_var = 20\n`          | Modifies outer variable.         |
| Nonlocal keyword | `python\ndef outer():\n    x = 5\n    def inner():\n        nonlocal x\n        x += 1\n` | Modify enclosing scope variable. |

---

## 7. Deleting Variables

| Command         | Syntax     | Explanation                   |
| --------------- | ---------- | ----------------------------- |
| Delete          | `del x`    | Removes variable from memory. |
| Delete multiple | `del a, b` | Delete multiple.              |

---

## 8. Dynamic Features

| Command     | Syntax                                  | Explanation |
| ----------- | --------------------------------------- | ----------- |
| `globals()` | Returns dict of global vars.            |             |
| `locals()`  | Returns dict of local vars.             |             |
| `vars()`    | Returns dict of object attributes/vars. |             |
| `id(x)`     | Memory address of variable.             |             |
| `dir()`     | List of attributes/methods.             |             |

---

## 9. Beginner Pitfalls

* ❌ Using reserved keywords (`for`, `class`) as variable names.
* ❌ Mixing types accidentally (`x = "5"; y = 2; print(x+y) → error`).
* ❌ Forgetting `global` when modifying globals inside functions.
* ❌ Confusing assignment `=` with comparison `==`.
* ❌ Shadowing built-ins (e.g., naming variable `list` or `str`).

---

👉 This is a **complete cheat sheet of variables in Python** — covering declaration, assignment, scope, type casting, deletion, and pitfalls.


---

---

## 📘 Python String Case Methods (`str`)

| Method             | Syntax                  | Explanation                            | Example                         | Notes / Pitfalls                                            |
| ------------------ | ----------------------- | -------------------------------------- | ------------------------------- | ----------------------------------------------------------- |
| `str.upper()`      | `"hello".upper()`       | Converts to uppercase.                 | `"hello".upper() → "HELLO"`     | Returns new string (strings are immutable).                 |
| `str.lower()`      | `"HELLO".lower()`       | Converts to lowercase.                 | `"HELLO".lower() → "hello"`     | Good for case-insensitive compare.                          |
| `str.title()`      | `"hello world".title()` | Capitalizes first letter of each word. | `"hello world" → "Hello World"` | Doesn’t always handle apostrophes well (`"it's" → "It'S"`). |
| `str.capitalize()` | `"hello".capitalize()`  | Capitalizes first letter of string.    | `"hello" → "Hello"`             | Only first word affected.                                   |
| `str.swapcase()`   | `"HeLLo".swapcase()`    | Swaps uppercase/lowercase.             | `"HeLLo" → "hEllO"`             | Useful for toggling.                                        |
| `str.casefold()`   | `"ß".casefold()`        | Aggressive lowercase (for Unicode).    | `"ß" → "ss"`                    | Better for comparisons than `.lower()`.                     |

---

✅ So to answer directly: **they fall into the String (`str`) data type methods**.

---

---

---

# 📘 Python String Methods Cheat Sheet

**All Built-in `str` Methods**

---

## 1. Case Methods

| Method         | Example              | Result       |
| -------------- | -------------------- | ------------ |
| `upper()`      | `"hi".upper()`       | `"HI"`       |
| `lower()`      | `"HI".lower()`       | `"hi"`       |
| `title()`      | `"hi world".title()` | `"Hi World"` |
| `capitalize()` | `"hi".capitalize()`  | `"Hi"`       |
| `swapcase()`   | `"Hi".swapcase()`    | `"hI"`       |
| `casefold()`   | `"ß".casefold()`     | `"ss"`       |

---

## 2. Check Methods (`is...`)

| Method           | Example                 | Result  |
| ---------------- | ----------------------- | ------- |
| `isupper()`      | `"HI".isupper()`        | `True`  |
| `islower()`      | `"hi".islower()`        | `True`  |
| `istitle()`      | `"Hi World".istitle()`  | `True`  |
| `isalnum()`      | `"abc123".isalnum()`    | `True`  |
| `isalpha()`      | `"abc".isalpha()`       | `True`  |
| `isdigit()`      | `"123".isdigit()`       | `True`  |
| `isdecimal()`    | `"²".isdecimal()`       | `False` |
| `isnumeric()`    | `"²".isnumeric()`       | `True`  |
| `isascii()`      | `"a".isascii()`         | `True`  |
| `isidentifier()` | `"var1".isidentifier()` | `True`  |
| `isspace()`      | `" \t".isspace()`       | `True`  |
| `isprintable()`  | `"abc".isprintable()`   | `True`  |

---

## 3. Search & Find

| Method         | Example                    | Result |
| -------------- | -------------------------- | ------ |
| `find()`       | `"hello".find("l")`        | `2`    |
| `rfind()`      | `"hello".rfind("l")`       | `3`    |
| `index()`      | `"hello".index("e")`       | `1`    |
| `rindex()`     | `"hello".rindex("l")`      | `3`    |
| `count()`      | `"hello".count("l")`       | `2`    |
| `startswith()` | `"hello".startswith("he")` | `True` |
| `endswith()`   | `"hello".endswith("lo")`   | `True` |

---

## 4. Modify / Replace

| Method           | Example                           | Result    |
| ---------------- | --------------------------------- | --------- |
| `replace()`      | `"hi hi".replace("hi","yo")`      | `"yo yo"` |
| `removeprefix()` | `"unhappy".removeprefix("un")`    | `"happy"` |
| `removesuffix()` | `"file.txt".removesuffix(".txt")` | `"file"`  |

---

## 5. Strip & Trim

| Method     | Example           | Result  |
| ---------- | ----------------- | ------- |
| `strip()`  | `" hi ".strip()`  | `"hi"`  |
| `lstrip()` | `" hi ".lstrip()` | `"hi "` |
| `rstrip()` | `" hi ".rstrip()` | `" hi"` |

---

## 6. Split & Join

| Method         | Example                   | Result            |
| -------------- | ------------------------- | ----------------- |
| `split()`      | `"a,b,c".split(",")`      | `["a","b","c"]`   |
| `rsplit()`     | `"a b c".rsplit(" ",1)`   | `["a b","c"]`     |
| `splitlines()` | `"a\nb".splitlines()`     | `["a","b"]`       |
| `partition()`  | `"a=b".partition("=")`    | `("a","=","b")`   |
| `rpartition()` | `"a=b=c".rpartition("=")` | `("a=b","=","c")` |
| `join()`       | `",".join(["a","b"])`     | `"a,b"`           |

---

## 7. Alignment & Padding

| Method     | Example              | Result    |
| ---------- | -------------------- | --------- |
| `center()` | `"hi".center(5,"-")` | `"-hi-"`  |
| `ljust()`  | `"hi".ljust(5,"-")`  | `"hi---"` |
| `rjust()`  | `"hi".rjust(5,"-")`  | `"---hi"` |
| `zfill()`  | `"42".zfill(5)`      | `"00042"` |

---

## 8. Encoding & Translation

| Method        | Example                      | Result        |
| ------------- | ---------------------------- | ------------- |
| `encode()`    | `"hi".encode("utf-8")`       | `b'hi'`       |
| `maketrans()` | `str.maketrans("abc","123")` | Mapping dict. |
| `translate()` | `"abc".translate(tbl)`       | `"123"`       |

---

## ✅ Final Count

🔹 Total string methods (Python 3.11): **\~50+**
We’ve now listed **all transformation, check, search, split, and encoding methods**.

---

👉 This is the **full cheat sheet for Python string methods**.

