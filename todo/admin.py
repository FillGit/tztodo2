from django.contrib import admin
from django.contrib.auth.models import Permission
from guardian.admin import GuardedModelAdmin

# Register your models here.
from .models import Desk, Company

#admin.site.register(Desks)

#admin.site.register(Profile)

#admin.site.register(CompanyName)

"""@admin.register(Company)
class CompanyAdmin(admin.GuardedModelAdmin):
    list_display = ('name','id')"""
class CompanyAdmin(GuardedModelAdmin):
    list_display = ('name','id')

admin.site.register(Company, CompanyAdmin)

@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('id','due_date','task','company_name')

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name','content_type','codename')


#@admin.register(Session)
#class SessionAdmin(admin.ModelAdmin):
#    list_display = ('username','idsession', 'date_idsession', 'active_for_company')
