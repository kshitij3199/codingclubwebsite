from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    head = models.CharField(max_length=256)
    #location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    #age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    github = models.CharField(max_length=256,default="N.A.")
    mobile = models.CharField(max_length=256,default="N.A.")
    email = models.EmailField(default="N.A.")
    interest = models.CharField(max_length=256,default="N.A.")
    skills = models.CharField(max_length=256,default="N.A.")
    #project_current = models.CharField(max_length=256,default="not available")
    def __str__(self):
        return self.name
