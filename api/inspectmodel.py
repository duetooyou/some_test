# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='SALARY')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Houses(models.Model):
    cost = models.IntegerField(db_column='COST')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='USER_ID',
                             related_name='houses')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'houses'
