from django.contrib import admin
from .models import yazi


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_filter = ('created_date', )


# Register your models here.
admin.site.register(yazi, BlogAdmin)
