from django.contrib import admin

from .models import Bio

admin.site.site_header = 'Chatbot'
admin.site.register(Bio)
