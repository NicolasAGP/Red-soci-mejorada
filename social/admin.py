from django.contrib import admin
from .models import Image, SocialPost, SocialComment

admin.site.register(SocialPost)
admin.site.register(SocialComment)
admin.site.register(Image)

# Register your models here.
