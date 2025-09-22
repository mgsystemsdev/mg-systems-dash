

---

# 📘 Python Typing Cheat Sheet

**Type Hints & Generics for Safer Code**

---

## 1. Basic Type Hints

```python
def add(x: int, y: int) -> int:
    return x + y
```

| Type    | Example                |
| ------- | ---------------------- |
| `int`   | `x: int = 5`           |
| `float` | `pi: float = 3.14`     |
| `str`   | `name: str = "Miguel"` |
| `bool`  | `done: bool = True`    |
| `bytes` | `b: bytes = b"hi"`     |

---

## 2. Built-in Collections

```python
from typing import List, Dict, Tuple, Set, Optional
```

| Type               | Example        |
| ------------------ | -------------- |
| `List[int]`        | `[1, 2, 3]`    |
| `Tuple[str, int]`  | `("a", 1)`     |
| `Dict[str, float]` | `{"pi": 3.14}` |
| `Set[str]`         | `{"a", "b"}`   |
| `Optional[int]`    | `int or None`  |

---

## 3. Union Types

```python
from typing import Union

def parse(x: Union[int, str]) -> str:
    return str(x)
```

Python 3.10+ shortcut:

```python
def parse(x: int | str) -> str:
    return str(x)
```

---

## 4. Callable (Functions as Types)

```python
from typing import Callable

def apply(fn: Callable[[int, int], int], a: int, b: int) -> int:
    return fn(a, b)
```

---

## 5. Any & NoReturn

```python
from typing import Any, NoReturn

def debug(x: Any) -> None: ...
def fail(msg: str) -> NoReturn:
    raise RuntimeError(msg)
```

---

## 6. Type Aliases

```python
UserId = int
Score = float

def get_score(user: UserId) -> Score:
    return 98.5
```

---

## 7. Generics

```python
from typing import TypeVar, Generic

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]
```

Custom Generic Class:

```python
class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
```

---

## 8. Protocols (Duck Typing)

```python
from typing import Protocol

class Flyable(Protocol):
    def fly(self) -> None: ...

class Bird:
    def fly(self): print("Flap")

def takeoff(obj: Flyable):
    obj.fly()
```

---

## 9. TypedDict (JSON-like Data)

```python
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str

user: User = {"id": 1, "name": "Alice"}
```

---

## 10. Literal Types

```python
from typing import Literal

def move(direction: Literal["left","right"]) -> None:
    ...
```

---

## 11. Type Checking Tools

* **Static checkers**:

  * `mypy file.py`
  * `pyright file.py`

* **Runtime checking (optional)**:

  ```python
  from typeguard import typechecked

  @typechecked
  def square(x: int) -> int:
      return x * x
  ```

---

## 12. Beginner Pitfalls

* ❌ Thinking type hints enforce types → they’re **hints only**, not runtime checks.
* ❌ Forgetting to use `Optional` when `None` is possible.
* ❌ Overusing `Any` → defeats purpose of typing.
* ❌ Forgetting Python 3.9+ supports `list[int]` instead of `List[int]`.

---

✅ With this, you have the **full Typing toolkit**: hints, unions, callables, generics, protocols, and TypedDicts.

---

