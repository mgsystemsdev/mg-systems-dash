

# 📘 Jupyter & IPython Tricks Cheat Sheet

**Interactive Computing Essentials**

---

## 1. Running Python Code Normally

```python
print("Hello Jupyter")
```

---

## 2. Magic Commands (Start with `%` or `%%`)

### Line Magics (`%`)

| Magic                  | Example                       | Use                              |
| ---------------------- | ----------------------------- | -------------------------------- |
| `%pwd`                 |                               | Show current directory           |
| `%ls`                  |                               | List files in current dir        |
| `%cd new_folder`       |                               | Change directory                 |
| `%env`                 |                               | Show environment variables       |
| `%time expr`           | `%time sum(range(1000000))`   | Time single statement            |
| `%timeit expr`         | `%timeit sum(range(1000000))` | Run multiple times for avg       |
| `%who` / `%whos`       |                               | List variables in namespace      |
| `%reset`               |                               | Clear namespace                  |
| `%history`             |                               | Show command history             |
| `%matplotlib inline`   |                               | Show plots inline                |
| `%pip install package` |                               | Install packages inside notebook |

### Cell Magics (`%%`)

| Magic                   | Example | Use                                                |
| ----------------------- | ------- | -------------------------------------------------- |
| `%%time`                |         | Time whole cell once                               |
| `%%timeit`              |         | Time whole cell many runs                          |
| `%%bash`                |         | Run bash commands                                  |
| `%%writefile script.py` |         | Save cell content to file                          |
| `%%capture`             |         | Suppress cell output (store in variable if needed) |
| `%%html`                |         | Render HTML                                        |
| `%%latex`               |         | Render LaTeX                                       |
| `%%javascript`          |         | Run JS in cell                                     |
| `%%markdown`            |         | Render Markdown in output                          |

---

## 3. Shell Integration

```python
!ls         # run shell command
!pip list   # list installed packages
```

* Variables from Python can be passed into shell:

```python
files = "*.py"
!ls {files}
```

---

## 4. Debugging

```python
%debug   # after error, open debugger
%pdb on  # auto-debug on errors
```

---

## 5. Profiling

```python
%prun some_function()   # profile execution
```

---

## 6. Rich Display

```python
from IPython.display import HTML, Image, Markdown

Image("pic.png")
Markdown("**bold text**")
HTML("<h2>Hello</h2>")
```

---

## 7. Keyboard Shortcuts (Jupyter)

| Mode    | Shortcut      | Action                      |
| ------- | ------------- | --------------------------- |
| Command | `A`           | Insert cell above           |
| Command | `B`           | Insert cell below           |
| Command | `D,D`         | Delete cell                 |
| Command | `Z`           | Undo cell delete            |
| Command | `Shift+M`     | Merge cells                 |
| Edit    | `Shift+Enter` | Run cell & move down        |
| Edit    | `Ctrl+Enter`  | Run cell, stay in place     |
| Edit    | `Alt+Enter`   | Run cell & insert new below |

---

## 8. Extensions (Optional)

* **Jupyter Lab extensions** for productivity:

  * Variable Inspector
  * Table of Contents
  * Spellchecker
* **nbextensions** in classic Jupyter Notebook.

---

## 9. Beginner Pitfalls

* ❌ Forgetting `%matplotlib inline` → plots won’t show.
* ❌ Using `!pip install` without `%pip install` inside notebooks (may install to wrong env).
* ❌ Overusing `!shell` commands when Python built-ins (`os`, `pathlib`) are safer.
* ❌ Forgetting to reset kernel after changing environment/packages.

---

✅ With this, you have the **Jupyter & IPython essentials**: magics, shell integration, debugging, profiling, rich outputs, and shortcuts.
