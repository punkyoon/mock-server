from django.contrib import admin

from accounts.models import MockUser, MockProfile


@admin.register(MockUser)
class MockUserAdmin(admin.ModelAdmin):
    fields = ('email', 'username', 'is_staff', 'is_superuser', )
    list_display = ('email', 'username', 'created', 'modified', 'is_superuser', )


@admin.register(MockProfile)
class MockProfileAdmin(admin.ModelAdmin):
    fields = ('nickname', 'locale',)
    list_display = ('nickname', 'created', 'modified', 'locale', )
