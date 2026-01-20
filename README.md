# 🦖 Google Dino Bot (Python)

This project is a simple Python bot that automatically plays the Google Chrome Dino (T-Rex) game using Selenium and basic image processing.

---

## Features

- Opens and starts the Dino game automatically
- Detects obstacles using pixel brightness
- Works in both light mode and dark mode
- Uses cropped screenshots for better performance
- No machine learning, no OpenCV

---

## How It Works

1. Selenium opens the Dino game and presses SPACE to start
2. A small screen region in front of the Dino is captured
3. The image is converted to grayscale
4. Pixel brightness is analyzed to detect obstacles
5. The bot presses SPACE to jump when an obstacle is detected

---

## Requirements

- Python 3.10+
- Google Chrome
- ChromeDriver

Python packages:
- selenium
- pillow
- numpy

---

## Installation

Create virtual environment:

python -m venv .venv  
source .venv/bin/activate

Install dependencies:

pip install selenium pillow numpy

---

## How to Run

python main.py

After a few seconds, the bot will start playing automatically.

Important:
- Do not resize or move the browser window
- Screen coordinates are fixed

---

## Notes

- Obstacle detection is based on grayscale brightness
- Dark mode and light mode are handled separately
- The bot only jumps (ducking is not implemented)

---

## Limitations

- Screen resolution dependent
- No bird duck logic
- No score tracking
- Fixed coordinates

---

## Purpose

This project is for learning:
- Selenium automation
- Screen capture
- Basic image processing
- Real-time automation logic

---

## Disclaimer

For educational purposes only.
