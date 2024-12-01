from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  staff = models.OneToOneField(User, on_delete=models.CASCADE)
  alamat = models.CharField(max_length=255)
  telp = models.CharField(max_length=13)
  foto = models.ImageField(upload_to="profile_img/", default="avatar.jpg")

  class Meta:
    verbose_name = "Profile"
    verbose_name_plural = "Profile User"

  def __str__(self):
    return f'{self.staff.username} Profile'
