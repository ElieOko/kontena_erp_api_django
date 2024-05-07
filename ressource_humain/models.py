from django.db import models


class NoOccurentData(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=40, blank=True, null=False)

    class Meta:
        abstract = True


class Status(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Devise(NoOccurentData):
    code = models.CharField(max_length=6, null=False, blank=True)
    symbole = models.CharField(max_length=5, null=True, blank=True)
    taux = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.code}({self.name})'


class Grade(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class TypePoste(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Folder(NoOccurentData):
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class SubFolder(NoOccurentData):
    fk_folder = models.OneToOneField(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class TypeProfession(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Profession(NoOccurentData):
    fk_type_profession = models.OneToOneField(TypeProfession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fk_type_profession.name}({self.name})'


class Country(NoOccurentData):
    code_country = models.CharField(max_length=5, blank=True, null=False)

    def __str__(self):
        return f'{self.name}({self.code_country})'


class GeographicPosition(NoOccurentData):
    name = None
    city = models.CharField(max_length=25, blank=True, null=False)
    fk_country = models.OneToOneField(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}({self.name})'


class TypeEnterprise(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class TypeIndustrie(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Enterprise(NoOccurentData):
    fk_type_industrie = models.OneToOneField(TypeIndustrie, on_delete=models.CASCADE)
    fk_type_enterprise = models.OneToOneField(TypeEnterprise, on_delete=models.CASCADE)


class Candidat(NoOccurentData):
    name = None
    first_name = models.CharField(max_length=40, blank=True, null=False)
    last_name = models.CharField(max_length=40, blank=True, null=False)
    is_valid = models.BooleanField(default=False)
    fk_profession = models.OneToOneField(Profession, on_delete=models.CASCADE)


class CurriculumVitae(NoOccurentData):
    fk_candidat = models.OneToOneField(Candidat, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/")


class FileFolder(NoOccurentData):
    name = None
    fk_subfolder = models.OneToOneField(SubFolder, null=True, on_delete=models.CASCADE)
    fk_folder = models.OneToOneField(Folder, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/")


class Poste(NoOccurentData):
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_type_poste = models.OneToOneField(TypePoste, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.fk_type_poste.name})'


class Department(NoOccurentData):
    description = models.CharField(max_length=255, blank=True, null=True)


class Employee(NoOccurentData):
    name = None
    first_name = models.CharField(max_length=40, blank=True, null=False)
    last_name = models.CharField(max_length=40, blank=True, null=False)
    date_birthday = models.DateTimeField(null=False)
    marital_status = models.CharField(max_length=12, blank=True, null=False)
    level_of_study = models.CharField(max_length=255, blank=True, null=False)
    fk_poste = models.OneToOneField(Poste, on_delete=models.CASCADE)


class SeniorityEmployee(NoOccurentData):
    name = None
    fk_employee = models.OneToOneField(Employee, on_delete=models.CASCADE, unique=True)
    seniority_old = models.IntegerField(default=0, null=True)
    seniority_mounth = models.IntegerField(default=0, null=True)


class TypeHoliday(NoOccurentData):
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Holiday(NoOccurentData):
    fk_type_holiday = models.OneToOneField(TypeHoliday, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)


class EmployeeHoliday(NoOccurentData):
    fk_employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    fk_holiday = models.OneToOneField(Holiday, on_delete=models.CASCADE)
    motif = models.CharField(max_length=255, blank=True, null=False)
    fk_status = models.OneToOneField(Status, on_delete=models.CASCADE)
    is_payment = models.BooleanField(default=False)
    number_day = models.IntegerField(default=1)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()


class TypePayment(NoOccurentData):
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Payment(NoOccurentData):
    fk_type_payment = models.OneToOneField(TypePayment, on_delete=models.CASCADE)
    amount_budget = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    fk_status = models.OneToOneField(Status, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    motif = models.CharField(max_length=255, blank=True, null=False)


class SalaryEmployee(NoOccurentData):
    fk_employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    amount_salary = models.DecimalField(decimal_places=2, default=0.0, max_digits=10)
    is_payment = models.BooleanField(default=False)


class Subvention(NoOccurentData):
    # https://www.leganet.cd/Legislation/DroitSocial/Loi%2016.010.15.07.html
    amount_subvention = models.DecimalField(decimal_places=2, default=0.0, max_digits=10)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.amount_subvention}({self.name})'


class SubventionEmployee(NoOccurentData):
    name = None
    fk_employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    fk_subvention = models.OneToOneField(Subvention, on_delete=models.CASCADE)


class Presence(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class PointagePresenceEmployee(NoOccurentData):
    fk_employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    fk_presence = models.OneToOneField(Presence, on_delete=models.CASCADE)
    is_presence = models.BooleanField(default=False)



