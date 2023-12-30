from django.db import models
from .organisation_number import generate_organisation_number as x

class Organisation(models.Model):

    ORGANISATION_TYPE_CHOICE = (
        ('NON GOVERNMENTAL ORGANIZATION', 'NON GOVERNMENTAL ORGANIZATION'),
        ('INTERNATIONAL NON-GOVERNMENTAL ORGANIZATION', 'INTERNATIONAL NON-GOVERNMENTAL ORGANIZATION'),
        ('COMMUNITY-BASED ORGANIZATION', 'COMMUNITY-BASED ORGANIZATION'),
        ('GOVERNMENTAL ORGANIZATION', 'GOVERNMENTAL ORGANIZATION'),
        ('SOCIAL ENTERPRISE', 'SOCIAL ENTERPRISE'),
        ('FOUNDATION', 'FOUNDATION'),
        ('HEALTHCARE ORGANIZATION', 'HEALTHCARE ORGANIZATION'),
    )
    organisation_code = 'GI'
    organisation_name = models.CharField(max_length=200, blank=True, null=True)
    # organisation_code = models.CharField(max_length=10, blank=True, default='GI', null=True)
    email_address = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    organisation_type = models.CharField(max_length=25, blank=True, null=True, choices=ORGANISATION_TYPE_CHOICE)
    logo = models.ImageField(upload_to='organisation_logos', default='organisation_logos/default_logo.jpg', blank=True, null=True)
    active = models.BooleanField(default=True)
    organisation_number = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.organisation_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.organisation_number = x(self.organisation_code, str(self.pk), 6, 8)
        super().save(*args, **kwargs)
