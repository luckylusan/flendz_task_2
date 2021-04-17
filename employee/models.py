from django.db import models

# Create your models here.

class employee(models.Model):
    emp_id = models.IntegerField(primary_key=True,null=False)
    emp_name = models.CharField(max_length=200,null=False)
    emp_designation = models.CharField(max_length=200,null=False)
    emp_doj = models.DateField(null=False)

    class Meta:
        db_table = 'employees'
