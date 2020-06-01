from django.contrib import admin
from .models import Post , Notification,Profile
# Register your models here.
admin.site.register(Post)
admin.site.register(Notification)
admin.site.register(Profile)