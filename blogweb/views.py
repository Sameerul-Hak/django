from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from  django.http import HttpResponse
from .models import addblogs,Projects
from .form import ProjectsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from twilio.rest import Client
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
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
            # Save the form data
            form.save()

            # Send an email notification
            subject = 'New project submitted'
            message = f"New project submitted: regarding {form.cleaned_data['project_name']}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['sameerulhakofficial@gmail.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Return a success response
            return render(request,'blogweb/index.html')
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