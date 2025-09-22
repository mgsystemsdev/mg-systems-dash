
# 📘 Python Crash Course – Chapter 11

**Testing Your Code Cheat Sheet**

---

## 1. The `unittest` Framework

| Command / Concept | Syntax                               | Explanation                             | Example                                                     | Notes / Gotchas                      | Beginner Pitfalls                    |
| ----------------- | ------------------------------------ | --------------------------------------- | ----------------------------------------------------------- | ------------------------------------ | ------------------------------------ |
| Import            | `import unittest`                    | Loads Python’s built-in test framework. | `import unittest`                                           | Standard library, no install needed. | Forgetting import.                   |
| Test class        | `class TestName(unittest.TestCase):` | Groups related tests.                   | `python\nclass TestFuncs(unittest.TestCase):\n    ...\n`    | Must inherit `unittest.TestCase`.    | Forgetting parent class.             |
| Run tests         | `unittest.main()`                    | Executes all tests in file.             | `python\nif __name__ == '__main__':\n    unittest.main()\n` | Standard test runner.                | Forgetting guard (`if __name__...`). |

---

## 2. Writing Test Methods

| Command / Concept | Syntax                      | Explanation                        | Example                                                            | Notes / Gotchas                 | Beginner Pitfalls          |
| ----------------- | --------------------------- | ---------------------------------- | ------------------------------------------------------------------ | ------------------------------- | -------------------------- |
| Method format     | `def test_something(self):` | Each test must start with `test_`. | `python\ndef test_addition(self):\n    self.assertEqual(2+3, 5)\n` | Otherwise, unittest ignores it. | Forgetting `test_` prefix. |

---

## 3. Common Assertions

| Assertion | Syntax                    | Explanation                    | Example                         | Notes / Gotchas                      | Beginner Pitfalls                        |
| --------- | ------------------------- | ------------------------------ | ------------------------------- | ------------------------------------ | ---------------------------------------- |
| Equal     | `assertEqual(a, b)`       | Passes if `a == b`.            | `self.assertEqual(add(2,3), 5)` | Most common check.                   | Using `=` instead of `==`.               |
| Not equal | `assertNotEqual(a, b)`    | Passes if `a != b`.            | `self.assertNotEqual(2+2, 5)`   | —                                    | Forgetting logic.                        |
| True      | `assertTrue(expr)`        | Passes if expression is True.  | `self.assertTrue(5 > 2)`        | —                                    | Testing expressions that aren’t boolean. |
| False     | `assertFalse(expr)`       | Passes if expression is False. | `self.assertFalse(3 > 5)`       | —                                    | Mixing up truth values.                  |
| In        | `assertIn(item, list)`    | Passes if item found.          | `self.assertIn('dog', pets)`    | Works for lists, strings, dict keys. | Forgetting case sensitivity.             |
| Not in    | `assertNotIn(item, list)` | Passes if item not found.      | `self.assertNotIn('cat', pets)` | —                                    | Confusing with equality.                 |

---

## 4. Testing Functions

| Command / Concept | Syntax                                                                                                                                                                                                            | Explanation                       | Example                          | Notes / Gotchas                         | Beginner Pitfalls  |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------- | --------------------------------------- | ------------------ |
| Import function   | `from module import func`                                                                                                                                                                                         | Test functions from another file. | `from name_func import get_name` | Keeps tests separate.                   | Forgetting import. |
| Example test      | `python\nfrom name_func import get_name\n\nclass TestNames(unittest.TestCase):\n    def test_first_last(self):\n        result = get_name('janis', 'joplin')\n        self.assertEqual(result, 'Janis Joplin')\n` | Demonstrates simple test.         | Must run with `unittest.main()`. | Forgetting capitalization expectations. |                    |

---

## 5. Best Practices

* ✅ Prefix all test methods with **`test_`**.
* ✅ Group related tests in one **TestCase class**.
* ✅ Keep test files separate (`test_module.py`).
* ⚠️ Don’t catch exceptions in code under test unless necessary — let tests fail.
* ⚠️ Avoid overly complex tests — keep them clear and focused.

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 11**.

