import cv2
import mediapipe as mp
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox

# Global flags
running = False
cap = None

# Initialize FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,  # Needed for iris landmarks (like 474)
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

screen_w, screen_h = pyautogui.size()
blink_time = 0
blink_count = 0


def get_blink_ratio(landmarks, eye_indices):
    """Calculate the blink ratio to detect blink events"""
    left = landmarks[eye_indices[0]]
    right = landmarks[eye_indices[1]]
    top = landmarks[eye_indices[2]]
    bottom = landmarks[eye_indices[3]]

    horizontal = ((left.x - right.x) ** 2 + (left.y - right.y) ** 2) ** 0.5
    vertical = ((top.y - bottom.y) ** 2 + (top.x - bottom.x) ** 2) ** 0.5
    return vertical / horizontal


def eye_control():
    """Main loop to control mouse using eye tracking"""
    global running, cap, blink_time, blink_count

    cap = cv2.VideoCapture(0)

    while running:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_frame)

        if result.multi_face_landmarks:
            landmarks = result.multi_face_landmarks[0].landmark

            # Blink detection
            right_eye = [33, 133, 159, 145]  # left, right, top, bottom
            ratio = get_blink_ratio(landmarks, right_eye)

            if ratio < 0.23:
                if time.time() - blink_time < 0.5:
                    blink_count += 1
                else:
                    blink_count = 1
                blink_time = time.time()

                if blink_count == 2:
                    pyautogui.click()
                    blink_count = 0

            # Eye movement to control mouse
            if len(landmarks) > 474:
                eye_x = landmarks[474].x
                eye_y = landmarks[474].y

                screen_x = screen_w * eye_x
                screen_y = screen_h * eye_y
                pyautogui.moveTo(screen_x, screen_y, duration=0.1)

        cv2.imshow("Eye Tracker - Press ESC to Quit", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            stop_eye_control()
            break

    if cap:
        cap.release()
    cv2.destroyAllWindows()


def start_eye_control():
    """Start the eye control thread"""
    global running
    if not running:
        running = True
        threading.Thread(target=eye_control).start()
    else:
        messagebox.showinfo("Info", "Eye control is already running!")


def stop_eye_control():
    """Stop the eye control"""
    global running
    running = False


# GUI
app = tk.Tk()
app.title("Eye Control Interface")
app.geometry("300x180")
app.configure(bg="#f0f0f0")

tk.Label(app, text="Iris-Based Mouse Controller", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Button(app, text="Start Eye Control", font=("Arial", 12), width=20, bg="#4caf50", fg="white",
          command=start_eye_control).pack(pady=5)
tk.Button(app, text="Stop", font=("Arial", 12), width=20, bg="#f44336", fg="white",
          command=stop_eye_control).pack(pady=5)

tk.Label(app, text="Double Blink = Click", font=("Arial", 10), fg="gray", bg="#f0f0f0").pack(pady=5)
tk.Label(app, text="ESC = Exit Eye Tracker", font=("Arial", 10), fg="gray", bg="#f0f0f0").pack()

app.mainloop()
