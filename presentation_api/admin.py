from django.contrib import admin

# Register your models here.
from .models import Presentation


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',
                    'pdf_file', 'float_value', 'link')
    search_fields = ('title',)
    list_filter = ('float_value',)
    ordering = ('-id',)
