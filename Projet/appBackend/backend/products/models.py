
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
class Laptoop(models.Model):
    Manufacturer = models.CharField(max_length=300)
    Model_Name = models.CharField(max_length=50)
    Category = models.CharField(max_length=150)
    Screen_Size = models.CharField(max_length=150)
    Screen = models.CharField(max_length=100)
    CPU = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    Storage = models.CharField(max_length=100)
    GPU = models.CharField(max_length=100)
    Operating_System = models.CharField(max_length=100)
    Weight = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)

    def __str__(self):
        return self.Manufacturer


