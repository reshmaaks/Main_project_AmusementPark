from django.contrib import admin
from.models import *
from django.contrib.auth.models import Group
# from django.contrib.auth.models import 
 # Register your models here.
class RideAdmin(admin.ModelAdmin):
    list_display=['name','available','created','updated']
    list_editable=['available']
    list_per_page=20


    
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Rides,RideAdmin)
# admin.site.register(Group)
admin.site.register(Account)
admin.site.register(Profile)
admin.site.unregister(Group)



