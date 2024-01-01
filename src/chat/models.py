from django.db import models
from users.models import User
# Create your models here.
class RoomMember(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)