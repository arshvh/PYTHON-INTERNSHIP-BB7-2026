class Notification:
    def send(self):
        print("Sending a general notification.")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")


notifications = [
    Notification(),
    EmailNotification(),
    SMSNotification(),
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send()