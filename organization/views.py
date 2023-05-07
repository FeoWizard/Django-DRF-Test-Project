from django.contrib.auth.decorators import login_required
from django.http                    import HttpRequest, FileResponse, HttpResponseNotFound
from django.db.models               import Count, Sum
from rest_framework                 import mixins, permissions, filters
from rest_framework.pagination      import PageNumberPagination
from rest_framework.viewsets        import GenericViewSet
from rest_framework.authentication  import BasicAuthentication, SessionAuthentication
from organization_project.settings  import MEDIA_ROOT
from organization.models            import EmployeesModel, DepartmentsModel
from organization.serializers       import EmployeesModelSerializer, DepartmentsModelSerializer


# Быстрая Web-Вьюха для картинок
@login_required(redirect_field_name = None, login_url = "../admin/")
def photo_view(request: HttpRequest, filename):
    try:
        file = open(f"{MEDIA_ROOT}/{filename}", "rb")

    except FileNotFoundError:
        return HttpResponseNotFound("Not found (404)")

    else:
        return FileResponse(file, as_attachment = False)


class Paginator(PageNumberPagination):
    page_size             = 5
    page_size_query_param = "page_size"  # Позволяем указать произвольный размер страницы


# RetrieveModelMixin и UpdateModelMixin по ТЗ не нужны
class EmployeesViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes     = [ permissions.IsAuthenticated ]
    authentication_classes = [ SessionAuthentication, BasicAuthentication ]
    serializer_class       = EmployeesModelSerializer
    queryset               = EmployeesModel.objects.all()
    pagination_class       = Paginator
    filter_backends        = [ filters.SearchFilter ]
    search_fields          = [ "id", "^surname" ]


class DepartmentsView(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [ permissions.AllowAny ]
    serializer_class   = DepartmentsModelSerializer
    queryset           = DepartmentsModel.objects.annotate( employees_count = Count('Employees'),
                                                            full_salary     = Sum('Employees__salary') )
