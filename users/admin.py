from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import RegisterForm

User = get_user_model()

# Register your models here.       
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    model = User
    list_display = ['username', 'email', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',), 
            'fields':('email', 'password', 'password_2', 'username')}),
    )

admin.site.register(User, CustomUserAdmin)
