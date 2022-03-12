from django.shortcuts import render, redirect
from .forms import SrForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Srlistofdispatcher

# Create your views here.
def index(request):
    return render(request, 'mainserver/base.html', {})

def home(request):
    all_sr = Srlistofdispatcher.objects.all()
    return render(request, 'mainserver/home.html', {'ls': all_sr})


def srform_page(request):

    return render(request, 'mainserver/srform.html', {'form': SrForm()})



