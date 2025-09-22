Here’s your **professional Markdown cheat sheet** for **OpenPyXL (Excel automation in Python)** — full reference style, like we did for Streamlit.

---

# 📘 OpenPyXL Cheat Sheet

**Work with Excel files (`.xlsx`) in Python**

---

## 1. Setup & Basics

| Command / Concept | Syntax                                | Explanation             | Notes / Gotchas                      |
| ----------------- | ------------------------------------- | ----------------------- | ------------------------------------ |
| Install           | `pip install openpyxl`                | Installs OpenPyXL.      | Only works with `.xlsx`, not `.xls`. |
| Import            | `import openpyxl as oxl`              | Standard import.        | You can also import submodules.      |
| Load workbook     | `wb = oxl.load_workbook("file.xlsx")` | Open existing workbook. | File must exist.                     |
| Create workbook   | `wb = oxl.Workbook()`                 | New blank workbook.     | Starts with one sheet.               |
| Save workbook     | `wb.save("file.xlsx")`                | Saves to file.          | Must call to persist changes.        |

---

## 2. Worksheets

| Command           | Syntax                    | Explanation                  | Notes / Gotchas        |
| ----------------- | ------------------------- | ---------------------------- | ---------------------- |
| Active sheet      | `ws = wb.active`          | Gets currently active sheet. | Default first sheet.   |
| Get sheet by name | `ws = wb["Sheet1"]`       | Access by name.              | Use exact name.        |
| Sheet names       | `wb.sheetnames`           | List all sheet names.        | Useful for navigation. |
| Create sheet      | `wb.create_sheet("Data")` | Adds new sheet.              | Appends by default.    |
| Remove sheet      | `wb.remove(ws)`           | Deletes sheet.               | Cannot undo.           |
| Rename sheet      | `ws.title = "NewName"`    | Change sheet name.           | Must be unique.        |

---

## 3. Cells

| Command       | Syntax                                   | Explanation            | Notes / Gotchas                            |
| ------------- | ---------------------------------------- | ---------------------- | ------------------------------------------ |
| Access cell   | `ws["A1"]` or `ws.cell(row=1, column=1)` | Get single cell.       | Both notations valid.                      |
| Get value     | `ws["A1"].value`                         | Read cell contents.    | Returns `None` if empty.                   |
| Set value     | `ws["A1"].value = "Hello"`               | Write to cell.         | Strings, numbers, formulas supported.      |
| Iterate rows  | `for row in ws.iter_rows(): ...`         | Iterate row-wise.      | Use `values_only=True` to get just values. |
| Iterate cols  | `for col in ws.iter_cols(): ...`         | Iterate col-wise.      | —                                          |
| Max rows/cols | `ws.max_row`, `ws.max_column`            | Highest row/col index. | May include empty cells.                   |

---

## 4. Ranges & Slicing

| Command      | Syntax        | Explanation        | Notes / Gotchas        |
| ------------ | ------------- | ------------------ | ---------------------- |
| Cell range   | `ws["A1:C3"]` | 2D slice of cells. | Returns tuple of rows. |
| Row range    | `ws["2:5"]`   | Rows 2–5.          | Entire row(s).         |
| Column range | `ws["A:C"]`   | Columns A–C.       | Entire column(s).      |

---

## 5. Formatting

| Command       | Syntax                                                                                                                    | Explanation       | Notes / Gotchas              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------------------- |
| Font          | `python\nfrom openpyxl.styles import Font\nws["A1"].font = Font(bold=True, color="FF0000")\n`                             | Style text.       | Must import `Font`.          |
| Fill          | `python\nfrom openpyxl.styles import PatternFill\nws["A1"].fill = PatternFill(fill_type="solid", fgColor="FFFF00")\n`     | Background color. | Hex color codes.             |
| Alignment     | `python\nfrom openpyxl.styles import Alignment\nws["A1"].alignment = Alignment(horizontal="center", vertical="center")\n` | Text alignment.   | Horizontal + vertical.       |
| Border        | `python\nfrom openpyxl.styles import Border, Side\nws["A1"].border = Border(left=Side(style="thin"))\n`                   | Cell borders.     | Must define each side.       |
| Number format | `ws["A1"].number_format = "0.00%"`                                                                                        | Format numbers.   | Same as Excel custom format. |

