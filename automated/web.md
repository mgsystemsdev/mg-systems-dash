

# 📘 Python Web (Requests, BeautifulSoup, Selenium) Cheat Sheet

**Fetching, Parsing, Automating Websites**

---

## 1. Requests — HTTP for Humans

```python
import requests

res = requests.get("https://example.com")
print(res.status_code)   # 200
print(res.text)          # HTML content
```

### Common Methods

| Method     | Example                              | Use             |
| ---------- | ------------------------------------ | --------------- |
| `get()`    | `requests.get(url)`                  | Fetch page      |
| `post()`   | `requests.post(url, data={"k":"v"})` | Submit form     |
| `put()`    | `requests.put(url, data)`            | Update resource |
| `delete()` | `requests.delete(url)`               | Delete resource |

### Response

```python
res.status_code
res.text
res.content   # raw bytes
res.json()    # JSON response
res.headers
```

### Advanced

```python
requests.get(url, params={"q":"python"})
requests.get(url, headers={"User-Agent":"MyApp"})
requests.get(url, timeout=5)
```

---

## 2. BeautifulSoup — HTML Parsing

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, "html.parser")
```

### Finding Elements

| Method                         | Example         | Result |
| ------------------------------ | --------------- | ------ |
| `soup.title`                   | Page `<title>`  |        |
| `soup.find("h1")`              | First `<h1>`    |        |
| `soup.find_all("a")`           | All links       |        |
| `soup.select("div.content a")` | CSS selectors   |        |
| `tag.get("href")`              | Attribute value |        |

### Extract Text

```python
soup.get_text()
link.text
```

---

## 3. Selenium — Browser Automation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

elem = driver.find_element(By.NAME, "q")
elem.send_keys("Python\n")
print(driver.title)
driver.quit()
```

### Common Find Methods

| Method                                          | Example        |
| ----------------------------------------------- | -------------- |
| `find_element(By.ID,"id")`                      | Single element |
| `find_elements(By.CLASS_NAME,"class")`          | Multiple       |
| `find_element(By.NAME,"q")`                     | Form input     |
| `find_element(By.TAG_NAME,"h1")`                | Tag            |
| `find_element(By.LINK_TEXT,"Home")`             | Link text      |
| `find_element(By.CSS_SELECTOR,"div.content a")` | CSS            |
| `find_element(By.XPATH,"//div[@id='main']")`    | XPath          |

### Actions

```python
elem.click()
elem.send_keys("text")
driver.back()
driver.forward()
driver.refresh()
```

---

## 4. Combining All Three

```python
import requests
from bs4 import BeautifulSoup

res = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(res.text,"html.parser")
quotes = [q.text for q in soup.select(".text")]
```

---

## 5. Beginner Pitfalls

* ❌ Using `requests` on **JavaScript-heavy sites** → need Selenium/Playwright.
* ❌ Forgetting headers → some sites block bots without a `User-Agent`.
* ❌ Parsing without checking `.status_code`.
* ❌ Not waiting for page load in Selenium → use `WebDriverWait`.
* ❌ Forgetting to `quit()` browser → leaves background processes.

---

✅ With this, you have the **full web toolkit**:

* `requests` → fetch content, APIs
* `BeautifulSoup` → parse HTML
* `Selenium` → interact with real browsers

---
