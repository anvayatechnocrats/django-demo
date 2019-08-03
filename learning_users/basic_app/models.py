from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship not inherite from User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra Fileds that is not part of Official User but Website devloper needs it.
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User
        return self.user.username
