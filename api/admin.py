from django.contrib import admin
from .models import User, House


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('salary',)


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_filter = ('owner', )
