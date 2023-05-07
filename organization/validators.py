from django.core.exceptions    import ValidationError as DJANGO_VALIDATION_ERROR
from rest_framework.exceptions import ValidationError as DRF_VALIDATION_ERROR


class EmployeesValidator:
    @staticmethod
    def __validate(instance):
        if (instance.position == instance.Position.DIRECTOR) \
                and (instance.department.director) and (instance.department.director != instance):
            return False

        else:
            return True


    @staticmethod
    def validate_web(instance):
        if (not EmployeesValidator.__validate(instance)):
            raise DJANGO_VALIDATION_ERROR("Директор департамента уже назначен, невозможно сделать данного сотрудника директором! "
                                          "Измените должность текущего директора департамента и повторите попытку.")


    @staticmethod
    def validate_drf(instance):
        if (not EmployeesValidator.__validate(instance)):
            raise DRF_VALIDATION_ERROR(
                { "error" : "Директор департамента уже назначен, невозможно сделать данного сотрудника директором! "
                            "Измените должность текущего директора департамента и повторите попытку." } )
