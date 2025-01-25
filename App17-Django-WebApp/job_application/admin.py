from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email','occupation')
    search_fields = ('first_name', 'last_name', 'email',)
    list_filter = ('date','occupation',)
    ordering = ('id',)
    readonly_fields = ('occupation',)

admin.site.register(Form, FormAdmin)
