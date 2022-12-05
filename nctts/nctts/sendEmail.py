import threading
from django.core.mail import send_mail


class SendEmail(threading.Thread):
    """Creates a background thread to send the email. Rather than freezing the page until the operation is done a background thread is spawned to complate the operation."""
    def __init__(self, title, body, email):
        self.title = title
        self.body = body
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        """Runs the thread in the background"""
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
