from rest_framework import routers
from .views import (GradeViewSet, PosteViewSet, PointagePresenceEmployeeViewSet, TypePosteViewSet, ProfessionViewSet,
                    EmployeeViewSet, TypeHolidayViewSet, HolidayViewSet, SaisonViewSet, PeriodeViewSet,
                    SubventionViewSet, StatutViewSet, SalaryEmployeeViewSet, SeniorityEmployeeViewSet,
                    SubventionEmployeeViewSet, SubFolderViewSet, FolderViewSet, CandidatViewSet, CountryViewSet,
                    CritereEvaluationViewSet, CurriculumVitaeViewSet, NoteCritereViewSet, EnterpriseViewSet,
                    EvaluationViewSet, EvaluationEmployeeViewSet, EvaluationObjectifViewSet, DepartmentViewSet,
                    DeviseViewSet, FileFolderViewSet, PaymentViewSet, TypePaymentViewSet, GeographicPositionViewSet,
                    PresenceViewSet, TypeIndustrieViewSet, TypeEnterpriseViewSet, TypeProfessionViewSet)


router = routers.DefaultRouter()
router.register(r'candidat', CandidatViewSet)
router.register(r'country', CountryViewSet)
router.register(r'critere/evaluation', CritereEvaluationViewSet)
router.register(r'critere/note', NoteCritereViewSet)
router.register(r'curriculum/vitae', CurriculumVitaeViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'devise', DeviseViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'employee/salary', SalaryEmployeeViewSet)
router.register(r'employee/seniority', SeniorityEmployeeViewSet)
router.register(r'employee/subvention', SubventionEmployeeViewSet)
router.register(r'enterprise', EnterpriseViewSet)
router.register(r'enterprise/type', TypeEnterpriseViewSet)
router.register(r'evaluation', EvaluationViewSet)
router.register(r'employee/evaluation', EvaluationEmployeeViewSet)
router.register(r'evaluation/objectif', EvaluationObjectifViewSet)
router.register(r'folder', FolderViewSet)
router.register(r'folder/file', FileFolderViewSet)
router.register(r'folder/sub', SubFolderViewSet)
router.register(r'geographie/position', GeographicPositionViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'holiday', HolidayViewSet)
router.register(r'holiday/type', TypeHolidayViewSet)
router.register(r'industrie/type', TypeIndustrieViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'payment/type', TypePaymentViewSet)
router.register(r'periode', PeriodeViewSet)
router.register(r'poste', PosteViewSet)
router.register(r'poste/type', TypePosteViewSet)
router.register(r'presence', PresenceViewSet)
router.register(r'presence/pointage/employee', PointagePresenceEmployeeViewSet)
router.register(r'profession', ProfessionViewSet)
router.register(r'profession/type', TypeProfessionViewSet)
router.register(r'saison', SaisonViewSet)
router.register(r'status', StatutViewSet)
router.register(r'subvention', SubventionViewSet)
urlpatterns = router.urls
