from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        #send an email
        send_mail(
            'message form website  ' + subject ,  #subject
             message + 'from'+ name + 'with a email id '+ email, #message
             #from email
            ['mevitechnologies@gmail.com','support@mevitechnologies.com'], #to email

        )
        zip={'name':name,'email':email,'subject':subject,'response':'Your message has been sent. Thank you!'}
        return render(request,'contact.html',zip)
    else:
        return render(request,'contact.html')

