from django.contrib import admin
from.models import *
from django.contrib.auth.models import Group
# from django.contrib.auth.models import 
 # Register your models here.
class RideAdmin(admin.ModelAdmin):
    list_display=['name','available','created','updated']
    list_editable=['available']
    list_per_page=20


    
admin.site.register(Rides,RideAdmin)
admin.site.register(Account)
admin.site.register(Adultpackage)
admin.site.register(Childpackage)
admin.site.register(booking)
admin.site.register(amount)

admin.site.unregister(Group)



