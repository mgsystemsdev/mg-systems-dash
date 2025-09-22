# 📘 NumPy Full Cheat Sheet

**Scientific Computing with Python**

---

## 1. Setup & Basics

| Command | Syntax               | Explanation     | Notes               |
| ------- | -------------------- | --------------- | ------------------- |
| Install | `pip install numpy`  | Installs NumPy. | Often preinstalled. |
| Import  | `import numpy as np` | Standard alias. | Always use `np.`.   |
| Version | `np.__version__`     | Check version.  | —                   |

---

## 2. Creating Arrays

| Method         | Syntax                 | Explanation              |
| -------------- | ---------------------- | ------------------------ |
| From list      | `np.array([1,2,3])`    | Create from Python list. |
| Zeros          | `np.zeros((2,3))`      | 2×3 array of zeros.      |
| Ones           | `np.ones((2,3))`       | Array of ones.           |
| Full           | `np.full((2,3), 7)`    | Fill with constant.      |
| Empty          | `np.empty((2,3))`      | Uninitialized.           |
| Arange         | `np.arange(0,10,2)`    | Like `range()`.          |
| Linspace       | `np.linspace(0,1,5)`   | Evenly spaced numbers.   |
| Random uniform | `np.random.rand(2,3)`  | \[0,1) uniform.          |
| Random normal  | `np.random.randn(2,3)` | Normal dist.             |
| Identity       | `np.eye(3)`            | Identity matrix.         |

---

## 3. Array Attributes

| Attribute | Syntax         | Explanation        |
| --------- | -------------- | ------------------ |
| Shape     | `arr.shape`    | Dimensions.        |
| Size      | `arr.size`     | Total elements.    |
| Dtype     | `arr.dtype`    | Data type.         |
| Ndim      | `arr.ndim`     | Number of dims.    |
| Itemsize  | `arr.itemsize` | Bytes per element. |

---

## 4. Indexing & Slicing

| Command | Syntax             | Explanation          |
| ------- | ------------------ | -------------------- |
| Element | `arr[0,1]`         | Row 0 col 1.         |
| Slice   | `arr[0:2, :]`      | Rows 0–1, all cols.  |
| Step    | `arr[::2]`         | Every 2nd element.   |
| Boolean | `arr[arr>5]`       | Filter by condition. |
| Fancy   | `arr[[0,2],[1,3]]` | Index arrays.        |

---

## 5. Reshaping

| Command     | Syntax                    | Explanation   |
| ----------- | ------------------------- | ------------- |
| Reshape     | `arr.reshape(2,6)`        | Change shape. |
| Flatten     | `arr.ravel()`             | 1D view.      |
| Transpose   | `arr.T`                   | Flip axes.    |
| Concatenate | `np.concatenate([a,b])`   | Join arrays.  |
| Stack       | `np.stack([a,b], axis=0)` | Add new dim.  |
| Split       | `np.split(arr,3)`         | Split into 3. |

---

## 6. Math Operations

| Operation | Syntax         | Explanation        |
| --------- | -------------- | ------------------ |
| Add       | `arr+5`        | Element-wise.      |
| Subtract  | `arr-2`        | —                  |
| Multiply  | `arr*3`        | —                  |
| Divide    | `arr/2`        | —                  |
| Power     | `arr**2`       | Square.            |
| Exp       | `np.exp(arr)`  | Exponential.       |
| Sqrt      | `np.sqrt(arr)` | Square root.       |
| Log       | `np.log(arr)`  | Natural log.       |
| Trig      | `np.sin(arr)`  | Works elementwise. |

---

## 7. Aggregations

| Command       | Syntax                   | Explanation       |
| ------------- | ------------------------ | ----------------- |
| Sum           | `arr.sum()`              | All elements.     |
| Axis sum      | `arr.sum(axis=0)`        | Per column.       |
| Mean          | `arr.mean()`             | Average.          |
| Median        | `np.median(arr)`         | Median.           |
| Std           | `arr.std()`              | Std dev.          |
| Min/Max       | `arr.min()`, `arr.max()` | Extremes.         |
| Argmin/Argmax | `arr.argmin()`           | Index of min/max. |

---

## 8. Linear Algebra

| Command     | Syntax                      | Explanation          |
| ----------- | --------------------------- | -------------------- |
| Dot         | `np.dot(a,b)`               | Dot product.         |
| Matmul      | `a @ b` or `np.matmul(a,b)` | Matrix multiply.     |
| Inverse     | `np.linalg.inv(a)`          | Matrix inverse.      |
| Determinant | `np.linalg.det(a)`          | Determinant.         |
| Eigenvalues | `np.linalg.eig(a)`          | Eigenvalues/vectors. |
| Solve       | `np.linalg.solve(a,b)`      | Solve Ax=b.          |

---

## 9. Random Module

| Command | Syntax                         | Explanation       |
| ------- | ------------------------------ | ----------------- |
| Uniform | `np.random.rand(3)`            | \[0,1) random.    |
| Normal  | `np.random.randn(3)`           | Normal dist.      |
| Ints    | `np.random.randint(0,10,5)`    | Random ints.      |
| Choice  | `np.random.choice([1,2,3], 2)` | Random sample.    |
| Shuffle | `np.random.shuffle(arr)`       | In-place shuffle. |
| Seed    | `np.random.seed(42)`           | Reproducibility.  |

---

## 10. Broadcasting

* **Rule:** Smaller array stretches to match larger array shape.

Example:

```python
a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
a+b
# shape (3,3)
```

---

## 11. File I/O

| Command       | Syntax                                      | Explanation         |
| ------------- | ------------------------------------------- | ------------------- |
| Save binary   | `np.save("arr.npy", arr)`                   | Save `.npy`.        |
| Load binary   | `arr = np.load("arr.npy")`                  | Load `.npy`.        |
| Save text     | `np.savetxt("arr.csv", arr, delimiter=",")` | Save CSV.           |
| Load text     | `np.loadtxt("arr.csv", delimiter=",")`      | Read CSV.           |
| Save multiple | `np.savez("file.npz", a=a, b=b)`            | Compressed archive. |

---

## 12. Useful Functions

| Command | Syntax                   | Explanation       |
| ------- | ------------------------ | ----------------- |
| Unique  | `np.unique(arr)`         | Unique values.    |
| Sort    | `np.sort(arr)`           | Sorted copy.      |
| Argsort | `np.argsort(arr)`        | Indices for sort. |
| Clip    | `np.clip(arr,0,1)`       | Bound values.     |
| Where   | `np.where(arr>0,1,0)`    | Conditional.      |
| Any/All | `arr.any()`, `arr.all()` | Boolean checks.   |

---

## 13. Best Practices

* ✅ Use vectorized NumPy ops, not Python loops.
* ✅ Preallocate arrays for speed.
* ✅ Use `astype()` to control dtypes.
* ✅ Set random seeds for reproducibility.
* ⚠️ NumPy arrays are fixed-size — resizing copies data.
* ⚠️ Watch for broadcasting mistakes.

---

👉 This cheat sheet now covers **all major NumPy features**: creation, indexing, math, aggregations, linear algebra, random, broadcasting, file I/O, and utilities.
