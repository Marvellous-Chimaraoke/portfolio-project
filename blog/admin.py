from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Blog, BlogAdmin)
