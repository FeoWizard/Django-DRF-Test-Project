from rest_framework import serializers
from .models        import EmployeesModel, DepartmentsModel
from .validators    import EmployeesValidator


class EmployeesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeesModel
        fields = "__all__"


    def create(self, validated_data):
        model_instance = EmployeesModel(**validated_data)
        EmployeesValidator.validate_drf(model_instance)
        return EmployeesModel.objects.create(**validated_data)


class DepartmentsModelSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField(read_only = True, label = "Количество сотрудников")
    full_salary     = serializers.DecimalField(read_only = True, max_digits = 20, decimal_places = 2, label = "Суммарный оклад")

    class Meta:
        model  = DepartmentsModel
        fields = [ "title",
                   "director",
                   "employees_count",
                   "full_salary" ]