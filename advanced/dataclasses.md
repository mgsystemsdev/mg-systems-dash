
---

# 📘 Python Dataclasses Cheat Sheet

**Simplify Class Creation**

---

## 1. Basic Usage

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    active: bool = True

u = User(1, "Alice")
print(u)   # User(id=1, name='Alice', active=True)
```

* Auto-generates `__init__`, `__repr__`, `__eq__`, etc.

---

## 2. Default Values & Factories

```python
from dataclasses import field

@dataclass
class Post:
    tags: list[str] = field(default_factory=list)  # avoids mutable default
```

---

## 3. Field Options

```python
@dataclass
class Product:
    id: int
    name: str
    price: float = 0.0
    _hidden: str = field(repr=False, default="secret")  # exclude from __repr__
    temp: int = field(init=False, default=42)          # not in __init__
```

| Option             | Use                          |
| ------------------ | ---------------------------- |
| `default=`         | Static default value         |
| `default_factory=` | Callable for dynamic default |
| `init=False`       | Exclude from constructor     |
| `repr=False`       | Hide from `__repr__`         |
| `compare=False`    | Ignore in comparisons        |
| `kw_only=True`     | Force keyword-only argument  |

---

## 4. Ordering & Comparison

```python
@dataclass(order=True)
class Point:
    x: int
    y: int
```

* Auto-adds `<`, `<=`, `>`, `>=` based on field order.

---

## 5. Frozen Dataclasses (Immutable)

```python
@dataclass(frozen=True)
class Config:
    debug: bool
```

* Fields cannot be reassigned.
* Hashable → usable as dict keys.

---

## 6. Post-Init Processing

```python
@dataclass
class Circle:
    radius: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = 3.14 * self.radius**2
```

---

## 7. Inheritance

```python
@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str
```

---

## 8. Utility Functions

```python
from dataclasses import asdict, astuple, replace

asdict(u)     # {'id': 1, 'name': 'Alice', 'active': True}
astuple(u)    # (1, 'Alice', True)
replace(u, active=False)  # new instance with change
```

---

## 9. Slots for Memory Efficiency (3.10+)

```python
@dataclass(slots=True)
class Pixel:
    x: int
    y: int
```

---

## 10. Beginner Pitfalls

* ❌ Using mutable defaults (`tags=[]`) → always use `default_factory`.
* ❌ Forgetting `frozen=True` if immutability is required.
* ❌ Assuming dataclasses handle validation automatically → must use `__post_init__`.
* ❌ Using with methods requiring `__hash__` → only safe if `frozen=True`.

---

✅ With this, you have the **complete dataclasses toolkit**: defaults, factories, frozen, ordering, post-init, inheritance, and utilities.

---
