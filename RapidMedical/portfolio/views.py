from django.shortcuts import render
from .forms import contactformemail
from django.core.mail import send_mail

def welcome(request):
    if request.method == "GET":
        form=contactformemail() 
    else:
        form=contactformemail(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            fromemail=form.cleaned_data['fromemail']
            subject='Recieved mail from, '+ fromemail+' about: '+form.cleaned_data['subject'] 
            message='<<Name: {0} >>'.format(name)+' '+form.cleaned_data['message']

            email = send_mail(subject, message, fromemail, ['salemododa2@gmail.com'], fail_silently=False)


    return render(request, 'portfolio/index.html', {'form':form})

def proj1(request):
    return render(request, 'portfolio/proj1.html')

def proj2(request):
    return render(request, 'portfolio/proj2.html')

def proj3(request):
    return render(request, 'portfolio/proj3.html')