---

## 6. Formulas

| Command        | Syntax                                           | Explanation                              | Notes / Gotchas                     |
| -------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------- |
| Insert formula | `ws["B2"].value = "=SUM(A1:A10)"`                | Adds Excel formula.                      | Evaluated inside Excel, not Python. |
| Read formula   | `ws["B2"].value`                                 | Returns `=SUM(...)`.                     | Does not calculate result.          |
| Data only      | `oxl.load_workbook("file.xlsx", data_only=True)` | Load cached results instead of formulas. | Useful for reading outputs.         |

---

## 7. Merging & Freezing

| Command      | Syntax                      | Explanation      | Notes / Gotchas               |
| ------------ | --------------------------- | ---------------- | ----------------------------- |
| Merge        | `ws.merge_cells("A1:D1")`   | Combines cells.  | Keeps top-left value.         |
| Unmerge      | `ws.unmerge_cells("A1:D1")` | Reverts merge.   | —                             |
| Freeze panes | `ws.freeze_panes = "B2"`    | Locks rows/cols. | `"B2"` freezes row 1 & col A. |

---

## 8. Charts

| Command        | Syntax                                                              | Explanation              | Notes / Gotchas                             |
| -------------- | ------------------------------------------------------------------- | ------------------------ | ------------------------------------------- |
| Import         | `from openpyxl.chart import BarChart, Reference`                    | Required for charts.     | Charts are objects.                         |
| Reference data | `data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=10)` | Define chart data range. | Needs worksheet + bounds.                   |
| Create chart   | `chart = BarChart(); chart.add_data(data, titles_from_data=True)`   | Creates bar chart.       | Many chart types: LineChart, PieChart, etc. |
| Add to sheet   | `ws.add_chart(chart, "E5")`                                         | Places chart at cell.    | Only visible in Excel.                      |

---

## 9. Named Ranges & Validation

| Command         | Syntax                                                                                                                                                                        | Explanation                 | Notes / Gotchas                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ----------------------------------- |
| Named range     | `wb.create_named_range("myrange", ws, "A1:A10")`                                                                                                                              | Defines a name for a range. | Access via `wb.defined_names`.      |
| Data validation | `python\nfrom openpyxl.worksheet.datavalidation import DataValidation\ndv = DataValidation(type="list", formula1='"Yes,No"')\nws.add_data_validation(dv)\ndv.add(ws["A1"])\n` | Adds dropdown validation.   | Can validate numbers, dates, lists. |

---

## 10. Best Practices

* ✅ Always call `wb.save()` after making changes.
* ✅ Use `values_only=True` in `iter_rows()` for cleaner iteration.
* ✅ Style with `openpyxl.styles` for fonts, fills, alignment.
* ✅ Use formulas for Excel-calculated fields; OpenPyXL does not compute them.
* ⚠️ Avoid repeatedly saving/reading large workbooks → performance hit.
* ⚠️ Remember: only `.xlsx` is supported (not `.xls`).

---



---

---

# 📘 xlwings Cheat Sheet

**Control Excel from Python (Windows & macOS)**

---

## 1. Setup & Basics

| Command / Concept | Syntax                      | Explanation                  | Notes / Gotchas                            |
| ----------------- | --------------------------- | ---------------------------- | ------------------------------------------ |
| Install           | `pip install xlwings`       | Installs xlwings.            | Works with Excel installed (not headless). |
| Import            | `import xlwings as xw`      | Standard alias.              | Always use `xw.` prefix.                   |
| New workbook      | `wb = xw.Book()`            | Opens blank Excel workbook.  | Auto-launches Excel app.                   |
| Open workbook     | `wb = xw.Book("file.xlsx")` | Opens existing file.         | Path must exist.                           |
| Active workbook   | `xw.books.active`           | Gets current Excel workbook. | Useful when one open.                      |
| Save workbook     | `wb.save("newname.xlsx")`   | Saves file.                  | Without path → overwrite.                  |
| Close workbook    | `wb.close()`                | Closes file.                 | Can `save()` before closing.               |

---

## 2. Worksheets

