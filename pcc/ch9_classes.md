
# 📘 Python Crash Course – Chapter 9

**Classes Cheat Sheet**

---

## 1. Defining a Class

| Command / Concept | Syntax                     | Explanation                              | Example                                                                         | Notes / Gotchas                 | Beginner Pitfalls     |
| ----------------- | -------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------- | --------------------- |
| Basic class       | `class ClassName:`         | Creates a new class.                     | `python\nclass Dog:\n    pass\n`                                                | Class names use **CamelCase**.  | Forgetting colon `:`. |
| `__init__` method | `def __init__(self, ...):` | Runs automatically when creating object. | `python\nclass Dog:\n    def __init__(self, name):\n        self.name = name\n` | `self` must be first parameter. | Forgetting `self`.    |

---

## 2. Creating Instances (Objects)

| Command / Concept | Syntax                     | Explanation                | Example               | Notes / Gotchas                     | Beginner Pitfalls                   |
| ----------------- | -------------------------- | -------------------------- | --------------------- | ----------------------------------- | ----------------------------------- |
| Instantiate       | `object = ClassName(args)` | Creates object from class. | `my_dog = Dog("Rex")` | Calls `__init__`.                   | Forgetting parentheses.             |
| Access attribute  | `object.attribute`         | Reads instance data.       | `print(my_dog.name)`  | Attributes are tied to each object. | Using class name instead of object. |

---

## 3. Methods

| Command / Concept | Syntax              | Explanation                  | Example                                                             | Notes / Gotchas        | Beginner Pitfalls                |
| ----------------- | ------------------- | ---------------------------- | ------------------------------------------------------------------- | ---------------------- | -------------------------------- |
| Instance method   | `def method(self):` | Defines behavior for object. | `python\nclass Dog:\n    def bark(self):\n        print("Woof!")\n` | Always include `self`. | Forgetting `self` → error.       |
| Calling method    | `object.method()`   | Executes behavior.           | `my_dog.bark()`                                                     | Must call on object.   | Calling on class without object. |

---

## 4. Working with Attributes

| Command / Concept           | Syntax                    | Explanation                     | Example          | Notes / Gotchas           | Beginner Pitfalls                  |
| --------------------------- | ------------------------- | ------------------------------- | ---------------- | ------------------------- | ---------------------------------- |
| Set attribute in `__init__` | `self.attr = value`       | Defines attribute at creation.  | `self.age = age` | Instance-specific.        | Forgetting `self.`.                |
| Modify attribute directly   | `object.attr = new_value` | Updates value.                  | `my_dog.age = 3` | Updates only this object. | Thinking it updates all objects.   |
| Default values              | `self.attr = fixed_value` | Same value for all new objects. | `self.age = 0`   | Still instance-specific.  | Expecting it to auto-update later. |

---

## 5. Inheritance

| Command / Concept | Syntax                      | Explanation                    | Example                                                                                              | Notes / Gotchas                | Beginner Pitfalls                    |
| ----------------- | --------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------ |
| Subclass          | `class Child(Parent):`      | Inherits attributes & methods. | `python\nclass ElectricCar(Car):\n    pass\n`                                                        | Parent must be in parentheses. | Forgetting to pass parent.           |
| `super()`         | `super().__init__(args)`    | Calls parent’s `__init__`.     | `python\nclass ElectricCar(Car):\n    def __init__(self, brand):\n        super().__init__(brand)\n` | Use to extend parent behavior. | Forgetting `super()`.                |
| Override method   | Define same method in child | Replaces parent’s version.     | `def fill_gas(self): print("No gas needed!")`                                                        | Child takes priority.          | Forgetting to call parent if needed. |

---

## 6. Importing Classes

| Command / Concept    | Syntax                     | Explanation      | Example                          | Notes / Gotchas                         | Beginner Pitfalls                      |
| -------------------- | -------------------------- | ---------------- | -------------------------------- | --------------------------------------- | -------------------------------------- |
| From module          | `from module import Class` | Imports class.   | `from car import Car`            | File must exist in same dir or package. | Forgetting `.py` extension not needed. |
| Import entire module | `import module`            | Use with prefix. | `import car; my_car = car.Car()` | Keeps namespace clear.                  | Forgetting prefix when calling.        |

---

## 7. Best Practices

* ✅ Use **CamelCase** for class names, `snake_case` for methods/variables.
* ✅ Keep classes focused on **one responsibility**.
* ✅ Use `super()` properly in subclasses.
* ⚠️ Always include `self` in instance methods.
* ⚠️ Don’t confuse **class** (blueprint) with **instance** (object).

---

👉 This cheat sheet now covers **all key commands, syntax, and pitfalls from Chapter 9**.
