"""Challenge 1 - Send an email with an image attachment (PNG/JPG/JPEG only)."""
import os
import smtplib
from email.message import EmailMessage

# ---- Apni details yahan bharo ----
NAME = "Mahi Deopa"
SEMESTER = "7"
BRANCH = "CSE"
ROLL_NUMBER = "29"
IMAGE_PATH = "photo.jpg"  # PNG, JPG ya JPEG hi allowed hai
# -----------------------------------

SUBJECT = "Challenge 3 Completed"  # PDF mein yehi subject likha hai
ALLOWED = {".png": "png", ".jpg": "jpeg", ".jpeg": "jpeg"}


def load_env(path=".env"):
    """.env file se KEY=VALUE padhta hai (koi extra install nahi chahiye)."""
    base = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base, path)
    if not os.path.exists(full_path):
        return
    with open(full_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

load_env()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT_EMAIL", "hr@ignitershub.com")

def build_message() -> EmailMessage:
    base = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(base, IMAGE_PATH)
    ext = os.path.splitext(image_file)[1].lower()
    if ext not in ALLOWED:
        raise ValueError("Only PNG, JPG and JPEG images are allowed.")

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT
    msg["Subject"] = SUBJECT
    msg.set_content(
        f"Name: {NAME}\n"
        f"Semester: {SEMESTER}\n"
        f"Branch: {BRANCH}\n"
        f"Roll Number: {ROLL_NUMBER}\n"
    )

    with open(image_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="image",
            subtype=ALLOWED[ext],
            filename=os.path.basename(image_file),
        )
    return msg


def main() -> None:
    if not SENDER_EMAIL or not APP_PASSWORD:
        raise SystemExit(".env file mein SENDER_EMAIL aur EMAIL_APP_PASSWORD daalo.")
    msg = build_message()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
    print(f"Email sent to {RECIPIENT}")


if __name__ == "__main__":
    main()
