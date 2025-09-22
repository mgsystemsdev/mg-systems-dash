

# 📘 Python CSV & JSON Cheat Sheet

**Working with Data Formats**

---

## 1. CSV (Comma-Separated Values)

### Reading CSV

```python
import csv

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

* `csv.reader` → returns rows as lists.

```python
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

* `csv.DictReader` → rows as dicts (keys = header row).

---

### Writing CSV

```python
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age"])
    writer.writerows([["Alice",30],["Bob",25]])
```

* `writerow()` → one row.
* `writerows()` → multiple rows.

```python
with open("out.csv","w",newline="") as f:
    fieldnames = ["name","age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name":"Alice","age":30})
```

* `DictWriter` → write rows as dicts.

---

### Common Options

| Option                | Example                              | Use              |
| --------------------- | ------------------------------------ | ---------------- |
| `delimiter=";"`       | `csv.reader(f, delimiter=";")`       | Custom separator |
| `quotechar='"'`       | `csv.reader(f, quotechar='"')`       | Quoting style    |
| `lineterminator="\n"` | `csv.writer(f, lineterminator="\n")` | Line ending      |

---

## 2. JSON (JavaScript Object Notation)

### Reading JSON

```python
import json

with open("data.json") as f:
    data = json.load(f)   # from file
```

```python
s = '{"name":"Alice","age":30}'
data = json.loads(s)      # from string
```

---

### Writing JSON

```python
with open("out.json","w") as f:
    json.dump(data,f)   # write to file
```

```python
s = json.dumps(data)     # convert to string
```

---

### Options

| Option               | Example                                | Use                |
| -------------------- | -------------------------------------- | ------------------ |
| `indent=2`           | `json.dumps(data, indent=2)`           | Pretty print       |
| `sort_keys=True`     | `json.dumps(data, sort_keys=True)`     | Ordered keys       |
| `ensure_ascii=False` | `json.dumps(data, ensure_ascii=False)` | Keep Unicode chars |

---

## 3. Common Patterns

* **CSV → JSON**

```python
import csv, json

with open("data.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("out.json","w") as f:
    json.dump(data,f,indent=2)
```

* **JSON → CSV**

```python
with open("data.json") as f:
    data = json.load(f)

with open("out.csv","w",newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
```

---

## 4. Beginner Pitfalls

* ❌ Forgetting `newline=""` when writing CSV (extra blank lines on Windows).
* ❌ Assuming `json.load()` can handle comments — JSON standard doesn’t allow them.
* ❌ Using `json.dumps()` without `indent` → unreadable one-liner.
* ❌ Forgetting to open files in **text mode (`"r"`, `"w"`)** not binary.

---

✅ With this, you have the **full CSV & JSON toolkit**: reading, writing, options, conversions, and pitfalls.

