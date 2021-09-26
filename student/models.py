from django.db import models
from django.db.models.fields import CharField, DateField


# Create your models here.
class Student(models.Model):
    name = CharField(max_length=256)
    birthday = DateField()

    def __str__(self) -> str:
        return self.name