| Command      | Syntax                      | Explanation           | Notes / Gotchas             |
| ------------ | --------------------------- | --------------------- | --------------------------- |
| Active sheet | `sht = wb.sheets.active`    | Get active sheet.     | —                           |
| By name      | `sht = wb.sheets["Sheet1"]` | Select sheet by name. | Case-sensitive.             |
| New sheet    | `wb.sheets.add("MySheet")`  | Add new sheet.        | Default to end of workbook. |
| Rename       | `sht.name = "Data"`         | Rename sheet.         | Must be unique.             |
| Delete       | `sht.delete()`              | Removes sheet.        | Cannot undo.                |
| All sheets   | `wb.sheets`                 | List of sheets.       | Can iterate.                |

---

## 3. Ranges & Cells

| Command        | Syntax                                 | Explanation           | Notes / Gotchas                        |
| -------------- | -------------------------------------- | --------------------- | -------------------------------------- |
| Single cell    | `sht.range("A1")`                      | Get cell object.      | —                                      |
| Cell value     | `sht.range("A1").value`                | Read or write value.  | Auto-converts Python ↔ Excel types.    |
| Multiple cells | `sht.range("A1:C3").value`             | Returns nested list.  | Write list of lists back.              |
| Resize range   | `sht.range("A1").resize(3,2)`          | Expands selection.    | Useful for dynamic data.               |
| Offset         | `sht.range("A1").offset(1,0)`          | Shift cell reference. | Moves down 1 row.                      |
| Entire row/col | `sht.range("1:1")`, `sht.range("A:A")` | Select whole row/col. | Watch large selections.                |
| Clear          | `sht.range("A1:C3").clear_contents()`  | Deletes values only.  | Use `.clear()` for all formatting too. |

---

## 4. DataFrames & Numpy

| Command        | Syntax                                                             | Explanation           | Notes / Gotchas                |
| -------------- | ------------------------------------------------------------------ | --------------------- | ------------------------------ |
| Pandas → Excel | `sht.range("A1").value = df`                                       | Writes DataFrame.     | Keeps index & headers.         |
| Excel → Pandas | `df = sht.range("A1").options(pd.DataFrame, expand="table").value` | Reads into DataFrame. | `expand="table"` auto-expands. |
| Numpy arrays   | Works same as lists.                                               | Auto-converts.        | Good for math workflows.       |

---

## 5. Excel Functions & Formulas

| Command          | Syntax                                                    | Explanation                | Notes / Gotchas                                    |
| ---------------- | --------------------------------------------------------- | -------------------------- | -------------------------------------------------- |
| Formula          | `sht.range("B1").formula = "=SUM(A1:A10)"`                | Inserts Excel formula.     | Formula calculated in Excel.                       |
| Evaluate formula | `sht.range("B1").value`                                   | Returns result of formula. | Needs Excel open.                                  |
| Named ranges     | `wb.names.add("MyRange", refers_to="=Sheet1!$A$1:$A$10")` | Define named range.        | Access later with `wb.names["MyRange"].refers_to`. |

---

## 6. Charts & Shapes

| Command     | Syntax                                      | Explanation          | Notes / Gotchas             |
| ----------- | ------------------------------------------- | -------------------- | --------------------------- |
| Add chart   | `chart = sht.charts.add()`                  | Creates chart.       | Default blank.              |
| Chart type  | `chart.chart_type = "line"`                 | Sets chart type.     | Excel chart type strings.   |
| Set source  | `chart.set_source_data(sht.range("A1:B5"))` | Binds chart to data. | Range must include headers. |
| Add picture | `sht.pictures.add("img.png")`               | Inserts image.       | Path required.              |

---

## 7. App Control

| Command       | Syntax                       | Explanation            | Notes / Gotchas                       |
| ------------- | ---------------------------- | ---------------------- | ------------------------------------- |
| Excel app     | `app = xw.App(visible=True)` | Starts Excel instance. | Set `visible=False` for background.   |
| Quit Excel    | `app.quit()`                 | Closes app.            | Ends session.                         |
| Multiple apps | `xw.apps`                    | List of apps.          | Useful for multi-instance automation. |

---

## 8. UDFs (User-Defined Functions)

| Command   | Syntax                                               | Explanation                           | Notes / Gotchas                |
| --------- | ---------------------------------------------------- | ------------------------------------- | ------------------------------ |
| Decorator | `@xw.func`                                           | Define Python func callable in Excel. | Requires Excel add-in enabled. |
| Example   | `python\n@xw.func\ndef double(x):\n    return x*2\n` | Called in Excel as `=double(A1)`.     | Must install xlwings add-in.   |

