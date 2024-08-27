from django.contrib import admin
from .models import User, Preferences


admin.site.register(User)
admin.site.register(Preferences)
