from django.urls import path, include

from organization.views import EmployeesViewSet, DepartmentsView, photo_view, ProjectsView
from rest_framework     import routers

router = routers.DefaultRouter()
router.register("departments", DepartmentsView,  basename = "Departments")
router.register("employees",   EmployeesViewSet, basename = "Employees")
router.register("projects",    ProjectsView,     basename = "Projects")


urlpatterns = [
    *router.urls,
    path("media/<filename>", photo_view,                     name = "photo_view"),
    path("auth/",            include('rest_framework.urls'), name = "auth"),
]