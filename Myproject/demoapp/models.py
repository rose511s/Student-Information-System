from django.db import models

# Create your models here.
#sara database ka kam hota h
#ORM stands for Object Relational Mapper

class student_info(models.Model):
  #id=variable
  id=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=50)
  email=models.CharField(max_length=100)
  contactno=models.CharField(max_length=15)




"""
create database student;
saara database ka kam hota hai

"""
