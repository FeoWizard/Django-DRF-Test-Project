from django.contrib import admin
from .models import EmployeesModel, DepartmentsModel, ProjectsModel


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


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ( "title",
                     "director" )


admin.site.register(EmployeesModel,   EmployeesAdmin)
admin.site.register(DepartmentsModel, DepartmentAdmin)
admin.site.register(ProjectsModel,    ProjectsAdmin)
