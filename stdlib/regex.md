

# 📘 Python Regex (`re`) Cheat Sheet

**Pattern Matching, Searching, and Replacing**

---

## 1. Import

```python
import re
```

---

## 2. Core Functions

| Function             | Example                                | Use                     |
| -------------------- | -------------------------------------- | ----------------------- |
| `re.match(p, s)`     | `re.match(r"\d+","123abc")`            | Match at start only     |
| `re.search(p, s)`    | `re.search(r"\d+","abc123")`           | First match anywhere    |
| `re.findall(p, s)`   | `re.findall(r"\d+","a1b22")`           | All matches as list     |
| `re.finditer(p, s)`  | `for m in re.finditer(r"\d+","a1b22")` | Iterator of matches     |
| `re.split(p, s)`     | `re.split(r"\W+","a,b;c")`             | Split by pattern        |
| `re.sub(p,r,s)`      | `re.sub(r"\d","#","a1b2")` → `"a#b#"`  | Replace matches         |
| `re.fullmatch(p, s)` | `re.fullmatch(r"\d+","123")`           | Whole string must match |
| `re.compile(p)`      | `pat = re.compile(r"\d+")`             | Pre-compiled pattern    |

---

## 3. Special Characters

| Symbol | Meaning                  | Example              |       |       |
| ------ | ------------------------ | -------------------- | ----- | ----- |
| `.`    | Any char except newline  | `a.c` → `abc`, `axc` |       |       |
| `^`    | Start of string          | `^Hello`             |       |       |
| `$`    | End of string            | `world$`             |       |       |
| `[]`   | Character set            | `[aeiou]`            |       |       |
| `[^]`  | Negated set              | `[^0-9]`             |       |       |
| `\d`   | Digit `[0-9]`            |                      |       |       |
| `\D`   | Non-digit                |                      |       |       |
| `\w`   | Word char `[A-Za-z0-9_]` |                      |       |       |
| `\W`   | Non-word                 |                      |       |       |
| `\s`   | Whitespace               |                      |       |       |
| `\S`   | Non-whitespace           |                      |       |       |
| \`     | \`                       | OR                   | \`cat | dog\` |

---

## 4. Quantifiers

| Symbol  | Meaning         | Example                        |
| ------- | --------------- | ------------------------------ |
| `*`     | 0 or more       | `ab*` → `a`, `abbb`            |
| `+`     | 1 or more       | `ab+` → `ab`, `abbbb`          |
| `?`     | 0 or 1          | `colou?r` → `color` / `colour` |
| `{n}`   | Exactly n       | `\d{3}` → `123`                |
| `{n,}`  | n or more       | `\d{2,}`                       |
| `{n,m}` | Between n and m | `\d{2,4}`                      |

---

## 5. Groups & References

| Syntax          | Example            | Use                 |
| --------------- | ------------------ | ------------------- |
| `()`            | `(abc)+`           | Capture group       |
| `(?: )`         | `(?:abc)+`         | Non-capturing group |
| `(?P<name>...)` | `(?P<year>\d{4})`  | Named group         |
| `\1`, `\2`      | `(ab)c\1`          | Backreference       |
| `(?P=name)`     | `(?P<word>\w+) \1` | Named backref       |

---

## 6. Lookarounds

| Syntax     | Example       | Meaning             |
| ---------- | ------------- | ------------------- |
| `(?=...)`  | `\d+(?=USD)`  | Positive lookahead  |
| `(?!...)`  | `\d+(?!USD)`  | Negative lookahead  |
| `(?<=...)` | `(?<=USD)\d+` | Positive lookbehind |
| `(?<!...)` | `(?<!USD)\d+` | Negative lookbehind |

---

## 7. Flags

| Flag    | Example                           | Meaning     |                |
| ------- | --------------------------------- | ----------- | -------------- |
| `re.I`  | `re.search(r"abc","ABC",re.I)`    | Ignore case |                |
| `re.M`  | `^` and `$` match per line        |             |                |
| `re.S`  | `.` matches newline too           |             |                |
| `re.X`  | Allow verbose regex with comments |             |                |
| Combine | \`re.I                            | re.M\`      | Multiple flags |

---

## 8. Common Patterns

| Task              | Pattern                                             | Example              |
| ----------------- | --------------------------------------------------- | -------------------- |
| Email             | `r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"` | `test@mail.com`      |
| URL               | `r"https?://\S+"`                                   | `http://example.com` |
| Phone             | `r"\+?\d{10,15}"`                                   | `+1234567890`        |
| Date (YYYY-MM-DD) | `r"\d{4}-\d{2}-\d{2}"`                              | `2025-09-21`         |

---

## 9. Beginner Pitfalls

* ❌ Forgetting raw strings: use `r"pattern"` not `"pattern"`.
* ❌ Overusing `.*` → greedy, may capture too much. Use `.*?` for lazy.
* ❌ Using `match()` when you need `search()`.
* ❌ Forgetting to escape special chars → use `\.` for literal `.`.

---

✅ With this, you have the **full regex toolkit**: functions, operators, quantifiers, groups, lookarounds, flags, and patterns.

