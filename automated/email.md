Here’s your **professional Markdown cheat sheet** for **Email & Notifications in Python** — using `smtplib`, `yagmail`, `Twilio`, and Gmail API.

---

# 📘 Python Email & Notifications Cheat Sheet

**Automated Messaging: Email, SMS, and Alerts**

---

## 1. Sending Email with `smtplib`

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["From"] = "you@example.com"
msg["To"] = "target@example.com"
msg["Subject"] = "Test Email"

msg.attach(MIMEText("Hello, this is a test!", "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("you@example.com", "app_password")
    server.send_message(msg)
```

✅ Use **App Passwords** for Gmail (not your real password).

---

## 2. Simplified Gmail with `yagmail`

```python
import yagmail

yag = yagmail.SMTP("you@gmail.com","app_password")
yag.send(
    to="target@example.com",
    subject="Hello",
    contents="This is a test email"
)
```

* Auto-handles attachments:

  ```python
  yag.send("target@example.com","Report","See attached","report.pdf")
  ```

---

## 3. Gmail API (OAuth-based)

* Requires Google Cloud setup + OAuth credentials.
* Safer than storing passwords.

```python
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
# Build service with creds, then send via Gmail API
```

📌 Best for production apps.

---

## 4. Sending SMS with Twilio

```python
from twilio.rest import Client

client = Client("ACCOUNT_SID", "AUTH_TOKEN")

message = client.messages.create(
    body="Hello from Python",
    from_="+1234567890",   # Your Twilio number
    to="+1987654321"       # Destination number
)

print(message.sid)
```

* Works globally for SMS/WhatsApp.
* Can also handle voice calls.

---

## 5. Notifications (System/Desktop)

```python
from plyer import notification

notification.notify(
    title="Task Complete",
    message="Your script finished running!",
    timeout=5
)
```

* Works cross-platform (Windows, macOS, Linux).

---

## 6. Common Pitfalls

* ❌ Using real Gmail password → must use **App Password** (2FA).
* ❌ Forgetting `starttls()` with `smtplib` → insecure connection.
* ❌ Sending too many emails without rate-limiting → flagged as spam.
* ❌ Using Twilio free account without verifying recipient number.

---

✅ With this, you have the **full messaging toolkit**:

* `smtplib` → low-level email
* `yagmail` → easy Gmail
* Gmail API → secure, production-ready
* `twilio` → SMS/voice
* `plyer` → desktop alerts

---

---

---



---

# 📘 Python Notifications Cheat Sheet

**Slack + Telegram + Email + SMS + Desktop**

---

## 1. Slack Notifications

### Using Incoming Webhooks

```python
import requests
import json

url = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

payload = {"text": "🚀 Task complete!"}
res = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

print(res.status_code)   # 200 = success
```

* Configure in Slack → Apps → Incoming Webhooks.
* Supports attachments & formatting (Markdown-like).

---

## 2. Telegram Bot Notifications

### Setup

1. Search **BotFather** in Telegram.
2. `/newbot` → get API token.
3. Get your chat\_id (`https://api.telegram.org/bot<token>/getUpdates`).

### Sending Message

```python
import requests

token = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
msg = "⚡ Script finished successfully!"

url = f"https://api.telegram.org/bot{token}/sendMessage"
requests.post(url, data={"chat_id": chat_id, "text": msg})
```

* Supports Markdown/HTML formatting:

  ```python
  requests.post(url, data={"chat_id": chat_id, "text": "<b>Bold Text</b>", "parse_mode": "HTML"})
  ```

---

## 3. Gmail (Quick Recap with `yagmail`)

```python
import yagmail

yag = yagmail.SMTP("me@gmail.com","app_password")
yag.send("target@example.com","Alert","Process completed ✅")
```

---

## 4. Twilio SMS (Quick Recap)

```python
from twilio.rest import Client

client = Client("SID","AUTH_TOKEN")
client.messages.create(body="⚠️ Error in script", from_="+1234567890", to="+1987654321")
```

---

## 5. Desktop Notifications

```python
from plyer import notification

notification.notify(
    title="Reminder",
    message="Take a break 🧘",
    timeout=5
)
```

---

## 6. Beginner Pitfalls

* ❌ **Slack:** Not enabling the webhook → 403 error.
* ❌ **Telegram:** Forgetting `chat_id` is required.
* ❌ **Twilio:** Free account can only send to verified numbers.
* ❌ **Gmail:** Needs **App Password** (if 2FA enabled).
* ❌ **Desktop:** Some OSes block notifications in "Do Not Disturb" mode.

---

✅ With this, you now have **multi-channel notifications**:

* Slack → team alerts
* Telegram → personal bot messages
* Gmail → email
* Twilio → SMS/WhatsApp
* Plyer → desktop popups

---


