from django.contrib import admin
from . models import *

# Register your models here.
class categadmin(admin.ModelAdmin):
   prepopulated_fields= {'slug':('name',)}
   list_display=['name','slug']
admin.site.register(categ,categadmin)


class prdctadmin(admin.ModelAdmin):
   prepopulated_fields={'slug':('name',)}
   list_display = ['name','slug', 'price', 'stock','img','avialable']
   list_editable = [ 'price', 'img', 'stock','avialable']
admin.site.register(prdct,prdctadmin)


# __________________________________________________________________
# class prodadmin(admin.ModelAdmin):
#    prepopulated_fields={'slug':('name',)}
#    list_display = ['name','slug', 'price', 'stock','img',]
#    list_editable = [ 'price', 'img', 'stock']
# admin.site.register(prod,prodadmin)
# --------------------------------------------------------------------

