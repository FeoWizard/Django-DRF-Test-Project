from django.contrib import admin
from .models import EmployeesModel, DepartmentsModel


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ( "title",
                     "director" )


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ( "surname",
                     "name",
                     "patronymic",
                     "age",
                     "position",
                     "salary",
                     "photo",
                     "department" )


admin.site.register(EmployeesModel,   EmployeesAdmin)
admin.site.register(DepartmentsModel, DepartmentAdmin)
