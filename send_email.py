import logging
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def construct_email(path, file):
    message = MIMEText(
        f"No video was uploaded to '{path}' since 1 hour ago, please check the functionality of your home camera. The latest added file is {file}",
        "plain", "utf-8")
    message['From'] = Header("File Change Detector", 'utf-8')
    message['To'] = Header("Members of the CatKingdom", 'utf-8')

    subject = 'Please Check Home Camera'
    message['Subject'] = Header(subject, 'utf-8')

    return message


class EmailSender():
    def __init__(self, config):
        # SMTP service
        mail_config = config["email"]
        self.mail_host = mail_config["server"]
        self.mail_user = mail_config["username"]
        self.mail_pass = mail_config["password"]
        self.sender = mail_config["sender"]
        self.receivers = mail_config["receivers"]

    def send_emails(self, message):
        try:
            server = smtplib.SMTP_SSL(self.mail_host, 465)
            server.ehlo()
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.sender, self.receivers, message.as_string())
            server.close()
            for receiver in self.receivers:
                logging.info("Successfully sent email to " + receiver)
        except smtplib.SMTPException:
            logging.error("Error: Email sending failed")
