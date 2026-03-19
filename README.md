
# Security-Authentication-Captcha-System

##  Project Overview
This project is an automated security tool developed for **OJT-3**. It generates dynamic CAPTCHA images with noise and distortion to distinguish between human users and bots.

##  Features
* **Random Alphanumeric Generation:** Creates unique codes for every attempt.
* **Image Obfuscation:** Adds random noise dots and lines to prevent OCR bypass.
* **OOPS Based Design:** Built using Python classes for better scalability.
* **Logging System:** Maintains `captcha_audit.txt` to track verification attempts.

##  Technology Stack
* Python 3.x
* Pillow (PIL) Library
* ### Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt

