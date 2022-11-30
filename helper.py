import smtplib, ssl

class Mailer:
    def __init__(self):
        self.port = 465
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = "kartheek@gmail.com"
        self.password = "qsyxyayaypcyqxet"
        self.receiver_email = "kartheek@gmail.com"
        self.context = ssl.create_default_context()
        
    def mail_format(self, subject, body):
        message = """\
        Subject: {}
        {}
        """.format(subject, body)
        return message
        
    def write_mail(self, subject, body):
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
            server.login(self.sender_email, self.password)
            message = self.mail_format(subject, body)
            server.sendmail(self.sender_email, self.receiver_email, self.message)