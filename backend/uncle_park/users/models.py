from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' ' + str(self.email)
