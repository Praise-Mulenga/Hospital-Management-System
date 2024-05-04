from django.db import models
from django.utils import timezone

# Create your models here.
class ward(models.Model):
    ward_id = models.CharField(max_length = 4, primary_key = True)
    ward_name = models.CharField(max_length = 25)
    number_beds = models.IntegerField()
    nurse_in_charge = models.CharField(max_length = 20)
    ward_type = models.CharField(max_length = 20, null=True)

    def __str__(self):
        return self.ward_id


class patient(models.Model):
    patient_id = models.CharField(max_length = 2, primary_key=True)
    name = models.CharField(max_length = 30)
    initials = models.CharField(max_length = 2)
    sex = models.CharField(max_length = 1)
    address = models.CharField(max_length = 30)
    post_code = models.CharField(max_length = 3)
    admission = models.DateField()
    DOB = models.DateField()
    ward_id = models.ForeignKey(ward, on_delete=models.CASCADE)
    next_of_kin = models.CharField(max_length = 30, null = True)