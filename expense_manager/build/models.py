from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])