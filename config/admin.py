from django.contrib import admin

from config.models import Task, Tag

# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)
