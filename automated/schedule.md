Here’s your **professional Markdown cheat sheet** for **Schedule & Time Automation in Python** — using `time`, `datetime`, and `schedule`.

---

# 📘 Python Schedule & Time Automation Cheat Sheet

**Delays, Scheduling, and Timing Tasks**

---

## 1. `time` Module (Delays & Sleep)

```python
import time

time.sleep(5)          # pause for 5 seconds
print(time.time())     # current epoch time
print(time.ctime())    # human-readable time
```

---

## 2. `datetime` Module (Date & Time Handling)

```python
from datetime import datetime, timedelta

now = datetime.now()                   # current time
print(now.strftime("%Y-%m-%d %H:%M"))  # format
future = now + timedelta(days=7)       # 1 week later
```

| Format Code | Meaning       |
| ----------- | ------------- |
| `%Y`        | Year (2025)   |
| `%m`        | Month (01–12) |
| `%d`        | Day (01–31)   |
| `%H`        | Hour (00–23)  |
| `%M`        | Minute        |
| `%S`        | Second        |

---

## 3. `schedule` Module (Task Scheduling)

### Install

```bash
pip install schedule
```

### Usage

```python
import schedule, time

def job():
    print("Task running!")

schedule.every(10).seconds.do(job)
schedule.every().minute.do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().monday.at("12:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## 4. `threading.Timer` (Run Later, Once)

```python
from threading import Timer

def hello():
    print("Hello after 5 seconds")

t = Timer(5.0, hello)
t.start()
```

---

## 5. Cron-like Scheduling (`APScheduler`)

```bash
pip install apscheduler
```

```python
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job("interval", minutes=1)
def timed_job():
    print("Runs every 1 min")

@sched.scheduled_job("cron", day_of_week="mon", hour=7)
def scheduled_job():
    print("Every Monday 7am")

sched.start()
```

---

## 6. Beginner Pitfalls

* ❌ Using `time.sleep()` in web apps → blocks everything. Use async or schedulers instead.
* ❌ Forgetting `while True` loop when using `schedule`.
* ❌ Relying only on `schedule` for production → better use `cron` or `APScheduler`.
* ❌ Mixing naive `datetime` with timezone-aware → use `pytz` or `zoneinfo`.

---

✅ With this, you have **full coverage of Python time automation**:

* `time` → delays
* `datetime` → date math
* `schedule` → simple jobs
* `Timer` → delayed one-shot
* `APScheduler` → cron-like advanced scheduling

---

