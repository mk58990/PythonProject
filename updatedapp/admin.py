from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Foodsales

# Register your models here.
class FoodsalesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['OrderDate','Region','City','Category','Product','Quantity','UnitPrice']

admin.site.register(Foodsales,FoodsalesAdmin)


