from django.contrib import admin
from authtools.admin import UserAdmin
from authentication.models import User
# Register your models here.

admin.site.register(User, UserAdmin)
