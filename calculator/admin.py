from django.contrib import admin
from .models import TestData

@admin.register(TestData)
class TestDataAdmin(admin.ModelAdmin):
    list_display = (
        'text1','text2', 'num1'
    )
    search_fields = (
        'text1','text2', 'num1'
    )