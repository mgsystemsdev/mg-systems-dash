
# 📘 Matplotlib Full Cheat Sheet

**Data Visualization in Python**

---

## 1. Setup & Basics

| Command          | Syntax                            | Explanation          |
| ---------------- | --------------------------------- | -------------------- |
| Install          | `pip install matplotlib`          | Install library.     |
| Import pyplot    | `import matplotlib.pyplot as plt` | Standard alias.      |
| Inline (Jupyter) | `%matplotlib inline`              | Display in notebook. |
| Style            | `plt.style.use("ggplot")`         | Change plot style.   |

---

## 2. Creating Figures

| Command           | Syntax                        | Explanation         |
| ----------------- | ----------------------------- | ------------------- |
| Basic plot        | `plt.plot(x,y)`               | Line plot.          |
| Show              | `plt.show()`                  | Render plot.        |
| Figure            | `fig = plt.figure()`          | Create empty fig.   |
| Subplots          | `fig, ax = plt.subplots()`    | Create fig + axes.  |
| Multiple subplots | `fig, ax = plt.subplots(2,2)` | Grid of plots.      |
| Adjust size       | `plt.figure(figsize=(8,6))`   | Set width × height. |

---

## 3. Plot Types

| Plot             | Syntax                             | Explanation             |
| ---------------- | ---------------------------------- | ----------------------- |
| Line             | `plt.plot(x,y)`                    | Basic line chart.       |
| Scatter          | `plt.scatter(x,y)`                 | Points.                 |
| Bar              | `plt.bar(x,height)`                | Vertical bars.          |
| Barh             | `plt.barh(y,width)`                | Horizontal bars.        |
| Histogram        | `plt.hist(data, bins=20)`          | Frequency distribution. |
| Pie              | `plt.pie(data, labels=labels)`     | Pie chart.              |
| Stack plot       | `plt.stackplot(x,y1,y2,...)`       | Area stack.             |
| Fill between     | `plt.fill_between(x,y1,y2)`        | Shade region.           |
| Boxplot          | `plt.boxplot(data)`                | Quartiles & outliers.   |
| Violin           | `plt.violinplot(data)`             | Distribution shape.     |
| Error bar        | `plt.errorbar(x,y,yerr=err)`       | With error.             |
| Heatmap (imshow) | `plt.imshow(data, cmap="viridis")` | Display 2D array.       |
| Contour          | `plt.contour(X,Y,Z)`               | Contour lines.          |
| Quiver           | `plt.quiver(X,Y,U,V)`              | Vector field.           |
| Streamplot       | `plt.streamplot(X,Y,U,V)`          | Flow lines.             |

---

## 4. Axes Methods

When using `ax = plt.subplots()`:

| Method     | Syntax                                      | Explanation  |
| ---------- | ------------------------------------------- | ------------ |
| Line       | `ax.plot(x,y)`                              | Same as plt. |
| Scatter    | `ax.scatter(x,y)`                           | —            |
| Set labels | `ax.set_xlabel("X")` / `ax.set_ylabel("Y")` | Axis labels. |
| Title      | `ax.set_title("Title")`                     | Title.       |
| Limits     | `ax.set_xlim(min,max)`                      | Axis limits. |
| Grid       | `ax.grid(True)`                             | Show grid.   |
| Legend     | `ax.legend()`                               | Add legend.  |

---

## 5. Formatting & Styling

| Command         | Syntax                             | Explanation        |
| --------------- | ---------------------------------- | ------------------ |
| Color           | `plt.plot(x,y,color="red")`        | Color by name/hex. |
| Linestyle       | `plt.plot(x,y,linestyle="--")`     | Dashed line.       |
| Marker          | `plt.plot(x,y,marker="o")`         | Point marker.      |
| Linewidth       | `plt.plot(x,y,linewidth=2)`        | Thickness.         |
| Alpha           | `plt.plot(x,y,alpha=0.5)`          | Transparency.      |
| Multiple series | `plt.plot(x1,y1,"r--",x2,y2,"bo")` | Multiple styles.   |

