from django.contrib import admin

from .models import Bill, Profile

from django.contrib.auth.views import LoginView
from django.utils.html import format_html

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department_name', 'department_id']  


class BillsAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_first_name', 'get_last_name', 'get_department_name', 'get_department_id','field1', 'field2', 'field3', 'field4','field41', 'field5', 'field6', 'field7', 'field8', 'field9', 'field10', 'display_field11')

    def get_username(self, obj):
        return obj.profile.user.username

    def get_first_name(self, obj):
        return obj.profile.user.first_name

    def get_last_name(self, obj):
        return obj.profile.user.last_name

    def get_department_name(self, obj):
        return obj.profile.department_name

    def get_department_id(self, obj):
        return obj.profile.department_id
    
    def display_field11(self, obj):
        if obj.field11:
            return format_html('<a href="{0}" target="_blank">{1}</a>', obj.field11.url, obj.field11.name)
        else:
            return "-"
    display_field11.short_description = 'Invoice pdf'

    get_username.short_description = 'Username'
    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'
    get_department_name.short_description = 'Department Name'
    get_department_id.short_description = 'Department ID'

class CustomLoginView(LoginView):
    template_name = 'custom_login.html'

admin.site.register(Profile, ProfileAdmin)


admin.site.register(Bill, BillsAdmin)

admin.site.login = CustomLoginView.as_view()