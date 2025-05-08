from django.contrib import admin

# Register your models here.
from .models import Presentation


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'float_value', 'link')
