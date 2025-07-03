# AI-Based Drone Surveillance System 🛰️

This project implements an intelligent drone surveillance system using YOLOv8 on a Raspberry Pi 4 to detect changes in monitored environments by comparing two video streams.

## 🔍 Project Objective
To monitor real-time environmental changes (e.g., new objects, intrusions) using AI-based object detection on edge devices.

## 🛠️ Features
- Compares a **baseline video** with a **current video feed**
- Runs **YOLOv8** object detection
- Detects newly appeared or missing objects
- Deployable on **Raspberry Pi 4**

## 🖼️ Sample Output
![Result Screenshot](<img width="721" alt="v1" src="https://github.com/user-attachments/assets/62625c58-2bb3-4597-99ea-1d79d79a80cf" />
)

## 📁 File Structure
- `main.py`: Main script to run YOLOv8 and compare frames.
- `utils/video_comparator.py`: Helper functions for comparison.
- `requirements.txt`: Python dependencies.
- `docs/project_report.pdf`: Full project documentation.

## 🧠 Technologies
- Python
- OpenCV
- Ultralytics YOLOv8
- Raspberry Pi 4

## 📦 Requirements
```bash
pip install -r requirements.txt
