from django.contrib import admin
from board.models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class WritingAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Writing, WritingAdmin)