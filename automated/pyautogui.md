
---

# 📘 PyAutoGUI Cheat Sheet

**Cross-platform Mouse, Keyboard & Screen Automation**

```python
import pyautogui as pg
```

---

## 1. Screen Size & Position

```python
pg.size()       # (width, height) of screen
pg.position()   # current mouse (x,y)
pg.onScreen(x,y) # True if coords are visible
```

---

## 2. Mouse Control

```python
pg.moveTo(100,200,duration=1)   # move to (100,200)
pg.moveRel(50,0,duration=0.5)   # move relative
pg.click()                      # left click
pg.click(200,300,button="right")# right click
pg.doubleClick()
pg.tripleClick()
pg.mouseDown(); pg.mouseUp()    # press/release
pg.scroll(500)                  # scroll up
```

---

## 3. Keyboard Control

```python
pg.typewrite("Hello world!", interval=0.1)
pg.press("enter")
pg.hotkey("ctrl","s")     # combo
pg.keyDown("shift"); pg.keyUp("shift")
```

Common keys: `"enter"`, `"esc"`, `"tab"`, `"ctrl"`, `"alt"`, `"shift"`, `"space"`, `"f1"`–`"f12"`

---

## 4. Screen Capture & Recognition

```python
pg.screenshot("shot.png")         # save screenshot
pg.locateOnScreen("icon.png")     # find element coords
pg.locateCenterOnScreen("btn.png")# find center
pg.locateAllOnScreen("img.png")   # all matches
```

* Works best when scaling = 100% and clear image.

---

## 5. Fail-Safes & Pauses

```python
pg.FAILSAFE = True    # move mouse to corner to stop
pg.PAUSE = 1          # 1-sec pause after each call
```

---

## 6. Alerts & Prompts

```python
pg.alert("Task done!")
pg.confirm("Continue?")
pg.prompt("Enter name:")
pg.password("Enter password:")
```

---

## 7. Useful Tricks

* **Relative automation** (no fixed coords):
  Use image recognition instead of raw `(x,y)`.
* **Multiple monitors:** use `pg.size()` to confirm correct dimensions.
* **Emergency exit:** slam mouse to **top-left corner** if script goes crazy.

---

## 8. Beginner Pitfalls

* ❌ Hardcoding pixel coords → breaks if window moves.
* ❌ Forgetting screen scaling → image matching fails.
* ❌ Running without `FAILSAFE` → can lock mouse/keyboard.
* ❌ Automation too fast → always use `duration` or `PAUSE`.

---

✅ With this, you have the **PyAutoGUI essentials**: mouse, keyboard, screenshots, image recognition, and safety.

---

