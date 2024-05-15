from rest_framework import serializers
from .models import (Grade, TypePoste, Candidat, Profession, Presence, TypeProfession, Holiday, TypeHoliday,
                     TypeEnterprise, Enterprise, Employee, Country, TypeIndustrie, SubventionEmployee, Subvention,
                     Folder, FileFolder, SubFolder, Devise, Status, SalaryEmployee, TypePayment,
                     PointagePresenceEmployee, Payment, SeniorityEmployee, Poste, Department, GeographicPosition,
                     CurriculumVitae, EvaluationEmployee, NoteCritere, CritereEvaluation, EvaluationObjectif,
                     Evaluation, Periode, Saison)


class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class DeviseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devise
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class TypePosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePoste
        fields = "__all__"


class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = "__all__"


class TypeProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProfession
        fields = "__all__"


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = "__all__"


class TypeHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeHoliday
        fields = "__all__"


class TypeEnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEnterprise
        fields = "__all__"


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class TypeIndustrieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeIndustrie
        fields = "__all__"


class SubventionEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubventionEmployee
        fields = "__all__"


class SubventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subvention
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class FileFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileFolder
        fields = "__all__"


class SubFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFolder
        fields = "__all__"


class SalaryEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryEmployee
        fields = "__all__"


class TypePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePayment
        fields = "__all__"


class PointagePresenceEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointagePresenceEmployee
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class SeniorityEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeniorityEmployee
        fields = "__all__"


class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class GeographicPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicPosition
        fields = "__all__"


class CurriculumVitaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumVitae
        fields = "__all__"


class EvaluationEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationEmployee
        fields = "__all__"


class NoteCritereSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCritere
        fields = "__all__"


class CritereEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CritereEvaluation
        fields = "__all__"


class EvaluationObjectifSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationObjectif
        fields = "__all__"


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"


class PeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periode
        fields = "__all__"


class SaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saison
        fields = "__all__"


