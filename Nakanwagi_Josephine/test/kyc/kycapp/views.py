from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    pr_title = 'kyc Registration form'
    firstName = ''
    gender = ''
    return render(            
        request,
        'index.html',                   
        {'pr_title': pr_title, 'firstName':firstName, 'gender':gender}
    )                                                                                   
                
def register(request):

    return render(request, 'register.html')

def customerRegistration(request):
    firstName= request.POST['firstName']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    registration=[
            firstName,email,password,gender
        ]
    print(registration)
    return render(request, 'index.html', {'firstName': firstName})


