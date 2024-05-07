from django.contrib import admin
from .models import (Grade, TypePoste, Candidat, Profession, Presence, TypeProfession, Holiday, TypeHoliday,
                     TypeEnterprise, Enterprise, Employee, Country, TypeIndustrie, SubventionEmployee, Subvention,
                     Folder, FileFolder, SubFolder, Devise, Status, SalaryEmployee, TypePayment,
                     PointagePresenceEmployee, Payment, SeniorityEmployee, Poste, Department, GeographicPosition,
                     CurriculumVitae)
# Register your models here.

admin.site.register(Candidat)
admin.site.register(Profession)
admin.site.register(Holiday)
admin.site.register(Grade)
admin.site.register(TypePoste)
admin.site.register(Presence)
admin.site.register(TypeProfession)
admin.site.register(TypeHoliday)
admin.site.register(TypeEnterprise)
admin.site.register(Enterprise)
admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(TypeIndustrie)
admin.site.register(SubventionEmployee)
admin.site.register(Subvention)
admin.site.register(Folder)
admin.site.register(FileFolder)
admin.site.register(SubFolder)
admin.site.register(Devise)
admin.site.register(SalaryEmployee)
admin.site.register(Status)
admin.site.register(TypePayment)
admin.site.register(PointagePresenceEmployee)
admin.site.register(Payment)
admin.site.register(SeniorityEmployee)
admin.site.register(Poste)
admin.site.register(Department)
admin.site.register(GeographicPosition)
admin.site.register(CurriculumVitae)
