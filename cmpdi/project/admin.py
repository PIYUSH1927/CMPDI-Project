from django.contrib import admin

from .models import RandomDetail, Profile

from django.contrib.auth.views import LoginView

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department_name', 'department_id']  


class RandomDetailAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_first_name', 'get_last_name', 'get_department_name', 'get_department_id','field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8', 'field9', 'field10')

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

    get_username.short_description = 'Username'
    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'
    get_department_name.short_description = 'Department Name'
    get_department_id.short_description = 'Department ID'

class CustomLoginView(LoginView):
    template_name = 'custom_login.html'

admin.site.register(Profile, ProfileAdmin)


admin.site.register(RandomDetail, RandomDetailAdmin)

admin.site.login = CustomLoginView.as_view()