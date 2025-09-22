

# 📘 Python Date & Time Cheat Sheet

**Working with Dates, Times & Formatting**

---

## 1. Importing

```python
import datetime
from datetime import date, time, datetime, timedelta
```

---

## 2. Current Date & Time

```python
from datetime import datetime, date

now = datetime.now()     # Current date + time
today = date.today()     # Current date
utc_now = datetime.utcnow() # Current UTC time
```

---

## 3. Creating Dates & Times

```python
d = date(2025, 9, 21)           # year, month, day
t = time(14, 30, 45)            # hour, minute, second
dt = datetime(2025, 9, 21, 14, 30, 45)  # full datetime
```

---

## 4. Accessing Components

```python
dt.year      # 2025
dt.month     # 9
dt.day       # 21
dt.hour      # 14
dt.minute    # 30
dt.second    # 45
dt.weekday() # 0=Monday ... 6=Sunday
```

---

## 5. Formatting Dates

```python
dt.strftime("%Y-%m-%d %H:%M:%S")
# "2025-09-21 14:30:45"
```

| Code | Meaning        | Example   |
| ---- | -------------- | --------- |
| `%Y` | Year (4-digit) | 2025      |
| `%y` | Year (2-digit) | 25        |
| `%m` | Month (01–12)  | 09        |
| `%B` | Month name     | September |
| `%d` | Day (01–31)    | 21        |
| `%A` | Weekday name   | Sunday    |
| `%H` | Hour (24h)     | 14        |
| `%I` | Hour (12h)     | 02        |
| `%p` | AM/PM          | PM        |
| `%M` | Minutes        | 30        |
| `%S` | Seconds        | 45        |

---

## 6. Parsing Strings → Dates

```python
dt = datetime.strptime("2025-09-21 14:30", "%Y-%m-%d %H:%M")
```

---

## 7. Date Arithmetic

```python
from datetime import timedelta

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

---

## 8. Comparing Dates

```python
d1 = date(2025, 9, 21)
d2 = date(2025, 9, 25)

d1 < d2   # True
d2 - d1   # timedelta(days=4)
```

---

## 9. Timezones (Python 3.9+)

```python
from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)
```

For advanced TZ handling → use `pytz` or `zoneinfo`.

---

## 10. Beginner Pitfalls

* ❌ Confusing `datetime.now()` (local) vs `datetime.utcnow()`.
* ❌ Forgetting to handle **timezones** when comparing times.
* ❌ Using `strftime`/`strptime` with wrong format codes.
* ❌ Mixing `date` and `datetime` objects in arithmetic.

---

✅ With this, you now have the **complete Date & Time reference**: creation, formatting, parsing, arithmetic, and timezones.

