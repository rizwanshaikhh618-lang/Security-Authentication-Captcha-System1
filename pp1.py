import random
import string
import os
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class CaptchaGenerator:
    def __init__(self):
        self.width = 250
        self.height = 90
        self.save_path = "captcha.png"
        self.log_file = "captcha_audit.txt"

    def generate_random_text(self, length=6):
        # Removing confusing characters like 0, O, I, l for better UX
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        return ''.join(random.choice(chars) for _ in range(length))

    def create_captcha_image(self, text):
        # 1. Create a light-colored background
        image = Image.new('RGB', (self.width, self.height), color=(240, 240, 240))
        draw = ImageDraw.Draw(image)

        # 2. Add Background Noise (Random Dots/Points)
        for _ in range(1200):
            xy = (random.randrange(0, self.width), random.randrange(0, self.height))
            draw.point(xy, fill=(random.randint(150, 200), random.randint(150, 200), random.randint(150, 200)))

        # 3. Text Rendering with Security Features
        try:
            # Arial font is standard on Windows. If not found, use default.
            font = ImageFont.truetype("arial.ttf", 45)
        except:
            font = ImageFont.load_default()
            print("Warning: arial.ttf not found, using default font.")

        # Draw each character with a slightly different color and position
        for i, char in enumerate(text):
            char_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            # Dynamic positioning to make it harder for OCR bots
            pos = (30 + i * 35, random.randint(15, 25))
            draw.text(pos, char, font=font, fill=char_color)

        # 4. Add Noise Lines (Obfuscation)
        for _ in range(6):
            start = (random.randint(0, self.width), random.randint(0, self.height))
            end = (random.randint(0, self.width), random.randint(0, self.height))
            draw.line([start, end], fill=(100, 100, 100), width=2)

        # 5. Apply Filter (Slight Blur to soften edges for security)
        image = image.filter(ImageFilter.SMOOTH)
        
        # Save the final image
        image.save(self.save_path)
        return self.save_path

    def log_result(self, status):
        # Maintain a log file for project records
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] Attempt Status: {status}\n")

# --- Main Program Execution ---
if __name__ == "__main__":
    # Initialize the System
    system = CaptchaGenerator()
    
    # 1. Generate Text and Image
    secret_text = system.generate_random_text()
    image_file = system.create_captcha_image(secret_text)
    
    print("\n==========================================")
    print("   SECURE CAPTCHA AUTHENTICATION SYSTEM   ")
    print("==========================================")
    print(f"[*] CAPTCHA generated and saved as: {image_file}")
    print("[*] Check your folder to see the image.")
    
    # 2. Verification Challenge
    user_input = input("\n[?] Enter the characters shown in the image: ").strip().upper()

    # 3. Logic Check
    if user_input == secret_text:
        print("\n✅ Verification SUCCESSFUL! Access Granted.")
        system.log_result("SUCCESS")
    else:
        print(f"\n❌ Verification FAILED! Access Denied.")
        print(f"   (The correct text was: {secret_text})")
        system.log_result("FAILED")
    
    print("==========================================\n")