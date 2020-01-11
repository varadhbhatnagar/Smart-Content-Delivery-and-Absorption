from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICES = (('Student', 'Student'), ('Parent', 'Parent'), ('Teacher', 'Teacher'), ('Supervisor', 'Supervisor'))

class Profile(models.Model):
    """!
    @detailed Defines the structure of the table used for storing User Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Role = models.CharField(max_length=18, choices=ROLE_CHOICES)
    Class = models.IntegerField(blank=True)
    Subject = models.CharField(max_length=50, blank=True)
    Section = models.CharField(max_length=2, blank=True)

# class Teacher(models.Model):
#     Teacher_First_Name = models.CharField(max_length=30)
#     Teacher_Last_Name = models.CharField(max_length=30)

#      def __str__(self):
#         return "%s %s" % (self.Teacher_First_Name, self.Teacher_Last_Name)

class Subject(models.Model):

    Subject_Name = models.CharField(max_length=30)
    Class = models.IntegerField()
    Section = models.CharField(max_length=2)
    Teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    CA_Score = models.FloatField()
    CD_Score = models.FloatField()

    def __str__(self):
        return "%s %s %s" % (self.Subject_Name, self.Class, self.Section)
