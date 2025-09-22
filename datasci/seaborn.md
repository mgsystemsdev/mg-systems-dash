

# 📘 Seaborn Full Cheat Sheet

**Statistical Data Visualization in Python**

---

## 1. Setup & Basics

| Command       | Syntax                            | Explanation           |
| ------------- | --------------------------------- | --------------------- |
| Install       | `pip install seaborn`             | Installs Seaborn.     |
| Import        | `import seaborn as sns`           | Standard alias.       |
| Version       | `sns.__version__`                 | Check version.        |
| Built-in data | `sns.get_dataset_names()`         | List sample datasets. |
| Load data     | `df = sns.load_dataset("tips")`   | Example dataset.      |
| Theme         | `sns.set_theme(style="darkgrid")` | Global style.         |

---

## 2. Relational Plots

| Plot       | Syntax                                                          | Explanation                |
| ---------- | --------------------------------------------------------------- | -------------------------- |
| Scatter    | `sns.scatterplot(x="x", y="y", data=df)`                        | Basic scatter plot.        |
| Line       | `sns.lineplot(x="x", y="y", data=df)`                           | Line plot with CI shading. |
| Relational | `sns.relplot(x="x", y="y", hue="col", data=df, kind="scatter")` | Facet grid scatter/line.   |

---

## 3. Categorical Plots

| Plot    | Syntax                                               | Explanation           |
| ------- | ---------------------------------------------------- | --------------------- |
| Strip   | `sns.stripplot(x="cat", y="val", data=df)`           | Jittered dots.        |
| Swarm   | `sns.swarmplot(x="cat", y="val", data=df)`           | Non-overlapping dots. |
| Bar     | `sns.barplot(x="cat", y="val", data=df)`             | Show mean + CI.       |
| Count   | `sns.countplot(x="cat", data=df)`                    | Count of categories.  |
| Box     | `sns.boxplot(x="cat", y="val", data=df)`             | Quartiles + outliers. |
| Violin  | `sns.violinplot(x="cat", y="val", data=df)`          | KDE + boxplot hybrid. |
| Point   | `sns.pointplot(x="cat", y="val", data=df)`           | Means + error bars.   |
| Catplot | `sns.catplot(x="cat", y="val", data=df, kind="bar")` | Multi-type cat plots. |

---

## 4. Distribution Plots

| Plot                  | Syntax                                             | Explanation                          |
| --------------------- | -------------------------------------------------- | ------------------------------------ |
| Histogram             | `sns.histplot(data=df["col"], bins=20)`            | Histogram.                           |
| KDE                   | `sns.kdeplot(data=df["col"], fill=True)`           | Kernel density estimate.             |
| Distplot (deprecated) | `sns.distplot(df["col"])`                          | Old API, use histplot/kdeplot.       |
| ECDF                  | `sns.ecdfplot(data=df["col"])`                     | Empirical CDF.                       |
| Rug                   | `sns.rugplot(data=df["col"])`                      | Small ticks along axis.              |
| Jointplot             | `sns.jointplot(x="x", y="y", data=df, kind="hex")` | Scatter + marginal histograms.       |
| Pairplot              | `sns.pairplot(df)`                                 | Matrix of scatter/hist for all vars. |

---

## 5. Regression Plots

| Plot       | Syntax                                         | Explanation             |
| ---------- | ---------------------------------------------- | ----------------------- |
| Regression | `sns.regplot(x="x", y="y", data=df)`           | Fit regression line.    |
| LMPlot     | `sns.lmplot(x="x", y="y", data=df, hue="cat")` | Regression with facets. |
| Residual   | `sns.residplot(x="x", y="y", data=df)`         | Residual analysis.      |

---

## 6. Matrix / Heatmap Plots

| Plot       | Syntax                                                     | Explanation              |
| ---------- | ---------------------------------------------------------- | ------------------------ |
| Heatmap    | `sns.heatmap(data=df.corr(), annot=True, cmap="coolwarm")` | Correlation heatmap.     |
| Clustermap | `sns.clustermap(df, cmap="viridis")`                       | Heatmap with clustering. |

---

## 7. Faceting (Multiple Plots)

| Command   | Syntax                                                                                                           | Explanation              |
| --------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Relplot   | `sns.relplot(..., col="sex", row="time")`                                                                        | Facet grid scatter/line. |
| Catplot   | `sns.catplot(..., col="day")`                                                                                    | Facet categorical plots. |
| FacetGrid | `python\ng = sns.FacetGrid(df, col="sex")\ng.map(sns.histplot, "age")`                                           | Custom facet control.    |
| PairGrid  | `python\ng = sns.PairGrid(df)\ng.map_upper(sns.scatterplot)\ng.map_lower(sns.kdeplot)\ng.map_diag(sns.histplot)` | Fine-grained matrix.     |

---

## 8. Styling & Customization

| Command       | Syntax                             | Explanation                             |
| ------------- | ---------------------------------- | --------------------------------------- |
| Set theme     | `sns.set_theme(style="whitegrid")` | Styles: white, dark, ticks.             |
| Color palette | `sns.color_palette("pastel")`      | Built-in palettes.                      |
| Set palette   | `sns.set_palette("muted")`         | Global palette.                         |
| Context       | `sns.set_context("talk")`          | Context: paper, notebook, talk, poster. |
| Axes style    | `sns.set_style("ticks")`           | Change axes appearance.                 |
| Despine       | `sns.despine()`                    | Remove top/right spines.                |

---

## 9. Integration with Matplotlib

* All Seaborn plots return **Matplotlib Axes**.
* You can chain Matplotlib commands:

```python
ax = sns.histplot(df["col"])
ax.set_title("Distribution")
ax.set_xlabel("Values")
ax.set_ylabel("Frequency")
```

---

## 10. Best Practices

* ✅ Use **Seaborn for high-level plots** (distributions, categories, regression).
* ✅ Use **Matplotlib for fine control** (annotations, custom layouts).
* ✅ Use `pairplot` for quick EDA.
* ⚠️ Large datasets → prefer `histplot` with `binwidth` or `kdeplot` with `bw_adjust`.
* ⚠️ Regression plots assume linear fit unless specified.

---

👉 This cheat sheet now covers **all major Seaborn features**: relational, categorical, distribution, regression, matrix plots, styling, and integration.

