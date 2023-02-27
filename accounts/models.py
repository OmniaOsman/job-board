from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from cities_light.models import City

# Create your models here.
class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    image = models.ImageField(upload_to='profile/')
    city  = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
     
    def __str__(self) -> str:
        return str(self.user)
        

# create profile after create user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
