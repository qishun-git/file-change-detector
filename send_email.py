import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailSender(object):
    def __init__(self, config):
        super().__init__()
        # SMTP service
        mail_config = config["email"]
        self.mail_host = mail_config["server"]
        self.mail_user = mail_config["username"]
        self.mail_pass = mail_config["password"]
        self.sender = mail_config["sender"]
        self.receivers = mail_config["receivers"]

    def construct_email(self, dir, file):
        message = MIMEText('Python Email Test...', 'plain', 'utf-8')
        message['From'] = Header("Email", 'utf-8')
        message['To'] = Header("Test", 'utf-8')

        subject = 'Python SMTP Email Test'
        message['Subject'] = Header(subject, 'utf-8')

        return message

    def send_emails(self, message):
        try:
            server = smtplib.SMTP_SSL(self.mail_host, 465)
            server.ehlo()
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.sender, self.receivers, message.as_string())
            server.close()
            for receiver in self.receivers:
                print("Successfully send email to " + receiver)
        except smtplib.SMTPException:
            print("Error: Email sending failed")
