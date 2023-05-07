from django.db                     import models
from django.utils.translation      import gettext_lazy as _
from organization_project.settings import MEDIA_ROOT
from .validators                   import EmployeesValidator


class EmployeesModel(models.Model):
    class Meta:
        verbose_name        = "Сотрудник"
        verbose_name_plural = "Сотрудники"


    class Position(models.TextChoices):
        DIRECTOR = 'Director', _('Директор')
        MANAGER  = 'Manager',  _('Менеджер')
        WORKER   = 'Worker',   _('Рабочий')


    id         = models.AutoField(primary_key = True, unique = True)
    surname    = models.CharField(verbose_name                 = "Фамилия",     max_length = 100, null = False, blank = False, db_index = True)
    name       = models.CharField(verbose_name                 = "Имя",         max_length = 100, null = False, blank = False)
    patronymic = models.CharField(verbose_name                 = "Отчество",    max_length = 100, null = False, blank = False)
    age        = models.PositiveSmallIntegerField(verbose_name = "Возраст",     null = False, blank = False)
    position   = models.CharField(verbose_name                 = "Должность",   choices = Position.choices, null = False, blank = False, max_length = 200)
    salary     = models.DecimalField(verbose_name              = "Оклад",       max_digits = 10, decimal_places = 2, null = False, blank = False)
    photo      = models.ImageField(verbose_name                = "Фото",        upload_to = MEDIA_ROOT, null = True, blank = True)
    department = models.ForeignKey(verbose_name                = "Департамент", to = "organization.DepartmentsModel",
                                   on_delete = models.CASCADE, related_name = "Employees", null = False, blank = False)


    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


    def validate_unique(self, **kwargs):
        super(EmployeesModel, self).validate_unique(**kwargs)
        EmployeesValidator.validate_web(self)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Автоматом убираем директора при переназначении и подставляем директора в таблицу Departments
        department = DepartmentsModel.objects.filter(director = self).first()
        if (department):
            department.director = None
            department.save()

        if (self.position == self.Position.DIRECTOR):
            department          = DepartmentsModel.objects.get(id = self.department.id)
            department.director = self
            department.save()


class DepartmentsModel(models.Model):
    class Meta:
        verbose_name        = "Департамент"
        verbose_name_plural = "Департаменты"


    id       = models.AutoField(primary_key = True, unique = True)
    title    = models.CharField(verbose_name     = "Название", null = False, blank = False, max_length = 200)
    director = models.OneToOneField(verbose_name = "Директор", to = EmployeesModel, on_delete = models.SET_NULL,
                                    null = True, blank = True, related_name = "director", editable = False)


    def __str__(self):
        return self.title