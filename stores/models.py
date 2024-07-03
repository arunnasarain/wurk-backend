from django.db import models


# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.group.name} - ({self.name})"

    class Meta:
        db_table = 'store'
