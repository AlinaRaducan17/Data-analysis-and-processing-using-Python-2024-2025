from django.contrib import admin

# Register your models here.

from .models import BlogPost

#inregistrare BlogPost
admin.site.register(BlogPost)