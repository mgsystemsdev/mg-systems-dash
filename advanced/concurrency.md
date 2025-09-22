
---

# 📘 Python Concurrency Cheat Sheet

**Threads • Processes • Async IO**

---

## 1. Threading (Lightweight, Shared Memory)

```python
import threading, time

def worker():
    print("Worker running")
    time.sleep(1)

t = threading.Thread(target=worker)
t.start()
t.join()
```

| Key                            | Notes                      |
| ------------------------------ | -------------------------- |
| `Thread(target=func, args=())` | Start a new thread         |
| `t.start()`                    | Begin execution            |
| `t.join()`                     | Wait until thread finishes |
| `threading.Lock()`             | Prevent race conditions    |
| `threading.Event()`            | Signal between threads     |

✅ Best for: I/O-bound tasks (networking, file I/O).
❌ Not great for CPU-heavy tasks (GIL bottleneck).

---

## 2. Multiprocessing (True Parallelism)

```python
from multiprocessing import Process, Queue, Pool

def worker(x): return x*x

if __name__ == "__main__":
    p = Process(target=worker, args=(5,))
    p.start(); p.join()
```

### Using a Pool

```python
with Pool(4) as pool:
    results = pool.map(worker, [1,2,3,4])
```

| Key                    | Notes                        |
| ---------------------- | ---------------------------- |
| `Process(target=func)` | Run in new process           |
| `Queue()`              | Share data between processes |
| `Pool(n)`              | Manage worker pool           |
| `pool.map(func, data)` | Parallel map                 |

✅ Best for: CPU-bound tasks (math, ML, crunching).
❌ Overhead is higher than threading.

---

## 3. AsyncIO (Single Threaded, Event Loop)

```python
import asyncio

async def worker(n):
    print(f"Start {n}")
    await asyncio.sleep(1)
    print(f"End {n}")

async def main():
    await asyncio.gather(worker(1), worker(2))

asyncio.run(main())
```

| Feature                 | Notes                          |
| ----------------------- | ------------------------------ |
| `async def`             | Define coroutine               |
| `await`                 | Pause until awaitable is ready |
| `asyncio.gather()`      | Run tasks concurrently         |
| `asyncio.create_task()` | Schedule task                  |
| `asyncio.Queue()`       | Async-safe queue               |

✅ Best for: high-concurrency I/O (web requests, sockets).
❌ Not for CPU-heavy work.

---

## 4. Mixing Concurrency

* **Threads inside asyncio**:

  ```python
  loop = asyncio.get_event_loop()
  await loop.run_in_executor(None, blocking_func)
  ```
* **Processes inside asyncio**: Use `ProcessPoolExecutor`.

---

## 5. Choosing the Right Tool

| Use Case                             | Best Choice              |
| ------------------------------------ | ------------------------ |
| Web scraping, file I/O, requests     | `threading` or `asyncio` |
| Parallel computation, CPU crunching  | `multiprocessing`        |
| Real-time networking (sockets, APIs) | `asyncio`                |
| Background jobs, signals             | Threads or async tasks   |

---

## 6. Beginner Pitfalls

* ❌ Forgetting `join()` → zombie threads/processes.
* ❌ Blocking call in `asyncio` (use `await` or run in executor).
* ❌ Using `threading` for CPU-heavy → GIL prevents true parallelism.
* ❌ Passing unpicklable objects to `multiprocessing`.

---

✅ With this, you have the **Concurrency Essentials**:

* **Threading** → lightweight, I/O tasks.
* **Multiprocessing** → true parallelism, CPU-heavy tasks.
* **AsyncIO** → scalable I/O, event-driven apps.

---

