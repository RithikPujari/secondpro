from django.contrib import admin
from .models import Drug

class DrugAdmin(admin.ModelAdmin):
    list_display=['Did','Dname','Duse']
admin.site.register(Drug,DrugAdmin)