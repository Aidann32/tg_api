from django.db import models

from apps.users.models import CustomUser


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    text = models.CharField(max_length=1024, null=True, blank=True)
    sended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'

