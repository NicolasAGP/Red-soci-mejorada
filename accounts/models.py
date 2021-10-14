from django.db import models

# Obtenemos el usuario heredando toda las virtudes de Django
from django.contrib.auth.models import AbstractUser

from django.conf import settings
#trabajamos con el directorio
import os
#Pil para trabajar las imagines 
from PIL import Image
from django.db.models.deletion import CASCADE
from django.db.models.fields import URLField
from django.db.models.lookups import Contains
#Para que cuando se cree el usuario podamos trabajar su perfil....
from django.db.models.signals import post_save

#guardamos y creamos carpeta para fotos de usuario
def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    
    return profile_picture_name

#guardamos y creamos carpeta para fotos de banner
def user_directory_path_banner(instance, filename):
    profile_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    
    return profile_picture_name


VERIFICATION_OPTIONS=(
    ('unverified', 'unverified'),
    ('verified', 'verified'),
)

#Crearemos la extencion del usuario desde AbstractUser donde eredamos los datos

class User(AbstractUser):
    #stripe_customer_id es para realizar pagos en lineas existen apis que pueden realizar todo esto
    stripe_customer_id = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/user_default_profile.png', upload_to="user_directory_path_profile")

    banner = models.ImageField(default='users/user_default_banner.png', upload_to="user_directory_path_banner")

    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')

    coins = models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=False)

    date_created = models.DateField(auto_now_add=True)


    #user info

    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    brithday= models.DateField(null=True, blank=True)
    bio= models.TextField(max_length=150, null=True, blank=True)


    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **Kwargs):
    if created:
        Profile.objects.create(user=instance)
    

def save_user_profile(sender, instance, **Kwargs):
    instance.profile.save()

#created profile
post_save.connect(create_user_profile, sender=User)
# save created profile
post_save.connect(save_user_profile, sender=User)