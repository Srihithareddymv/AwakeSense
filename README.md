# AwakeSense 🚗🧠

### AI-Powered Driver Drowsiness & Distraction Detection System

AwakeSense is a real-time computer vision system designed to monitor driver alertness and detect signs of drowsiness and distraction.

It analyzes facial features, eye activity, head position, and phone usage through a live camera feed and provides visual and audio alerts when potentially dangerous behavior is detected.

---

## ✨ Features

- 👀 Real-time eye state detection
- 😉 Blink detection and counting
- 🥱 Yawn detection and counting
- 🧠 Head pose detection
- 📱 Phone usage detection
- 😴 Real-time fatigue scoring
- 🔊 Audio alarm for prolonged eye closure
- 📱 Audio alarm when phone usage is detected
- 🚨 Emergency warning mode for drowsiness
- 📊 Live monitoring dashboard
- 📷 Real-time camera processing

---

## 🧠 How It Works

AwakeSense processes the camera feed continuously and analyzes multiple visual indicators:

```text
Camera
   ↓
Face Detection
   ↓
Face Mesh & Landmark Detection
   ↓
┌───────────────┬───────────────┬───────────────┐
│ Eye Analysis  │ Yawn Analysis │ Head Pose     │
└───────────────┴───────────────┴───────────────┘
                 ↓
          Fatigue Analysis
                 ↓
       Phone/Object Detection
                 ↓
       Dashboard + Alerts