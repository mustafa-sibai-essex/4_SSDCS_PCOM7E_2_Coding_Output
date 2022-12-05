import threading
from django.core.mail import send_mail


class SendEmail(threading.Thread):
    def __init__(self, title, body, email):
        self.title = title
        self.body = body
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        try:
            send_mail(
                self.title,
                self.body,
                None,
                [self.email],
                False,
            )
        except Exception as e:
            print(e)
