import email
from django.db import models

# Create your models here.
class Srdatabase(models.Model):
    action_choice = [
        ('auto', 'auto'),
        ('manual', 'manual'),
        ('deny', 'deny')
    ]
    date_created = models.DateTimeField(auto_now_add=True)
    workorder = models.CharField(max_length=12)
    serivce_tag = models.CharField(max_length=7)
    action_taken = models.CharField(choices=action_choice, max_length=10, default='auto')
    dispatch_name =  models.CharField(max_length=20)
    def __str__(self):
        return self.workorder in {
            self.Srdatabase.date_created, 
            self.Srdatabase.serivce_tag,
            self.Srdatabase.action_taken,
            self.Srdatabase.dispatch_name}

class dispatch_name(models.Model):
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=4)
    email_address = models.EmailField(max_length=254)
    def __str__(self):
        return self.name in {
            self.dispatch_name.name,
            self.dispatch_name.employee_number,
            self.dispatch_name.email_address
            }


### secondary type
class dispatch_name_1(models.Model):
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=4)
    email_address = models.EmailField(max_length=254)
    def __str__(self):
        return self.employee_number 

class Srlistofdispatcher(models.Model):
    action_choice = [
        ('auto', 'auto'),
        ('manual', 'manual'),
        ('deny', 'deny')
    ]
    dispatch_name_of_sr = models.ForeignKey(dispatch_name_1, on_delete=models.CASCADE)
    sr_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True)
    serivce_tag = models.CharField(max_length=7)
    action_taken = models.CharField(choices=action_choice, max_length=10, default='auto')
    def __str__(self):
        return self.sr_number