from django.db import models
from employee.models import employee

# Create your models here.


class tasks(models.Model):
    task_name = models.CharField(max_length=200)
    task_start_date = models.DateField()
    task_end_date = models.DateField()
    task_completion_time = models.IntegerField()
    assigned = models.ForeignKey(employee,null=True)