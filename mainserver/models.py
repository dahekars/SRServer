import email
from django.db import models

# Create your models here.

### secondary type
class dispatch_name_1(models.Model):
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=4)
    email_address = models.EmailField(max_length=254)
    def __str__(self):
        return self.name 

class Srlistofdispatcher(models.Model):
    action_choice = [
        ('Auto', 'Auto'),
        ('Manual', 'Manual'),
        ('Deny', 'Deny')
    ]
    dispatch_name_of_sr = models.ForeignKey(dispatch_name_1, on_delete=models.CASCADE)
    sr_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True)
    serivce_tag = models.CharField(max_length=7)
    action_taken = models.CharField(choices=action_choice, max_length=10, default='Auto')
    
    class Meta:
        ordering = ('-date_created',)
    def __str__(self):
        return self.sr_number