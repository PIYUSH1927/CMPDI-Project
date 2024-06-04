from django.contrib import admin

from .models import Profile

from django.contrib.auth.views import LoginView

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department_name', 'department_id']  # Specify fields to display in the admin interface

class CustomLoginView(LoginView):
    template_name = 'custom_login.html'

admin.site.register(Profile, ProfileAdmin)


admin.site.login = CustomLoginView.as_view()