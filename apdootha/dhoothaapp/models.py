from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

def get_profile_image_path(self, filename):
    return f'profile_images/{filename}'
def get_default_profile_image():
    return 'profile_images/user.png'
class Account(AbstractUser):
    profile_image = models.ImageField(null=True, blank=True)
    phonecode = models.CharField(max_length=255, null=True, blank=True)
    phone = models.PositiveBigIntegerField(null=True, blank=True)
    pincode = models.PositiveBigIntegerField(null=True, blank=True)
    village = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    mandal = models.CharField(max_length=255, null=True, blank=True)
    doj=models.DateField(null=True,blank=True)
    dor=models.DateField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

# Create your models here.
