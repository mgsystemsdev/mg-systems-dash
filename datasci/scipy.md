



# 📘 Python SciPy Cheat Sheet

**Scientific Computing Toolkit**

---

## 1. Importing

```python
import numpy as np
from scipy import linalg, optimize, stats, integrate, fft, signal
```

---

## 2. Linear Algebra (`scipy.linalg`)

| Function            | Example                      | Use |
| ------------------- | ---------------------------- | --- |
| `linalg.inv(A)`     | Inverse of a matrix          |     |
| `linalg.det(A)`     | Determinant                  |     |
| `linalg.solve(A,b)` | Solve Ax = b                 |     |
| `linalg.eig(A)`     | Eigenvalues & eigenvectors   |     |
| `linalg.svd(A)`     | Singular Value Decomposition |     |

---

## 3. Optimization (`scipy.optimize`)

| Function                    | Example                 | Use |
| --------------------------- | ----------------------- | --- |
| `optimize.minimize(f,x0)`   | Minimize function       |     |
| `optimize.root(f,x0)`       | Solve equation `f(x)=0` |     |
| `optimize.curve_fit(f,x,y)` | Fit curve to data       |     |

---

## 4. Integration (`scipy.integrate`)

| Function                         | Example         | Use |
| -------------------------------- | --------------- | --- |
| `integrate.quad(f,a,b)`          | Single integral |     |
| `integrate.dblquad(f,a,b,g1,g2)` | Double integral |     |
| `integrate.odeint(f,y0,t)`       | Solve ODEs      |     |

---

## 5. Statistics (`scipy.stats`)

### Probability Distributions

```python
from scipy import stats

stats.norm.pdf(0)     # density at x=0
stats.norm.cdf(1.96)  # cumulative prob
stats.norm.rvs(size=5)  # random samples
```

Common distributions: `norm`, `binom`, `poisson`, `uniform`, `chi2`, `t`.

### Statistical Tests

| Test                       | Example                   | Use |
| -------------------------- | ------------------------- | --- |
| `stats.ttest_ind(a,b)`     | Independent t-test        |     |
| `stats.ttest_rel(a,b)`     | Paired t-test             |     |
| `stats.chisquare(obs,exp)` | Chi-square test           |     |
| `stats.pearsonr(x,y)`      | Pearson correlation       |     |
| `stats.spearmanr(x,y)`     | Spearman rank correlation |     |

---

## 6. Fourier Transforms (`scipy.fft`)

```python
from scipy import fft

x = np.array([1,2,3,4])
fft_vals = fft.fft(x)
ifft_vals = fft.ifft(fft_vals)
```

---

## 7. Signal Processing (`scipy.signal`)

| Function                  | Example             | Use |
| ------------------------- | ------------------- | --- |
| `signal.convolve(x,y)`    | Convolution         |     |
| `signal.correlate(x,y)`   | Correlation         |     |
| `signal.find_peaks(data)` | Find peaks          |     |
| `signal.spectrogram(sig)` | Compute spectrogram |     |
| `signal.butter(N,Wn)`     | Butterworth filter  |     |

---

## 8. Spatial & Distance (`scipy.spatial`)

| Function                          | Example            | Use |
| --------------------------------- | ------------------ | --- |
| `spatial.distance.euclidean(u,v)` | Euclidean distance |     |
| `spatial.distance.cosine(u,v)`    | Cosine distance    |     |
| `spatial.KDTree(data)`            | Nearest neighbors  |     |

---

## 9. Interpolation (`scipy.interpolate`)

```python
from scipy import interpolate

x = np.linspace(0,10,10)
y = np.sin(x)
f = interpolate.interp1d(x,y,kind="cubic")
f(5.5)   # interpolated value
```

---

## 10. Beginner Pitfalls

* ❌ Forgetting SciPy builds on **NumPy** — convert lists to arrays first.
* ❌ Using `numpy.linalg` when you need `scipy.linalg` for more advanced features.
* ❌ Confusing `optimize.minimize` (continuous) vs `optimize.root` (equations).
* ❌ Not checking distribution assumptions before applying `stats` tests.

---

✅ With this, you now have the **SciPy essentials**: linear algebra, optimization, integration, stats, FFT, signal, spatial, interpolation.

