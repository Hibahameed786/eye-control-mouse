# eye-control-mouse
This project is created as an insight for future.By using our eye we can control the mouse of a computer and also when we blink it double clicks and selects the option.

👁️ Iris-Based Eye Mouse Controller

This project allows you to **control your computer cursor using eye movement** and **click by double blinking**, using your webcam. It uses **MediaPipe** for face and eye tracking, **OpenCV** for video input, and **PyAutoGUI** for controlling the mouse.

> Includes a simple GUI interface built with `tkinter` to start/stop the eye control easily.

---

🚀 Features

* 🖱️ Move the mouse cursor with your eye (iris tracking).
* 👀 Double blink to perform a click.
* 🧠 Smart detection using MediaPipe FaceMesh.
* 🪟 Easy-to-use GUI with start/stop buttons.
* 💻 Real-time webcam control with ESC key to exit.

---

🛠️ Requirements

* Python 3.7 or later
* Webcam

 📦 Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

> `tkinter` comes pre-installed with Python.

---

📁 How to Run

1. Clone or download this repository.
2. Run the Python script:

```bash
python eye_mouse_gui.py
```

> Replace `eye_mouse_gui.py` with the name of your Python file if different.

3. Click **Start Eye Control** to begin using your eyes to control the cursor.

4. Press **ESC** in the webcam window to stop or click the **Stop** button in the GUI.

---

 🎮 Controls

| Action                  | Behavior                   |
| ----------------------- | -------------------------- |
| Move Eyes               | Moves mouse cursor         |
| Double Blink (Fast)     | Left Mouse Click           |
| ESC Key (Webcam Window) | Stop and Close webcam feed |

---

 📷 How It Works

* Uses **MediaPipe's FaceMesh** with `refine_landmarks=True` to get accurate iris positions (landmark 474).
* Calculates your eye's (x, y) position and maps it to screen resolution.
* Detects blinking by comparing the vertical and horizontal eye landmark distance.

---

 🧠 Credits

* [Google MediaPipe](https://mediapipe.dev/)
* [OpenCV](https://opencv.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/)

---

 ⚠️ Disclaimer

This is a prototype and may require good lighting and a centered face for accurate results. Not tested on all screen sizes or webcam models.
