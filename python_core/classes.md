
# 📘 Python Classes Cheat Sheet

**Object-Oriented Programming (OOP) in Python**

---

## 1. Defining a Class

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
```

```python
d = Dog("Fido")
d.bark()   # Fido says woof!
```

---

## 2. Class Components

| Part                | Example               | Explanation              |
| ------------------- | --------------------- | ------------------------ |
| Constructor         | `__init__(self, …)`   | Runs at object creation. |
| Instance attributes | `self.name`           | Unique per object.       |
| Methods             | `def bark(self): ...` | Functions inside class.  |
| Class attributes    | `species = "Canine"`  | Shared by all instances. |

---

## 3. Attribute Access

| Command         | Example                      | Result                  |
| --------------- | ---------------------------- | ----------------------- |
| Get             | `d.name`                     | `"Fido"`                |
| Set             | `d.age = 3`                  | Adds/changes attribute. |
| Delete          | `del d.age`                  | Removes attribute.      |
| Check           | `hasattr(d,"name")`          | `True`                  |
| Get w/ default  | `getattr(d,"age",0)`         | `0`                     |
| Set dynamically | `setattr(d,"color","brown")` | Adds `color`.           |

---

## 4. Class vs Instance Attributes

```python
class Dog:
    species = "Canine"    # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

* `Dog.species` → `"Canine"`
* `d = Dog("Fido"); d.species` → `"Canine"`

⚠️ If you assign `d.species = "Wolf"`, it overrides only for that object.

---

## 5. Methods

| Type            | Example                       | Notes                  |
| --------------- | ----------------------------- | ---------------------- |
| Instance method | `def bark(self):`             | Works on object data.  |
| Class method    | `@classmethod def info(cls):` | Works on class itself. |
| Static method   | `@staticmethod def util():`   | Independent helper.    |

---

## 6. Inheritance

```python
class Animal:
    def speak(self): print("Generic sound")

class Dog(Animal):
    def speak(self): print("Woof!")
```

* `Dog` inherits from `Animal`.
* `super().method()` calls parent version.

---

## 7. Multiple Inheritance

```python
class A: pass
class B: pass
class C(A,B): pass
```

Python uses **MRO (Method Resolution Order)** to determine lookup.

---

## 8. Special / Magic Methods

| Method                  | Example            | Purpose          |
| ----------------------- | ------------------ | ---------------- |
| `__init__`              | `__init__(self,…)` | Constructor      |
| `__str__`               | `str(obj)`         | Human-readable   |
| `__repr__`              | `repr(obj)`        | Debug output     |
| `__len__`               | `len(obj)`         | Custom length    |
| `__getitem__`           | `obj[key]`         | Indexing         |
| `__setitem__`           | `obj[key]=val`     | Assigning        |
| `__iter__`              | `for x in obj:`    | Iteration        |
| `__call__`              | `obj()`            | Callable objects |
| `__eq__`, `__lt__`      | Comparisons        | Sorting/equality |
| `__enter__`, `__exit__` | Context manager    | `with obj:`      |

---

## 9. Data Classes (Python ≥3.7)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

* Auto-generates `__init__`, `__repr__`, `__eq__`, etc.
* Great for storing structured data.

---

## 10. Beginner Pitfalls

* ❌ Forgetting `self` in method definitions.
* ❌ Mixing up class vs instance attributes.
* ❌ Using mutable default attributes (`def __init__(self, x=[])`).
* ❌ Overusing inheritance instead of composition.
* ❌ Not implementing `__repr__` → debugging harder.

---

✅ This cheat sheet covers **everything about Python classes**: defining, attributes, methods, inheritance, magic methods, and dataclasses.

