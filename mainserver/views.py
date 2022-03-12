from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SrForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Srlistofdispatcher, dispatch_name_1

# Create your views here.
def index(request):
    return render(request, 'mainserver/base.html', {})

def home(request):
    all_sr = Srlistofdispatcher.objects.all()
    return render(request, 'mainserver/home.html', {'ls': all_sr})


def srform_page(request):
    if request.method == 'POST':
        form = SrForm(request.POST)
        if form.is_valid():
            sr = form.cleaned_data['sr_number']
            service_tag = form.cleaned_data['serivce_tag']
            #dispatcher = form.cleaned_data['dispatch_name_of_sr']
            action_taken = form.cleaned_data['action_taken']

            add_process = Srlistofdispatcher(sr_number=sr, serivce_tag=service_tag, action_taken=action_taken, dispatch_name_of_sr= dispatch_name_1.objects.get(id = 1))
            add_process.save()
        return HttpResponseRedirect('/srform/')
    else:
        form = SrForm()
    return render(request, 'mainserver/srform.html', {'form': form})
