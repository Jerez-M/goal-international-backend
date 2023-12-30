from django.db import models
from django.contrib.auth.models import AbstractUser
from organisation.models import Organisation


class User(AbstractUser):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )

    ROLE = (
        ('SUPERUSER', 'SUPERUSER'),
        ('ADMIN', 'ADMIN'),
        ('ADMIN-TEACHER', 'ADMIN-TEACHER'),
        ('TEACHER', 'TEACHER'),
        ('STUDENT', 'STUDENT'),
        ('PARENT', 'PARENT'),
    )
    tenant = models.ForeignKey(Organisation, blank=True, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    middleNames = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=25, unique=True, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True, choices=ROLE)
    gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True)
    phoneNumber = models.CharField(max_length=25, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

