

# 📘 Python Argparse Cheat Sheet

**Command-Line Argument Parsing**

---

## 1. Basic Setup

```python
import argparse

parser = argparse.ArgumentParser(description="Example CLI")
parser.add_argument("name")   # positional argument
args = parser.parse_args()

print(f"Hello {args.name}")
```

```bash
python app.py Miguel
# → Hello Miguel
```

---

## 2. Positional Arguments

```python
parser.add_argument("input_file")
parser.add_argument("output_file")
```

* Required by order.
* Access with `args.input_file`.

---

## 3. Optional Arguments (Flags)

```python
parser.add_argument("-v","--verbose", action="store_true")
parser.add_argument("-o","--output", type=str, help="Output file")
```

| Action        | Example       | Effect                             |
| ------------- | ------------- | ---------------------------------- |
| `store`       | `-o file.txt` | Stores value (default).            |
| `store_true`  | `-v`          | Boolean flag → True if present.    |
| `store_false` | `--no-cache`  | Boolean flag → False if present.   |
| `append`      | `-t py -t js` | Collect multiple values in a list. |

---

## 4. Data Types & Validation

```python
parser.add_argument("--count", type=int)
parser.add_argument("--ratio", type=float)
parser.add_argument("--choices", choices=["low","med","high"])
```

* Converts automatically.
* Invalid input → automatic error message.

---

## 5. Default Values

```python
parser.add_argument("--level", default="info")
```

---

## 6. Argument Groups

```python
group = parser.add_argument_group("authentication")
group.add_argument("--user")
group.add_argument("--password")
```

* Organizes help output.

---

## 7. Mutually Exclusive Arguments

```python
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--fast", action="store_true")
group.add_argument("--slow", action="store_true")
```

* User must pick **one option only**.

---

## 8. Subcommands

```python
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("x", type=int)
add_parser.add_argument("y", type=int)

remove_parser = subparsers.add_parser("remove")
remove_parser.add_argument("id")
```

```bash
python app.py add 2 3
python app.py remove 42
```

---

## 9. Parsing Known Args

```python
args, extras = parser.parse_known_args()
```

* Useful if your script passes extra args to another program.

---

## 10. Customizing Help

```python
parser = argparse.ArgumentParser(
    description="My CLI Tool",
    epilog="Example: python app.py -v input.txt"
)
```

* Auto-generates `-h/--help`.
* Customize with description, epilog, argument help.

---

## 11. Beginner Pitfalls

* ❌ Forgetting to call `parse_args()`.
* ❌ Not setting `dest` → args get confusing names.
* ❌ Using positional args when optional flags would be clearer.
* ❌ Overloading with too many flags without grouping or subcommands.

---

✅ With this, you have the **complete Argparse toolkit**: positional, optional, flags, choices, groups, subcommands, and best practices.

