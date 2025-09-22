Perfect ✅ — here’s your **professional Markdown cheat sheet** for **Pandas**. This one is *full*, like the Streamlit and xlwings ones — covering Series, DataFrames, indexing, selection, I/O, cleaning, reshaping, grouping, merging, time series, and more.

---

# 📘 Pandas Full Cheat Sheet

**Data Analysis with Python**

---

## 1. Setup & Basics

| Command | Syntax                | Explanation     | Notes / Gotchas            |
| ------- | --------------------- | --------------- | -------------------------- |
| Install | `pip install pandas`  | Install pandas. | Often used with NumPy.     |
| Import  | `import pandas as pd` | Standard alias. | Always `pd`.               |
| Version | `pd.__version__`      | Check version.  | Important for API changes. |

---

## 2. Data Structures

### Series (1D)

```python
s = pd.Series([10, 20, 30], index=["a","b","c"])
```

* Like labeled array (1D).
* `.values` → underlying NumPy array.
* `.index` → index labels.

### DataFrame (2D)

```python
df = pd.DataFrame({
    "name": ["Alice","Bob"],
    "age": [25,30]
})
```

* Tabular, 2D labeled data.
* `.columns` → column labels.
* `.index` → row labels.

---

## 3. Import / Export Data

| Format    | Command                           | Notes                               |
| --------- | --------------------------------- | ----------------------------------- |
| CSV       | `pd.read_csv("file.csv")`         | `to_csv("file.csv", index=False)`   |
| Excel     | `pd.read_excel("file.xlsx")`      | Needs `openpyxl` or `xlrd`.         |
| JSON      | `pd.read_json("file.json")`       | `orient="records"` for row-wise.    |
| SQL       | `pd.read_sql(query, conn)`        | Requires `sqlalchemy` or DB driver. |
| Parquet   | `pd.read_parquet("file.parquet")` | Fast, columnar storage.             |
| Clipboard | `pd.read_clipboard()`             | Paste from clipboard.               |
| Pickle    | `pd.read_pickle("file.pkl")`      | Python-native serialization.        |

---

## 4. Viewing Data

| Command  | Syntax          | Explanation             |
| -------- | --------------- | ----------------------- |
| Head     | `df.head(n)`    | First n rows.           |
| Tail     | `df.tail(n)`    | Last n rows.            |
| Shape    | `df.shape`      | (rows, cols).           |
| Info     | `df.info()`     | Columns + types.        |
| Describe | `df.describe()` | Stats for numeric cols. |
| Columns  | `df.columns`    | List of column names.   |
| Index    | `df.index`      | Row index.              |
| Types    | `df.dtypes`     | Column dtypes.          |

---

## 5. Selection & Indexing

| Command         | Syntax                  | Explanation              |
| --------------- | ----------------------- | ------------------------ |
| Column          | `df["col"]` or `df.col` | Single column.           |
| Multiple cols   | `df[["col1","col2"]]`   | Subset of columns.       |
| Row by label    | `df.loc["row"]`         | Label-based selection.   |
| Row by position | `df.iloc[0]`            | Integer index selection. |
| Row + col       | `df.loc[2, "col"]`      | Specific cell.           |
| Slicing         | `df.iloc[0:5]`          | Rows slice.              |
| Conditional     | `df[df["age"] > 30]`    | Boolean filter.          |

---

## 6. Adding & Modifying Data

| Action         | Syntax                                | Explanation       |
| -------------- | ------------------------------------- | ----------------- |
| New col        | `df["new"] = val`                     | Adds column.      |
| Assign         | `df = df.assign(new=df["a"]+df["b"])` | Chainable.        |
| Insert         | `df.insert(1, "new", values)`         | Add at pos.       |
| Rename cols    | `df.rename(columns={"old":"new"})`    | Change col names. |
| Drop col       | `df.drop("col", axis=1)`              | Remove column.    |
| Drop row       | `df.drop(0, axis=0)`                  | Remove row.       |
| Replace values | `df.replace({1:"one"})`               | Replace mapping.  |

---

## 7. Handling Missing Data

| Command      | Syntax                      | Explanation           |
| ------------ | --------------------------- | --------------------- |
| Detect NaN   | `df.isna()`, `df.notna()`   | Boolean mask.         |
| Drop rows    | `df.dropna()`               | Removes NaN rows.     |
| Drop cols    | `df.dropna(axis=1)`         | Removes NaN cols.     |
| Fill         | `df.fillna(0)`              | Replace with value.   |
| Fill fwd/bwd | `df.fillna(method="ffill")` | Fill using prev/next. |

---

## 8. Sorting & Ranking

