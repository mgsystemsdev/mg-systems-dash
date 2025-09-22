

# 📘 Python Automation Cheat Sheet

**Tools & Libraries for Everyday Automation**

---

## 1. OS & File Automation

| Module                     | Command                     | Explanation                |
| -------------------------- | --------------------------- | -------------------------- |
| `os`                       | `os.listdir("path")`        | List files in directory.   |
| `os.rename("old","new")`   | Rename file.                |                            |
| `os.remove("file.txt")`    | Delete file.                |                            |
| `os.makedirs("newdir")`    | Create directory.           |                            |
| `os.getcwd()`              | Current working directory.  |                            |
| `shutil`                   | `shutil.copy("src","dst")`  | Copy files.                |
| `shutil.move("src","dst")` | Move/rename file.           |                            |
| `shutil.rmtree("dir")`     | Delete folder recursively.  |                            |
| `pathlib`                  | `Path("file.txt").exists()` | Modern file path handling. |

---

## 2. File Formats (Excel, CSV, JSON)

| Library            | Command                      | Explanation            |
| ------------------ | ---------------------------- | ---------------------- |
| `csv`              | `csv.reader(f)`              | Read CSV rows.         |
| `pandas`           | `pd.read_csv("file.csv")`    | Powerful CSV handling. |
| `openpyxl`         | `load_workbook("file.xlsx")` | Read/write Excel.      |
| `xlwings`          | Automate Excel via Python.   | Needs Excel installed. |
| `json`             | `json.load(f)`               | Load JSON.             |
| `json.dump(obj,f)` | Save JSON.                   |                        |

---

## 3. Web & Internet

| Library                         | Command                                    | Explanation                       |
| ------------------------------- | ------------------------------------------ | --------------------------------- |
| `requests`                      | `requests.get("url")`                      | Fetch webpage.                    |
| `requests.post("url",data=...)` | Send data.                                 |                                   |
| `bs4` (BeautifulSoup)           | `soup = BeautifulSoup(html,"html.parser")` | Parse HTML.                       |
| `selenium`                      | Browser automation (clicks, inputs).       | Great for scraping dynamic sites. |
| `pyppeteer/playwright`          | Headless Chrome automation.                | Advanced scraping.                |

---

## 4. Files & PDFs

| Library      | Command                     | Explanation                 |
| ------------ | --------------------------- | --------------------------- |
| `PyPDF2`     | `PdfReader("doc.pdf")`      | Extract text, merge, split. |
| `pdfplumber` | Better PDF text extraction. | Handles tables.             |
| `reportlab`  | Create PDF documents.       | Generate invoices/reports.  |
| `docx`       | `Document("file.docx")`     | Automate Word docs.         |

---

## 5. Automation with Time & Scheduling

| Module       | Command                                    | Explanation           |
| ------------ | ------------------------------------------ | --------------------- |
| `time`       | `time.sleep(5)`                            | Pause execution.      |
| `schedule`   | `schedule.every().day.at("09:00").do(job)` | Daily job scheduling. |
| `threading`  | Run tasks in background.                   | Concurrency.          |
| `subprocess` | Run shell commands.                        | Integrate CLI tools.  |

---

## 6. Email & Notifications

| Library   | Command                 | Explanation            |
| --------- | ----------------------- | ---------------------- |
| `smtplib` | Send emails via SMTP.   | Requires server creds. |
| `imaplib` | Read emails from inbox. | Fetch & filter.        |
| `yagmail` | Easy Gmail automation.  | Simplifies SMTP.       |
| `twilio`  | Send SMS/WhatsApp.      | Requires API key.      |
| `plyer`   | Desktop notifications.  | Cross-platform.        |

---

## 7. Web APIs

| Library                    | Command                               | Explanation             |
| -------------------------- | ------------------------------------- | ----------------------- |
| `requests`                 | `requests.get("api_url").json()`      | REST API calls.         |
| `httpx`                    | Modern async HTTP client.             | Faster than `requests`. |
| `openai`                   | Automate with GPT/AI APIs.            | Requires API key.       |
| `google-api-python-client` | Automate Google Drive, Sheets, Gmail. | Needs OAuth.            |

---

## 8. GUI & Desktop Automation

| Library                        | Command                      | Explanation               |
| ------------------------------ | ---------------------------- | ------------------------- |
| `pyautogui`                    | `pyautogui.click(x,y)`       | Mouse & keyboard control. |
| `pyautogui.typewrite("Hello")` | Type text.                   |                           |
| `pyautogui.screenshot()`       | Take screenshots.            |                           |
| `tkinter`                      | Build GUIs.                  | Bundled with Python.      |
| `PySide6 / PyQt5`              | Full desktop app automation. | Professional GUIs.        |

---

## 9. System & Data Automation

| Library    | Command                | Explanation              |
| ---------- | ---------------------- | ------------------------ |
| `psutil`   | `psutil.cpu_percent()` | Monitor system usage.    |
| `logging`  | `logging.info("msg")`  | Log automation events.   |
| `argparse` | Build CLI tools.       | Parse command-line args. |
| `dotenv`   | `load_dotenv()`        | Store secrets in `.env`. |

---

## 10. Best Practices

* ✅ Start with **small tasks** (file renaming, CSV cleaning).
* ✅ Use **virtual environments** for clean setups.
* ✅ Log automation tasks (errors, successes).
* ✅ Use **try/except** to handle failures.
* ⚠️ Be careful with scripts that **delete or overwrite files**.
* ⚠️ Don’t store passwords in scripts → use environment variables.

---

👉 This cheat sheet now covers **Python’s automation ecosystem**: OS, file formats, web scraping, scheduling, Excel/PDF/Word, email, APIs, and GUIs.

