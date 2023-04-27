from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    search_fields = ('username',)
    list_filter = ('age',)


admin.site.register(User, UserAdmin)