| Command        | Syntax                  | Explanation      |
| -------------- | ----------------------- | ---------------- |
| Sort by values | `df.sort_values("col")` | Order by column. |
| Sort by index  | `df.sort_index()`       | Order by index.  |
| Rank           | `df["col"].rank()`      | Ranking.         |

---

## 9. Aggregation & Stats

| Command      | Syntax                     | Explanation      |
| ------------ | -------------------------- | ---------------- |
| Sum          | `df.sum()`                 | Column sums.     |
| Mean         | `df.mean()`                | Column means.    |
| Median       | `df.median()`              | Median values.   |
| Count        | `df.count()`               | Non-NaN count.   |
| Value counts | `df["col"].value_counts()` | Frequency table. |
| Unique       | `df["col"].unique()`       | Unique values.   |
| Nunique      | `df["col"].nunique()`      | Count uniques.   |
| Correlation  | `df.corr()`                | Pearson corr.    |

---

## 10. GroupBy

```python
df.groupby("col")["val"].mean()
```

| Command       | Syntax                                       | Explanation        |
| ------------- | -------------------------------------------- | ------------------ |
| Group + agg   | `df.groupby("col").agg({"val":"sum"})`       | Multi agg.         |
| Multiple keys | `df.groupby(["col1","col2"]).mean()`         | Group by multiple. |
| Transform     | `df.groupby("col")["val"].transform("mean")` | Broadcast back.    |

---

## 11. Merging & Joining

| Command     | Syntax                          | Explanation       |
| ----------- | ------------------------------- | ----------------- |
| Concat rows | `pd.concat([df1, df2])`         | Stack vertically. |
| Concat cols | `pd.concat([df1, df2], axis=1)` | Side by side.     |
| Merge       | `pd.merge(df1, df2, on="key")`  | SQL-style join.   |
| Join        | `df1.join(df2, lsuffix="_l")`   | Join by index.    |

---

## 12. Reshaping

| Command     | Syntax                                                          | Explanation       |
| ----------- | --------------------------------------------------------------- | ----------------- |
| Pivot       | `df.pivot(index, columns, values)`                              | Wide reshaping.   |
| Pivot table | `pd.pivot_table(df, values="val", index="col", aggfunc="mean")` | Like Excel pivot. |
| Melt        | `pd.melt(df, id_vars=["id"])`                                   | Wide → long.      |
| Stack       | `df.stack()`                                                    | Columns → rows.   |
| Unstack     | `df.unstack()`                                                  | Rows → columns.   |

---

## 13. Dates & Time Series

| Command     | Syntax                                              | Explanation          |
| ----------- | --------------------------------------------------- | -------------------- |
| Parse dates | `pd.to_datetime(df["date"])`                        | Convert to datetime. |
| Today       | `pd.Timestamp.today()`                              | Current timestamp.   |
| Date range  | `pd.date_range("2024-01-01", periods=10, freq="D")` | Generate dates.      |
| Resample    | `df.resample("M").mean()`                           | Downsample.          |
| Rolling     | `df["val"].rolling(7).mean()`                       | Rolling window.      |

---

## 14. Apply & Map

| Command   | Syntax                         | Explanation               |
| --------- | ------------------------------ | ------------------------- |
| Apply col | `df["col"].apply(func)`        | Apply function to series. |
| Apply DF  | `df.apply(np.sum, axis=1)`     | Row/col-wise apply.       |
| Map       | `df["col"].map({"a":1,"b":2})` | Map values.               |
| Applymap  | `df.applymap(str.upper)`       | Apply elementwise.        |

---

## 15. Exporting

| Command   | Syntax                              | Explanation                    |
| --------- | ----------------------------------- | ------------------------------ |
| CSV       | `df.to_csv("out.csv", index=False)` | Save CSV.                      |
| Excel     | `df.to_excel("out.xlsx")`           | Needs `openpyxl`/`xlsxwriter`. |
| JSON      | `df.to_json("out.json")`            | Save JSON.                     |
| SQL       | `df.to_sql("table", conn)`          | Save to database.              |
| Parquet   | `df.to_parquet("out.parquet")`      | Save parquet.                  |
| Clipboard | `df.to_clipboard()`                 | Copy to clipboard.             |

---

## 16. Best Practices

* ✅ Use `.loc[]` for labels, `.iloc[]` for positions.
* ✅ Avoid chained indexing (`df["col"]["row"]`).
* ✅ Use vectorized ops instead of loops.
* ✅ Use `categorical` dtype for memory efficiency.
* ⚠️ Pandas is **in-memory** — big data may need Dask/Polars.
* ⚠️ `inplace=True` often confusing → prefer reassigning.

---

👉 This cheat sheet now covers **all major Pandas features**: importing, cleaning, transforming, grouping, merging, reshaping, time series, and exporting.

