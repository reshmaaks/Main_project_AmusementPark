import csv
from django.contrib import admin
from django.http import HttpResponse
from.models import *
from django.contrib.auth.models import Group
# from django.contrib.auth.models import 
 # Register your models here.
class RideAdmin(admin.ModelAdmin):
    list_display=['name','available','created','updated']
    list_editable=['available']
    list_per_page=20


    
admin.site.register(Rides,RideAdmin)
# admin.site.register(Account)
admin.site.register(Adultpackage)
admin.site.register(Childpackage)
admin.site.register(booking)
admin.site.register(amount)
admin.site.register(Payment)
admin.site.register(Placed_Booking)


admin.site.unregister(Group)




def export_reg(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registration.csv"'
    writer = csv.writer(response)
    writer.writerow(['User Name','First Name','Last Name','Email','Phone'])
    registration = queryset.values_list('username','first_name','last_name','email','phone')
    for i in registration:
        writer.writerow(i)
    return response


export_reg.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','phone']
    actions = [export_reg]
admin.site.register(Account,RegAdmin)



