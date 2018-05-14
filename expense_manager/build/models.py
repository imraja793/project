from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    mobile_no = models.IntegerField()

    def __str__(self):
        return self.user.username.IntegerField(blank=True)
