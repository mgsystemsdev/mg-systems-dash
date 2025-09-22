

# 📘 Python File I/O Cheat Sheet

**Reading, Writing & Managing Files**

---

## 1. Opening Files

```python
f = open("file.txt", "r")
```

| Mode   | Meaning                               |
| ------ | ------------------------------------- |
| `"r"`  | Read (default), error if file missing |
| `"w"`  | Write (overwrite if exists)           |
| `"x"`  | Create new file, error if exists      |
| `"a"`  | Append (add to end)                   |
| `"b"`  | Binary mode (e.g. `"rb"`)             |
| `"t"`  | Text mode (default)                   |
| `"r+"` | Read & write                          |

⚠️ Always prefer **`with open(...) as f`** to auto-close files.

---

## 2. Reading Files

```python
with open("file.txt", "r") as f:
    data = f.read()
```

| Method        | Example          | Result               |
| ------------- | ---------------- | -------------------- |
| `read()`      | `f.read()`       | Entire file (string) |
| `read(n)`     | `f.read(5)`      | First 5 chars        |
| `readline()`  | `f.readline()`   | One line             |
| `readlines()` | `f.readlines()`  | List of lines        |
| Iterate       | `for line in f:` | Line by line         |

---

## 3. Writing Files

```python
with open("file.txt", "w") as f:
    f.write("Hello\n")
```

| Method         | Example                       | Result                 |
| -------------- | ----------------------------- | ---------------------- |
| `write()`      | `f.write("Hi")`               | Writes string          |
| `writelines()` | `f.writelines(["a\n","b\n"])` | Writes list of strings |

---

## 4. File Position

```python
f = open("file.txt","r")
f.read(3)        # reads 3 chars
f.tell()         # position in file
f.seek(0)        # move back to start
```

---

## 5. Working with Binary Files

```python
with open("image.png","rb") as f:
    data = f.read()

with open("copy.png","wb") as f:
    f.write(data)
```

---

## 6. File Utilities (`os`, `shutil`, `pathlib`)

```python
import os, shutil
os.rename("old.txt","new.txt")   # rename
os.remove("file.txt")            # delete
os.path.exists("file.txt")       # check existence
shutil.copy("a.txt","b.txt")     # copy
shutil.move("a.txt","dir/")      # move
```

Modern alternative: **`pathlib`**

```python
from pathlib import Path
p = Path("file.txt")
p.exists()
p.read_text()
p.write_text("content")
```

---

## 7. Exception Handling

```python
try:
    with open("nofile.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File missing")
```

---

## 8. Beginner Pitfalls

* ❌ Forgetting to close file → leaks → use `with`.
* ❌ Using `w` when you meant `a` (overwrites file).
* ❌ Not handling encoding properly (`open(..., encoding="utf-8")`).
* ❌ Using `read()` on huge files → prefer iteration.

---

✅ With this, you now have the **full File I/O reference**: open/read/write, binary, seek/tell, and utilities with `os`/`pathlib`.

