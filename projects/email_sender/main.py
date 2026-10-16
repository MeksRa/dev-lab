import os
import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def load_config() -> tuple[str, str]:
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    if not email or not password:
        raise ValueError("EMAIL or PASSWORD not found in environment variables.")
    return email, password


EMAIL, PASSWORD = load_config()


def create_image_attachment(path: Path) -> MIMEImage:
    """Creates an image attachment from path"""
    with open(path, "rb") as file:
        mime_image = MIMEImage(file.read())
        mime_image.add_header(
            "Content-Disposition", f"attachment; filename={path.name}"
        )
        return mime_image


def send_email(
    to_email: str, subject: str, body: str, image: Path | None = None
) -> None:
    host: str = "smtp.gmail.com"  # SMTP Server
    port: int = 587  # Port TLS

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print("Logging in ...")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(EMAIL, PASSWORD)

        # Prepare the email
        print("Attempting to send the email...")
        message = MIMEMultipart()
        message["From"] = EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=message.as_string())

        # Success!
        print("Sent!")


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    # --- -- --- -- ---  /Settings  --- -- --- -- --- #
    file_dir = script_dir / "data" / "aires.jpg"
    to_email = "remeksra@gmail.com"
    subject: str = "Hey there, buddy!"
    body: str = "I sent you an image... Look..."
    # --- -- --- -- ---  Settings/  --- -- --- -- --- #

    send_email(
        to_email=to_email,
        subject=subject,
        body=body,
        image=file_dir,
    )


if __name__ == "__main__":
    main()
