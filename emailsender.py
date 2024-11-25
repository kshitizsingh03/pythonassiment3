import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, receiver_email, subject, message):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(sender_email, app_password)

        server.sendmail(sender_email, receiver_email, msg.as_string())

        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sender_email = input("Enter your email address: ")
    app_password = input("Enter your App Password: ")
    receiver_email = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    message = input("Enter the message: ")

    send_email(sender_email, app_password, receiver_email, subject, message)