---

## 9. Utilities

| Command    | Syntax                                     | Explanation                          | Notes / Gotchas              |
| ---------- | ------------------------------------------ | ------------------------------------ | ---------------------------- |
| Autofit    | `sht.autofit("c")`                         | Autofit columns (`c`) or rows (`r`). | —                            |
| Pictures   | `sht.pictures`                             | List of all pictures.                | Can manipulate.              |
| Copy range | `sht.range("A1:C3").copy(sht.range("E1"))` | Copies values & formatting.          | Similar to Excel copy/paste. |

---

## 10. Best Practices

* ✅ Always call `wb.save()` before `wb.close()`.
* ✅ Use `with xw.App():` context to auto-close.
* ✅ Prefer Pandas integration for tables.
* ✅ Use `.clear_contents()` instead of overwriting with blanks.
* ⚠️ xlwings **requires Excel installed** (not pure Python like OpenPyXL).
* ⚠️ Large ranges slow — read/write in bulk, not cell-by-cell.

---

👉 This cheat sheet now covers **all key xlwings features**: workbook/sheets, ranges, formulas, charts, Pandas/Numpy integration, app control, UDFs.

---

---
Here’s your **professional Markdown cheat sheet** for **XlsxWriter** — a library for creating Excel `.xlsx` files with advanced formatting.

---

# 📘 Python XlsxWriter Cheat Sheet

**Excel Report Generation & Formatting**

---

## 1. Basic Setup

```python
import xlsxwriter

workbook = xlsxwriter.Workbook("demo.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1", "Hello, Excel!")
workbook.close()
```

---

## 2. Writing Data

| Method                 | Example                                      | Use             |
| ---------------------- | -------------------------------------------- | --------------- |
| `write(row, col, val)` | `ws.write(0,0,"Text")`                       | Generic write   |
| `write_string()`       | `ws.write_string(0,0,"Text")`                | Explicit string |
| `write_number()`       | `ws.write_number(1,0,123)`                   | Numbers         |
| `write_boolean()`      | `ws.write_boolean(2,0,True)`                 | Booleans        |
| `write_datetime()`     | `ws.write_datetime(3,0,datetime.now(), fmt)` | Dates           |
| `write_formula()`      | `ws.write_formula("B1","=SUM(A1:A10)")`      | Excel formulas  |

---

## 3. Formatting

```python
bold = workbook.add_format({"bold": True})
ws.write("A1", "Bold Text", bold)
```

Common format options:

* `bold`, `italic`, `underline`
* `font_color`, `bg_color`
* `align`, `valign`
* `num_format` (dates, currency, etc.)

---

## 4. Column & Row Settings

```python
ws.set_column("A:A", 20)     # Width 20
ws.set_row(0, 30)            # Height 30
```

---

## 5. Charts

```python
chart = workbook.add_chart({"type": "column"})
chart.add_series({
    "categories": "=Sheet1!$A$2:$A$5",
    "values": "=Sheet1!$B$2:$B$5",
})
ws.insert_chart("D2", chart)
```

Chart types: `line`, `bar`, `column`, `pie`, `scatter`, `area`, etc.

---

## 6. Conditional Formatting

```python
ws.conditional_format("A1:A10", {"type": "cell", "criteria": ">", "value": 5, "format": bold})
```

---

## 7. Images & Shapes

```python
ws.insert_image("C5", "logo.png")
```

---

## 8. Tables

```python
ws.add_table("A1:C5", {"columns": [{"header":"Name"}, {"header":"Age"}, {"header":"Score"}]})
```

---

## 9. Worksheets

```python
ws2 = workbook.add_worksheet("Data")
ws3 = workbook.add_worksheet("Report")
```

* Use `workbook.worksheets()` to list all.

---

## 10. Beginner Pitfalls

* ❌ XlsxWriter **cannot read** existing Excel files (write-only).
* ❌ Forgetting to call `workbook.close()` → file stays corrupted.
* ❌ Using Python datetime without `num_format` → Excel shows raw numbers.
* ❌ Large files with many formats = memory heavy.

---

✅ With this, you have the **full XlsxWriter toolkit**: writing data, formatting, charts, images, conditional formats, and tables.

---