---

## 6. Legends & Annotations

| Command    | Syntax                                                       | Explanation   |
| ---------- | ------------------------------------------------------------ | ------------- |
| Label data | `plt.plot(x,y,label="data")`                                 | Named plot.   |
| Legend     | `plt.legend(loc="upper left")`                               | Add legend.   |
| Text       | `plt.text(x,y,"Hello")`                                      | Add text.     |
| Annotate   | `plt.annotate("Peak", xy=(x,y), xytext=(..), arrowprops={})` | Arrow labels. |

---

## 7. Ticks & Axes Control

| Command      | Syntax                          | Explanation       |
| ------------ | ------------------------------- | ----------------- |
| X/Y ticks    | `plt.xticks(ticks,labels)`      | Custom ticks.     |
| Log scale    | `plt.xscale("log")`             | Logarithmic axis. |
| Invert axis  | `plt.gca().invert_yaxis()`      | Flip axis.        |
| Aspect ratio | `plt.gca().set_aspect("equal")` | Equal scaling.    |

---

## 8. Images

| Command    | Syntax                             | Explanation             |
| ---------- | ---------------------------------- | ----------------------- |
| Show image | `plt.imshow(img)`                  | Display 2D array/image. |
| Colormap   | `plt.imshow(img,cmap="gray")`      | Apply colormap.         |
| Colorbar   | `plt.colorbar()`                   | Add scale legend.       |
| Save fig   | `plt.savefig("plot.png", dpi=300)` | Save as file.           |

---

## 9. Multiple Plots & Layouts

| Command      | Syntax                                     | Explanation          |
| ------------ | ------------------------------------------ | -------------------- |
| Subplot      | `plt.subplot(2,2,1)`                       | 2×2 grid, 1st plot.  |
| Subplots     | `fig, ax = plt.subplots(2,2)`              | More flexible.       |
| Share axes   | `fig, ax = plt.subplots(2,sharex=True)`    | Shared x.            |
| Tight layout | `plt.tight_layout()`                       | Auto adjust spacing. |
| GridSpec     | `from matplotlib.gridspec import GridSpec` | Complex layouts.     |

---

## 10. 3D Plots

```python
from mpl_toolkits.mplot3d import Axes3D
ax = plt.figure().add_subplot(111, projection="3d")
```

| Plot       | Syntax                                  |
| ---------- | --------------------------------------- |
| 3D line    | `ax.plot3D(x,y,z)`                      |
| 3D scatter | `ax.scatter3D(x,y,z)`                   |
| Surface    | `ax.plot_surface(X,Y,Z,cmap="viridis")` |
| Wireframe  | `ax.plot_wireframe(X,Y,Z)`              |
| Contour    | `ax.contour3D(X,Y,Z,50,cmap="cool")`    |

---

## 11. Config & Utilities

| Command          | Syntax                                 | Explanation         |
| ---------------- | -------------------------------------- | ------------------- |
| Global params    | `plt.rcParams["figure.figsize"]=(8,6)` | Change defaults.    |
| Styles           | `plt.style.available`                  | List themes.        |
| Interactive mode | `plt.ion()`, `plt.ioff()`              | Toggle interactive. |
| Close            | `plt.close()`                          | Close current fig.  |

---

## 12. Best Practices

* ✅ Use **object-oriented API** (`fig, ax = plt.subplots()`) instead of `plt.plot()`.
* ✅ Save figures with high DPI for reports.
* ✅ Use `tight_layout()` to avoid overlaps.
* ⚠️ Large datasets → prefer scatter with alpha for clarity.
* ⚠️ Don’t forget `plt.show()` when running scripts.

---

👉 This cheat sheet covers **all major Matplotlib features**: basic plots, formatting, axes, legends, images, multiple subplots, 3D, and saving.

