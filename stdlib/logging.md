

# 📘 Python Logging Cheat Sheet

**Tracking Program Behavior & Errors**

---

## 1. Basic Setup

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Debugging info")
logging.info("General info")
logging.warning("Something might be wrong")
logging.error("An error occurred")
logging.critical("Critical failure")
```

---

## 2. Logging Levels

| Level    | Method               | Value | Use                               |
| -------- | -------------------- | ----- | --------------------------------- |
| DEBUG    | `logging.debug()`    | 10    | Detailed info (dev only).         |
| INFO     | `logging.info()`     | 20    | General events.                   |
| WARNING  | `logging.warning()`  | 30    | Unexpected but not fatal.         |
| ERROR    | `logging.error()`    | 40    | Errors that stop part of program. |
| CRITICAL | `logging.critical()` | 50    | Severe errors, program may stop.  |

---

## 3. Formatting Messages

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
```

| Placeholder     | Meaning     |
| --------------- | ----------- |
| `%(asctime)s`   | Timestamp   |
| `%(levelname)s` | Log level   |
| `%(message)s`   | Log text    |
| `%(name)s`      | Logger name |
| `%(filename)s`  | File name   |
| `%(lineno)d`    | Line number |

---

## 4. Logging to File

```python
logging.basicConfig(
    filename="app.log",
    filemode="a",  # overwrite "w" or append "a"
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

---

## 5. Custom Logger

```python
logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("myapp.log")
ch = logging.StreamHandler()

formatter = logging.Formatter("%(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info("Custom logger setup complete")
```

---

## 6. Advanced Features

* **Exception logging**

```python
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division failed")
```

Includes full traceback automatically.

* **Rotating log files**

```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=3)
logger.addHandler(handler)
```

* **Timed rotation**

```python
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler("timed.log", when="midnight", interval=1, backupCount=7)
logger.addHandler(handler)
```

---

## 7. Beginner Pitfalls

* ❌ Using `print()` instead of `logging` (no levels/formatting).
* ❌ Forgetting `basicConfig()` before logging → default WARN only.
* ❌ Not setting handlers properly → duplicate logs.
* ❌ Using `logging.debug()` but level set too high → nothing shows.

---

✅ With this, you have the **complete logging reference**: levels, formatting, file logging, custom loggers, rotation, and exception handling.

