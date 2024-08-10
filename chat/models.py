from django.db import models
from django.conf import settings

class Message(models.Model):
    sender_id = models.CharField(max_length=255,default='unknown') #default value  default='unknown' removed
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender_id}: {self.content[:20]}"

