from django.contrib import admin

from . models import Task
admin.site.register(Task)

def __str__(self):
        return self.title