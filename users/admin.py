from django.contrib import admin

# Register your models here.
from users.models import Company,Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name','location')
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company_id')
    

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
