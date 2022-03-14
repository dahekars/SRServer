from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SrForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Srlistofdispatcher, dispatch_name_1
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request, 'mainserver/base.html', {})

def home(request):
    all_data = Srlistofdispatcher.objects.all()
    return render(request, 'mainserver/home.html', {'ls': all_data})

    #testing
#    if User.is_authenticated:
#        if dispatch_name_1.objects.get(name=request.user):
#            user = request.user
#            user_name = dispatch_name_1.objects.get(name=user)
#            today = datetime.today() - timedelta(days=1)
#            all_sr_for_today = Srlistofdispatcher.objects.filter(dispatch_name_of_sr= user_name, date_created__gte=today) 
#            return render(request, 'mainserver/home.html', {'ls': all_sr_for_today})
#        if not dispatch_name_1.objects.get(name=request.user):
#            all_data = Srlistofdispatcher.objects.all()
#            return render(request, 'mainserver/home.html', {'ls': all_data})
#    
#    elif User.is_anonymous:
#        all_data = Srlistofdispatcher.objects.all()
#        return render(request, 'mainserver/home.html', {'ls': all_data})


def srform_page(request):
    if request.method == 'POST':
        form = SrForm(request.POST)
        if form.is_valid():
            sr = form.cleaned_data['sr_number']
            service_tag = form.cleaned_data['serivce_tag']
            #dispatcher = form.cleaned_data['dispatch_name_of_sr']
            action_taken = form.cleaned_data['action_taken']

            add_process = Srlistofdispatcher(sr_number=sr, serivce_tag=service_tag, action_taken=action_taken, dispatch_name_of_sr= dispatch_name_1.objects.get(name=request.user))
            add_process.save()

        return HttpResponseRedirect('/srform/')
    else:
        form = SrForm()
    
    user = request.user
    user_name = dispatch_name_1.objects.get(name=user)
    today = datetime.today() - timedelta(days=1)
    latest_5 =Srlistofdispatcher.objects.filter(dispatch_name_of_sr= user_name, date_created__gte=today) [:5]
    return render(request, 'mainserver/srform.html', {'form': form, 'latest_5': latest_5})
