

# 📘 Python APIs Cheat Sheet

**Requests + Authentication**

---

## 1. Basic GET Request

```python
import requests

res = requests.get("https://api.example.com/data")
print(res.status_code)   # 200
print(res.json())        # JSON response as dict
```

---

## 2. Query Parameters

```python
params = {"q":"python","limit":5}
res = requests.get("https://api.example.com/search", params=params)
```

➡️ Encodes as `...?q=python&limit=5`

---

## 3. Headers

```python
headers = {"User-Agent": "MyApp/1.0"}
res = requests.get("https://api.example.com/data", headers=headers)
```

---

## 4. Sending Data

* **Form data**

```python
res = requests.post("https://api.example.com/form", data={"name":"Miguel"})
```

* **JSON body**

```python
res = requests.post("https://api.example.com/json", json={"name":"Miguel"})
```

---

## 5. Authentication

### Basic Auth

```python
from requests.auth import HTTPBasicAuth
res = requests.get("https://api.example.com",
                   auth=HTTPBasicAuth("user","pass"))
```

### Token Auth (Bearer)

```python
headers = {"Authorization":"Bearer YOUR_TOKEN"}
res = requests.get("https://api.example.com/secure", headers=headers)
```

### API Key in Header

```python
headers = {"x-api-key":"YOUR_KEY"}
res = requests.get("https://api.example.com/data", headers=headers)
```

### API Key in URL

```python
res = requests.get("https://api.example.com/data?apikey=YOUR_KEY")
```

---

## 6. Handling Responses

```python
if res.status_code == 200:
    data = res.json()
else:
    print("Error:", res.status_code, res.text)
```

---

## 7. File Uploads & Downloads

* **Upload**

```python
files = {"file": open("report.csv","rb")}
res = requests.post("https://api.example.com/upload", files=files)
```

* **Download**

```python
with requests.get("https://example.com/file.pdf", stream=True) as r:
    with open("file.pdf","wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
```

---

## 8. Sessions (Keep Cookies)

```python
s = requests.Session()
s.headers.update({"Authorization":"Bearer TOKEN"})
res = s.get("https://api.example.com/me")
```

---

## 9. Common Pitfalls

* ❌ Forgetting to check `res.status_code` → silent failures.
* ❌ Mixing `data=` and `json=` → use the correct one.
* ❌ Hardcoding secrets → use **environment variables** (`os.getenv`).
* ❌ Ignoring API rate limits → always check docs.

---

✅ With this, you have the **API essentials**: GET/POST, params, headers, auth (Basic, Token, API key), file uploads/downloads, and sessions.
