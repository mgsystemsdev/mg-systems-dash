

# 📘 Python Crash Course – Chapter 10

**Files and Exceptions Cheat Sheet**

---

## 1. Reading Files

| Command / Concept    | Syntax           | Explanation                         | Example                                     | Notes / Gotchas             | Beginner Pitfalls                         |
| -------------------- | ---------------- | ----------------------------------- | ------------------------------------------- | --------------------------- | ----------------------------------------- |
| Open file            | `open(filename)` | Opens file in read mode by default. | `f = open("pi_digits.txt")`                 | Must close later.           | Forgetting to close file.                 |
| Read entire file     | `f.read()`       | Reads all contents as string.       | `contents = f.read()`                       | Includes `\n` line breaks.  | Large files → memory heavy.               |
| Read line by line    | `for line in f:` | Iterates over each line.            | `python\nfor line in f:\n    print(line)\n` | Keeps `\n`. Use `.strip()`. | Forgetting `.strip()` causes blank lines. |
| Read lines into list | `f.readlines()`  | Stores lines in a list.             | `lines = f.readlines()`                     | Each element has `\n`.      | Not stripping newlines.                   |

---

## 2. Writing Files

| Command / Concept    | Syntax                | Explanation              | Example                                                           | Notes / Gotchas             | Beginner Pitfalls             |
| -------------------- | --------------------- | ------------------------ | ----------------------------------------------------------------- | --------------------------- | ----------------------------- |
| Write (overwrite)    | `open(filename, 'w')` | Creates/overwrites file. | `python\nwith open("file.txt","w") as f:\n    f.write("Hello")\n` | Destroys old contents.      | Forgetting `'w'` erases file. |
| Append               | `open(filename, 'a')` | Adds to end of file.     | `python\nwith open("file.txt","a") as f:\n    f.write("More")\n`  | File is created if missing. | Expecting `'a'` to overwrite. |
| Write multiple lines | `f.write("line\n")`   | Must add `\n` manually.  | `f.write("Line 1\nLine 2\n")`                                     | No auto line breaks.        | Forgetting `\n`.              |

---

## 3. The `with` Statement (Best Practice)

| Command / Concept | Syntax                 | Explanation       | Example                                                          | Notes / Gotchas          | Beginner Pitfalls                   |
| ----------------- | ---------------------- | ----------------- | ---------------------------------------------------------------- | ------------------------ | ----------------------------------- |
| Context manager   | `with open(...) as f:` | Auto-closes file. | `python\nwith open("file.txt") as f:\n    contents = f.read()\n` | No need for `f.close()`. | Forgetting `with` → resource leaks. |

---

## 4. Exceptions (Error Handling)

| Command / Concept   | Syntax                                                | Explanation                          | Example                                                                                                      | Notes / Gotchas                                    | Beginner Pitfalls                             |
| ------------------- | ----------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | --------------------------------------------- |
| Try/except          | `python\ntry:\n    ...\nexcept ErrorType:\n    ...\n` | Prevents crashes by handling errors. | `python\ntry:\n    f = open("missing.txt")\nexcept FileNotFoundError:\n    print("File not found")\n`        | Catch specific exceptions.                         | Using bare `except:` hides real errors.       |
| Multiple exceptions | `except (Error1, Error2):`                            | Catches several error types.         | `except (FileNotFoundError, PermissionError):`                                                               | Group with tuple.                                  | Forgetting parentheses.                       |
| else                | `else:`                                               | Runs if no exception.                | `python\ntry:\n    f = open("file.txt")\nexcept FileNotFoundError:\n    ...\nelse:\n    print("Success!")\n` | Good for success code.                             | Misplacing `else`.                            |
| finally             | `finally:`                                            | Always runs (cleanup).               | `python\ntry:\n    f = open("file.txt")\nfinally:\n    print("Done")\n`                                      | Used for cleanup (close files, release resources). | Overusing when `with` handles cleanup better. |

---

## 5. Common Exceptions

| Error               | When it Happens                       |
| ------------------- | ------------------------------------- |
| `FileNotFoundError` | File doesn’t exist.                   |
| `PermissionError`   | No permission to access file.         |
| `ValueError`        | Wrong type conversion (`int("abc")`). |
| `ZeroDivisionError` | Divide by zero.                       |

---

## 6. Best Practices

* ✅ Always use `with open(...) as f:`.
* ✅ Handle **specific** exceptions, not generic `except:`.
* ✅ Add `\n` manually when writing new lines.
* ⚠️ Opening with `'w'` **erases file contents**.
* ⚠️ Don’t assume input will always be valid (wrap with try/except).

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 10**.

