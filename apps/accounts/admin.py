from django.contrib import admin
from .models import CustomUser, ProfileUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, UserAdmin)
admin.site.register(ProfileUser, ProfileAdmin)
