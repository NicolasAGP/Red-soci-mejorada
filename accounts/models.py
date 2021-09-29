from django.db import models

# Obtenemos el usuario heredando toda las virtudes de Django
from django.contrib.auth.models import AbstractUser

from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save