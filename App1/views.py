from django.shortcuts import render
from App1.forms import studentRegistration
from App1.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

def Home(request):
    stuInfo=User.objects.all()
    if request.method=="POST":
        stuForm=studentRegistration(request.POST)
        if stuForm.is_valid():
            nm=stuForm.cleaned_data['name']
            em=stuForm.cleaned_data['email']
            passw=stuForm.cleaned_data['password']
            data=User(name=nm,email=em,password=passw)
            data.save()
            # messages.add_message(request,messages.SUCCESS,'Your Data Has Been Added !!!')
            messages.success(request,'Your Data Has Been Added Succesfully ')
    else:
        stuForm=studentRegistration()
    return render(request,'App1/Home.html',{'form':stuForm,'stuInfo':stuInfo})

def Update(request,id):
    if request.method=='POST':
        stuData=User.objects.get(pk=id)
        stuForm=studentRegistration(request.POST,instance=stuData)
        if stuForm.is_valid():
            stuForm.save()
            return HttpResponseRedirect('/')
    else:
        stuForm=studentRegistration()
    context={
        'form':stuForm
    }
    return render(request,'App1/Update.html',context)

def Delete(request,id):
    deleteData=User.objects.get(pk=id)
    if request.method=="POST":
        deleteData.delete()
        return HttpResponseRedirect('/')
    return render(request,'App1/Delete.html')



    
