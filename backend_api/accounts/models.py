from django.db import models
from django.contrib.auth.models import AbstractUser
from organisation.models import Organisation


class User(AbstractUser):
    # exclude fields from AbstractUser
    date_joined = None
    last_login = None
    email = None

    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    ROLE = (
        ('SUPERUSER', 'SUPERUSER'),
        ('ADMIN', 'ADMIN'),
        ('GENERAL EMPLOYEE', 'GENERAL EMPLOYEE'),
    )
    Job_tittle = (
        ('DATABASE OFFICER', 'DATABASE OFFICER'),
        ('PROGRAMS MANAGER', 'PROGRAMS MANAGER'),
        ('PROGRAMS COORDINATOR', 'PROGRAMS COORDINATOR'),
        ('COORDINATOR', 'COORDINATOR'),
        ('MEAL OFFICER', 'MEAL OFFICER'),
        ('ASSISTANT MEAL COORDINATOR', 'ASSISTANT MEAL COORDINATOR'),
        ('FOOD SECURITY AND LIVELIHOODS COORDINATOR', 'FOOD SECURITY AND LIVELIHOODS COORDINATOR'),
        ('SENIOR FIELD OFFICER', 'SENIOR FIELD OFFICER'),
        ('FIELD OFFICER', 'FIELD OFFICER'),
        ('DATA CAPTURE CLERK', 'DATA CAPTURE CLERK'),
    )
    Employment_status = (
        ('FULL TIME', 'FULL TIME'),
        ('PART TIME', 'PART TIME'),
        ('CONTRACT', 'CONTRACT'),
    )
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('RESIGNED', 'RESIGNED'),
        ('DISMISSED', 'DISMISSED'),
        ('ON LEAVE', 'ON LEAVE'),
        ('LEFT ORGANISATION', 'LEFT ORGANISATION'),
    )
    organisation = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_names = models.CharField(max_length=50, blank=True, null=True)
    employeeNumber = models.CharField(max_length=30, unique=True, blank=True, null=True)
    username = models.CharField(max_length=25, unique=True, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True, choices=ROLE)
    gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER)
    company_email = models.EmailField(blank=True, null=True)
    altEmail = models.EmailField(blank=True, null=True, help_text="personal Email apart from the company email ")
    phone_number_1 = models.CharField(max_length=25, blank=True, null=True)
    phone_number_2 = models.CharField(max_length=25, blank=True, null=True)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    job_tittle = models.CharField(max_length=200, blank=True, null=True, choices=Job_tittle)
    date_joined = models.DateField(blank=True, null=True, help_text="The date the employee joined the organisation")
    date_created = models.DateField(auto_now_add=True, blank=True, null=True, help_text="The date the employee was enrolled on the organisation's system")
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, choices=STATUS)
    employment_status = models.CharField(max_length=200, blank=True, null=True, choices=Employment_status)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'company_email'

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

