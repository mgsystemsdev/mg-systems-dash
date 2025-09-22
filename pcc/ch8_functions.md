
# 📘 Python Crash Course – Chapter 8

**Functions Cheat Sheet**

---

## 1. Defining Functions

| Command / Concept | Syntax        | Explanation                     | Example                                       | Notes / Gotchas                       | Beginner Pitfalls                            |
| ----------------- | ------------- | ------------------------------- | --------------------------------------------- | ------------------------------------- | -------------------------------------------- |
| Basic function    | `def name():` | Defines reusable block of code. | `python\ndef greet():\n    print("Hello!")\n` | Must use `def` + colon + indentation. | Forgetting `()` when calling → no execution. |
| Call function     | `name()`      | Executes function.              | `greet()`                                     | Must match definition exactly.        | Using undefined function.                    |

---

## 2. Passing Information

| Command / Concept   | Syntax              | Explanation                    | Example                                                    | Notes / Gotchas                       | Beginner Pitfalls                  |
| ------------------- | ------------------- | ------------------------------ | ---------------------------------------------------------- | ------------------------------------- | ---------------------------------- |
| Parameter           | `def func(param):`  | Accepts input inside function. | `python\ndef greet(name):\n    print(f"Hello, {name}!")\n` | Placeholder until function is called. | Forgetting to pass argument.       |
| Multiple parameters | `def func(p1, p2):` | Accepts multiple inputs.       | `def add(a, b): return a + b`                              | Order matters unless using keywords.  | Passing wrong number of arguments. |

---

## 3. Return Values

| Command / Concept      | Syntax         | Explanation                  | Example                                      | Notes / Gotchas                            | Beginner Pitfalls                           |
| ---------------------- | -------------- | ---------------------------- | -------------------------------------------- | ------------------------------------------ | ------------------------------------------- |
| Return                 | `return value` | Sends result back to caller. | `python\ndef add(a, b):\n    return a + b\n` | Without `return`, function returns `None`. | Forgetting to store result.                 |
| Return dictionary/list | `return {...}` | Can return complex objects.  | `return {"first": first, "last": last}`      | Useful for structured data.                | Expecting multiple returns without packing. |

---

## 4. Arguments

| Command / Concept | Syntax                 | Explanation                        | Example                    | Notes / Gotchas                   | Beginner Pitfalls                    |
| ----------------- | ---------------------- | ---------------------------------- | -------------------------- | --------------------------------- | ------------------------------------ |
| Positional args   | `func(val1, val2)`     | Matched by position.               | `add(2, 3)`                | Must be in correct order.         | Mixing order.                        |
| Keyword args      | `func(param=value)`    | Explicitly assign argument.        | `greet(name="Alice")`      | Improves clarity.                 | Misspelling keyword name.            |
| Default values    | `def func(p=default):` | Provides fallback if no arg given. | `def greet(name="Guest"):` | Defaults only once at definition. | Using mutable defaults (`[]`, `{}`). |

---

## 5. Flexible Arguments

| Command / Concept    | Syntax     | Explanation                          | Example                                                 | Notes / Gotchas             | Beginner Pitfalls             |
| -------------------- | ---------- | ------------------------------------ | ------------------------------------------------------- | --------------------------- | ----------------------------- |
| Arbitrary positional | `*args`    | Collects extra args as tuple.        | `python\ndef sum_all(*nums):\n    return sum(nums)\n`   | Use when unknown # of args. | Forgetting `*` when defining. |
| Arbitrary keyword    | `**kwargs` | Collects extra keyword args as dict. | `python\ndef build_profile(**info):\n    return info\n` | Great for flexible data.    | Forgetting `**` in call.      |

---

## 6. Organizing Functions

| Command / Concept | Syntax                    | Explanation                | Example                        | Notes / Gotchas                        | Beginner Pitfalls                         |
| ----------------- | ------------------------- | -------------------------- | ------------------------------ | -------------------------------------- | ----------------------------------------- |
| Import function   | `from module import func` | Brings function into file. | `from pizza import make_pizza` | Use aliases with `as`.                 | Forgetting `.py` extension is not needed. |
| Module import     | `import module`           | Imports whole file.        | `import pizza`                 | Call as `pizza.make_pizza()`.          | Using undefined module.                   |
| Aliases           | `import module as m`      | Shortens module name.      | `import pizza as p`            | Helps readability.                     | Forgetting alias in call.                 |
| Import all        | `from module import *`    | Imports everything.        | `from pizza import *`          | Not recommended (can cause conflicts). | Overwriting built-ins.                    |

---

## 7. Best Practices

* ✅ Use **descriptive function names** (`calculate_total`, not `do_stuff`).
* ✅ Keep functions short and focused on **one task**.
* ✅ Use **default parameters** to simplify calls.
* ⚠️ Avoid **mutable default arguments** (`[]`, `{}`).
* ⚠️ Organize functions into **modules** for clarity.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 8**.

