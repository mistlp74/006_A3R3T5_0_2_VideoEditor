# WebcamEffectsRecorder

## Description

**WebcamEffectsRecorder** is a simple desktop application using Python and Tkinter that allows you to view your webcam feed with real-time effects, adjust brightness, convert to grayscale, invert colors, and record video with the selected effect.

---

## Features

- Live webcam preview in a graphical window
- Apply brightness adjustment, grayscale, or inversion effects in real time
- Reset the feed to the original view
- Record video with the selected effect and save as AVI
- Intuitive and minimal GUI built with Tkinter

---

## Requirements

- Python 3.8+
- `opencv-python`
- `Pillow`
- `tkinter` (usually included with Python)

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mistlp74/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies:**
    ```bash
    pip install opencv-python pillow
    ```

---

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. Use the buttons to:
    - Show original webcam feed
    - Adjust brightness (enter value 0-100)
    - Apply black & white (grayscale) effect
    - Invert colors
    - Start/stop video recording (AVI format)

---

## Troubleshooting

- **No webcam detected:** Make sure your camera is connected and not used by another app.
- **Cannot save video:** Check the save path and permissions.
- **GUI does not open:** Verify that all dependencies are installed and your Python version is supported.

---

## Author

Developed by [mistlp74](https://github.com/mistlp74)