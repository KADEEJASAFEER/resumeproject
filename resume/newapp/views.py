from django.shortcuts import render, redirect
from newapp.forms import CreateResumeForm,RegistrationForm,ResumeEditForm
from newapp.models import ResumeModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginpage')
def CreateResume(request):
    form=CreateResumeForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form=CreateResumeForm(request.POST,request.FILES)
        print("pst")
        if form.is_valid():
            print("inside save")
            form.save()
            return redirect("viewresume")
    return render(request,"resume/create_resume.html",context)

def register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
        else:
            context["form"]=form
            return render(request, "resume/registration.html", context)

    return render(request,"resume/registration.html",context)


def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        print(username,",",password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("loginpage")
    return render(request,"resume/loginpage.html")

def logoutPage(request):
    logout(request)
    return redirect("loginpage")

def index(request):
    obj = ResumeModel.objects.all()
    context = {}
    context["res"] = obj
    return render(request,"resume/indexpage.html")


@login_required(login_url='loginpage')
def viewResume(request):
    obj=ResumeModel.objects.filter(fullname=request.user)
    context={}
    context["res"]=obj
    return render(request,"resume/view_resume.html",context)

def editResume(request,pk):
    obj=ResumeModel.objects.get(id=pk)
    form=ResumeEditForm(instance=obj)
    context={}
    context["form"]=form
    if request.method == "POST":
        form=CreateResumeForm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewresume")
    return render(request,"resume/edit_resume.html",context)

def deleteResume(request,pk):
    obj = ResumeModel.objects.get(id=pk).delete()
    return redirect("createresume")


