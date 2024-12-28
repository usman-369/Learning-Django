from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class ContactBook(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
