from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from  django.http import HttpResponse
from .models import addblogs,Projects
from .form import ProjectsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from twilio.rest import Client
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request,'blogweb/index.html')

def createblog(request):
    return render(request,'blogweb/createblog.html')

def viewblogs(request):
    datas=addblogs.objects.all()
    print(datas)
    return render(request,'blogweb/viewblogs.html',{'data':datas})


def productdetail(request,id):
    datas=get_object_or_404(addblogs,id=id)
    return render(request,'blogweb/detailblog.html',{'data':datas})
@csrf_protect
def projects_save(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            print(request.POST)
            # Do something with the form data
            form.save()
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"New project submitted:regarding about {form.cleaned_data['project_name']} ",
                from_="+15673671530",
                to="+919944012249"
            )
            print(message.sid)
            return redirect("/home/")
    else:
        form = ProjectsForm()
    return render(request, 'blogweb/projetcs.html', {'form': form})
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            projects=Projects.objects.all()
            return render(request,'blogweb/viewproject.html',{"projects":projects})
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'blogweb/login_project.html')