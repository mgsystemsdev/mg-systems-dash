

# 📘 Python Crash Course – Chapter 7

**User Input and while Loops Cheat Sheet**

---

## 1. Getting User Input

| Command / Concept | Syntax              | Explanation                            | Example                             | Notes / Gotchas                | Beginner Pitfalls                     |
| ----------------- | ------------------- | -------------------------------------- | ----------------------------------- | ------------------------------ | ------------------------------------- |
| Input             | `input(prompt)`     | Pauses program and returns typed text. | `name = input("Enter your name: ")` | Always returns a **string**.   | Forgetting quotes in prompt.          |
| Convert to int    | `int(input(...))`   | Converts input to integer.             | `age = int(input("Age: "))`         | Errors if non-numeric entered. | Forgetting conversion before math.    |
| Convert to float  | `float(input(...))` | Converts to decimal.                   | `price = float(input("Price: "))`   | Handles decimals properly.     | Using `int()` when decimals expected. |

---

## 2. While Loops (Repeating Code)

| Command / Concept | Syntax             | Explanation                          | Example                                                    | Notes / Gotchas                              | Beginner Pitfalls    |
| ----------------- | ------------------ | ------------------------------------ | ---------------------------------------------------------- | -------------------------------------------- | -------------------- |
| Basic loop        | `while condition:` | Repeats block until condition false. | `python\nx = 1\nwhile x <= 5:\n    print(x)\n    x += 1\n` | Must update variable to avoid infinite loop. | Forgetting `x += 1`. |
| Infinite loop     | `while True:`      | Runs forever until stopped.          | `python\nwhile True:\n    print("Press Ctrl+C to stop")\n` | Break with `break`.                          | Forgetting `break`.  |

---

## 3. Loop Control

| Command / Concept | Syntax                       | Explanation                      | Example                                                                                                               | Notes / Gotchas                       | Beginner Pitfalls                    |
| ----------------- | ---------------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------ |
| `break`           | `break`                      | Exits loop immediately.          | `python\nwhile True:\n    msg = input("Type 'quit': ")\n    if msg == 'quit':\n        break\n`                       | Often used with `while True:`.        | Forgetting condition → stuck loop.   |
| `continue`        | `continue`                   | Skips rest of current iteration. | `python\nx = 0\nwhile x < 5:\n    x += 1\n    if x % 2 == 0:\n        continue\n    print(x)\n`                       | Use carefully to avoid infinite loop. | Forgetting update before `continue`. |
| Flags             | `active = True` + loop check | Use boolean to control loop.     | `python\nactive = True\nwhile active:\n    msg = input("Message: ")\n    if msg == 'quit':\n        active = False\n` | Clearer than `while True`.            | Forgetting to reset flag.            |

---

## 4. Using while with Lists & Dictionaries

| Command / Concept    | Syntax                 | Explanation                     | Example                                                                                                                                 | Notes / Gotchas             | Beginner Pitfalls                 |
| -------------------- | ---------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------- |
| Moving items         | `while list:`          | Loop until list empty.          | `python\nunconfirmed = ['alice','bob']\nconfirmed = []\nwhile unconfirmed:\n    user = unconfirmed.pop()\n    confirmed.append(user)\n` | Common in workflows.        | Forgetting `.pop()` empties list. |
| Removing all matches | `while value in list:` | Keeps removing until none left. | `python\npets = ['cat','dog','cat']\nwhile 'cat' in pets:\n    pets.remove('cat')\n`                                                    | Avoids one-pass `remove()`. | Assuming `remove()` deletes all.  |

---

## 5. Best Practices

* ✅ Always ensure a **loop exit condition**.
* ✅ Use `break` for emergency stops, flags for controlled flow.
* ✅ Convert input to numbers **before math**.
* ⚠️ Watch for **infinite loops** (common beginner mistake).
* ⚠️ Remember: `input()` **always returns a string**.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 7**.
