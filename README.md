#  Security Authentication Captch System

An advanced **Security Tool** developed for **OJT-3** to prevent automated bot attacks using dynamic image obfuscation and alphanumeric verification.

---

##  Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Technology Stack](#-technology-stack)
- [Installation & Usage](#-installation--usage)
- [Project Artifacts](#-project-artifacts)
- [Author](#-author)

---

##  Project Overview
This system is designed to distinguish between human users and automated scripts (bots). By generating a unique image challenge with background noise, curved lines, and rotated text, it ensures that standard OCR (Optical Character Recognition) tools cannot easily bypass the authentication layer.

##  Key Features
* **Dynamic Generation:** Unique 6-character alphanumeric strings for every session.
* **Image Obfuscation:**
    * **Salt & Pepper Noise:** 1200+ random pixels to confuse bot sensors.
    * **Character Rotation:** Each letter is tilted randomly (-30° to 30°).
    * **Interference Lines:** Randomly placed lines to break character contours.
* **Auto-Installer:** Automatically detects and installs the **Pillow** library on the first run.
* **Security Audit Log:** Every attempt is recorded in `captcha_audit.txt` for monitoring.

##  Technology Stack
* **Language:** Python 3.x
* **Libraries:** * `Pillow (PIL)` - For Image processing.
    * `Subprocess` - For automatic dependency management.
    * `Random` & `String` - For secure text generation.

---

##  Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/rizwanshaikhh618-lang/Security-Authentication-Captcha-System1.git](https://github.com/rizwanshaikhh618-lang/Security-Authentication-Captcha-System1.git)
