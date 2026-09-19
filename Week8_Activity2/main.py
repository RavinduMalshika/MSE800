from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("Email sent")

class SMS(Notification):
    def send(self):
        print("SMS sent")

class PushNotification(Notification):
    def send(self):
        print("Push Notification sent")

class NotificationFactory(ABC):
    @abstractmethod
    def create(self):
        pass

class EmailFactory(NotificationFactory):
    def create(self):
        return Email()

class SMSFactory(NotificationFactory):
    def create(self):
        return SMS()

class PushNotificationFactory(NotificationFactory):
    def create(self):
        return PushNotification()

EmailFactory().create().send()
