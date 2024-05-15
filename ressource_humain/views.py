from rest_framework import viewsets
from .models import (Grade, TypePoste, Candidat, Profession, Presence, TypeProfession, Holiday, TypeHoliday,
                     TypeEnterprise, Enterprise, Employee, Country, TypeIndustrie, SubventionEmployee, Subvention,
                     Folder, FileFolder, SubFolder, Devise, Status, SalaryEmployee, TypePayment,
                     PointagePresenceEmployee, Payment, SeniorityEmployee, Poste, Department, GeographicPosition,
                     CurriculumVitae, EvaluationEmployee, NoteCritere, CritereEvaluation, EvaluationObjectif,
                     Evaluation, Periode, Saison)
from .serializers import (GradeSerializer, TypePosteSerializer, CandidatSerializer, ProfessionSerializer,
                          PresenceSerializer, TypeProfessionSerializer, HolidaySerializer, TypeHolidaySerializer,
                          TypeEnterpriseSerializer, EnterpriseSerializer, EmployeeSerializer, CountrySerializer,
                          TypeIndustrieSerializer, SubventionEmployeeSerializer, SubventionSerializer,
                          FolderSerializer, FileFolderSerializer, SubFolderSerializer, DeviseSerializer,
                          StatutSerializer, SalaryEmployeeSerializer, TypePaymentSerializer,
                          PointagePresenceEmployeeSerializer, PaymentSerializer, SeniorityEmployeeSerializer,
                          PosteSerializer, DepartmentSerializer, GeographicPositionSerializer,
                          CurriculumVitaeSerializer, EvaluationEmployeeSerializer, NoteCritereSerializer,
                          CritereEvaluationSerializer, EvaluationObjectifSerializer,
                          EvaluationSerializer, PeriodeSerializer, SaisonSerializer)


# Create your views here.


class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class TypePosteViewSet(viewsets.ModelViewSet):
    serializer_class = TypePosteSerializer
    queryset = TypePoste.objects.all()


class CandidatViewSet(viewsets.ModelViewSet):
    serializer_class = CandidatSerializer
    queryset = Candidat.objects.all()


class ProfessionViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class PresenceViewSet(viewsets.ModelViewSet):
    serializer_class = PresenceSerializer
    queryset = Presence.objects.all()


class TypeProfessionViewSet(viewsets.ModelViewSet):
    serializer_class = TypeProfessionSerializer
    queryset = TypeProfession.objects.all()


class HolidayViewSet(viewsets.ModelViewSet):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()


class TypeHolidayViewSet(viewsets.ModelViewSet):
    serializer_class = TypeHolidaySerializer
    queryset = TypeHoliday.objects.all()


class TypeEnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = TypeEnterpriseSerializer
    queryset = TypeEnterprise.objects.all()


class EnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = EnterpriseSerializer
    queryset = Enterprise.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class TypeIndustrieViewSet(viewsets.ModelViewSet):
    serializer_class = TypeIndustrieSerializer
    queryset = TypeIndustrie.objects.all()


class SubventionEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = SubventionEmployeeSerializer
    queryset = SubventionEmployee.objects.all()


class SubventionViewSet(viewsets.ModelViewSet):
    serializer_class = SubventionSerializer
    queryset = Subvention.objects.all()


class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()


class FileFolderViewSet(viewsets.ModelViewSet):
    serializer_class = FileFolderSerializer
    queryset = FileFolder.objects.all()


class SubFolderViewSet(viewsets.ModelViewSet):
    serializer_class = SubFolderSerializer
    queryset = SubFolder.objects.all()


class DeviseViewSet(viewsets.ModelViewSet):
    serializer_class = DeviseSerializer
    queryset = Devise.objects.all()


class StatutViewSet(viewsets.ModelViewSet):
    serializer_class = StatutSerializer
    queryset = Status.objects.all()


class SalaryEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = SalaryEmployeeSerializer
    queryset = SalaryEmployee.objects.all()


class PointagePresenceEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = PointagePresenceEmployeeSerializer
    queryset = PointagePresenceEmployee.objects.all()


class TypePaymentViewSet(viewsets.ModelViewSet):
    serializer_class = TypePaymentSerializer
    queryset = TypePayment.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class SeniorityEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = SeniorityEmployeeSerializer
    queryset = SeniorityEmployee.objects.all()


class PosteViewSet(viewsets.ModelViewSet):
    serializer_class = PosteSerializer
    queryset = Poste.objects.all()


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class GeographicPositionViewSet(viewsets.ModelViewSet):
    serializer_class = GeographicPositionSerializer
    queryset = GeographicPosition.objects.all()


class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    serializer_class = CurriculumVitaeSerializer
    queryset = CurriculumVitae.objects.all()


class EvaluationEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluationEmployeeSerializer
    queryset = EvaluationEmployee.objects.all()


class NoteCritereViewSet(viewsets.ModelViewSet):
    serializer_class = NoteCritereSerializer
    queryset = NoteCritere.objects.all()


class CritereEvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = CritereEvaluationSerializer
    queryset = CritereEvaluation.objects.all()


class EvaluationObjectifViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluationObjectifSerializer
    queryset = EvaluationObjectif.objects.all()


class EvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.all()


class PeriodeViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodeSerializer
    queryset = Periode.objects.all()


class SaisonViewSet(viewsets.ModelViewSet):
    serializer_class = SaisonSerializer
    queryset = Saison.objects.all()

