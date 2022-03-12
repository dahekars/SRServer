import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

# Sr form for data stroing in database
class SrForm(forms.Form):
    action_choice = [
    ('Auto', 'Auto'),
    ('Manual', 'Manual'),
    ('Deny', 'Deny')]
    sr_number = forms.CharField(max_length=12, label='SR Number',required=True)
    serivce_tag = forms.CharField(max_length=7, label='Service Tag', required = True)
    #dispatch_name_of_sr = forms.CharField(max_length=20, label='Dispatch Name', required=False)
    action_taken = forms.ChoiceField(choices =action_choice, label='Action Taken', required=False)
    #date_created = forms.DateTimeField(label='Date Created')
