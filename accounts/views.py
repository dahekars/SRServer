from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from mainserver.models import dispatch_name_1

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            add_user = dispatch_name_1(name=username, employee_number=form.cleaned_data['employee_number'], email_address=form.cleaned_data['email'])
            add_user.save()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/srform/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

