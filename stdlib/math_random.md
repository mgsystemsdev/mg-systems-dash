
# 📘 Python `math` & `random` Cheat Sheet

**Numerical Computations & Randomization**

---

## 1. Importing

```python
import math
import random
```

---

## 2. Math Module (`math`)

### Constants

| Constant   | Example      | Value          |
| ---------- | ------------ | -------------- |
| `math.pi`  | `3.14159...` | π              |
| `math.e`   | `2.71828...` | Euler’s number |
| `math.inf` | Infinity     | `float("inf")` |
| `math.nan` | Not-a-Number | `float("nan")` |

### Basic Functions

| Function            | Example             | Result |
| ------------------- | ------------------- | ------ |
| `math.sqrt(x)`      | `math.sqrt(16)`     | `4.0`  |
| `math.pow(x,y)`     | `math.pow(2,3)`     | `8.0`  |
| `math.ceil(x)`      | `math.ceil(3.2)`    | `4`    |
| `math.floor(x)`     | `math.floor(3.9)`   | `3`    |
| `math.trunc(x)`     | `math.trunc(-3.7)`  | `-3`   |
| `math.fabs(x)`      | `math.fabs(-5)`     | `5.0`  |
| `math.factorial(x)` | `math.factorial(5)` | `120`  |

### Logarithms

| Function            | Example             | Result      |
| ------------------- | ------------------- | ----------- |
| `math.log(x)`       | `math.log(10)`      | Natural log |
| `math.log(x, base)` | `math.log(100, 10)` | Base-10 log |
| `math.log10(x)`     | `math.log10(1000)`  | `3.0`       |
| `math.log2(x)`      | `math.log2(8)`      | `3.0`       |

### Trigonometry

| Function          | Example                         | Notes           |
| ----------------- | ------------------------------- | --------------- |
| `math.sin(x)`     | `math.sin(math.pi/2)` → `1.0`   | x in radians    |
| `math.cos(x)`     | `math.cos(0)` → `1.0`           |                 |
| `math.tan(x)`     | `math.tan(math.pi/4)` → `1.0`   |                 |
| `math.asin(x)`    | `math.asin(1)` → `π/2`          | Inverse sine    |
| `math.acos(x)`    | `math.acos(0)` → `π/2`          | Inverse cosine  |
| `math.atan(x)`    | `math.atan(1)` → `π/4`          | Inverse tangent |
| `math.degrees(x)` | `math.degrees(math.pi)` → `180` | Rad → deg       |
| `math.radians(x)` | `math.radians(180)` → `π`       | Deg → rad       |

---

## 3. Random Module (`random`)

### Basic Usage

| Function                     | Example                    | Result         |
| ---------------------------- | -------------------------- | -------------- |
| `random.random()`            | `0.374...`                 | Float ∈ \[0,1) |
| `random.uniform(a,b)`        | `random.uniform(1,5)`      | Float ∈ \[1,5] |
| `random.randint(a,b)`        | `random.randint(1,6)`      | Int ∈ \[1,6]   |
| `random.randrange(a,b,step)` | `random.randrange(0,10,2)` | Even int 0–8   |

### Choice & Sampling

| Function                   | Example                        | Result              |
| -------------------------- | ------------------------------ | ------------------- |
| `random.choice(seq)`       | `random.choice(["a","b","c"])` | One element         |
| `random.choices(seq, k=3)` | `random.choices("ABC",k=3)`    | With replacement    |
| `random.sample(seq, k)`    | `random.sample(range(10),3)`   | Without replacement |
| `random.shuffle(list)`     | `random.shuffle(deck)`         | Shuffles in place   |

### State Control

| Function                 | Example             | Purpose    |
| ------------------------ | ------------------- | ---------- |
| `random.seed(42)`        | Reproducible output | Set seed   |
| `random.getstate()`      | Returns RNG state   | Save state |
| `random.setstate(state)` | Restore RNG state   | Load state |

### Distributions

| Function                            | Example     | Distribution |
| ----------------------------------- | ----------- | ------------ |
| `random.betavariate(a,b)`           | Beta        |              |
| `random.expovariate(lmbd)`          | Exponential |              |
| `random.gammavariate(a,b)`          | Gamma       |              |
| `random.gauss(mu,sigma)`            | Gaussian    |              |
| `random.normalvariate(mu,sigma)`    | Normal      |              |
| `random.lognormvariate(mu,sigma)`   | Log-normal  |              |
| `random.triangular(low,high,mode)`  | Triangular  |              |
| `random.vonmisesvariate(mu,kappa)`  | Circular    |              |
| `random.paretovariate(alpha)`       | Pareto      |              |
| `random.weibullvariate(alpha,beta)` | Weibull     |              |

---

## 4. Beginner Pitfalls

* ❌ `math.pow()` vs `**`: use `**` for speed, `math.pow` always returns float.
* ❌ `random.random()` ∈ \[0,1), never 1.
* ❌ Forgetting to set a **seed** for reproducible results.
* ❌ Using `random` for **cryptography** — use `secrets` instead.

---

✅ With this, you have the **full toolkit for math & random** in Python: constants, trig/logs, distributions, RNG control, and pitfalls.

