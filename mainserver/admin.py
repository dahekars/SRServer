from django.contrib import admin
from .models import Srdatabase, dispatch_name, dispatch_name_1, Srlistofdispatcher

# Register your models here.
#admin.site.register(Srdatabase)
#admin.site.register(dispatch_name)
#admin.site.register(dispatch_name_1)
#admin.site.register(Srlistofdispatcher)

@admin.register(Srdatabase)
class SrdatabaseAdmin(admin.ModelAdmin):
    list_display = ('workorder', 'serivce_tag', 'action_taken', 'dispatch_name')
    list_filter = ('action_taken', 'dispatch_name')
    search_fields = ('workorder', 'serivce_tag')

@admin.register(dispatch_name)
class dispatch_nameAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_number', 'email_address')
    list_filter = ('name', 'employee_number', 'email_address')
    search_fields = ('name', 'employee_number', 'email_address')

@admin.register(dispatch_name_1)
class dispatch_name_1Admin(admin.ModelAdmin):
    list_display = ('name', 'employee_number', 'email_address')
    list_filter = ('name', 'employee_number', 'email_address')
    search_fields = ('name', 'employee_number', 'email_address')

@admin.register(Srlistofdispatcher)
class SrlistofdispatcherAdmin(admin.ModelAdmin):
    list_display = ('sr_number', 'action_taken', 'dispatch_name_of_sr','date_created')
    list_filter = ('action_taken', 'dispatch_name_of_sr')
    search_fields = ('sr_number', 'action_taken', 'dispatch_name_of_sr')

