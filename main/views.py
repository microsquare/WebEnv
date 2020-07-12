from django.shortcuts import render
from oursite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . import models


def home(requests):
    return render(requests, 'index.html')


def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        emailid = request.POST.get('email')
        subject = request.POST.get('subject')
        des = request.POST.get('desp')
        desp = "Subject: " + subject + "\n  Message: " + des

        models.Contactf.objects.create(full_name=name, emailid=emailid, desp=desp)

        subject = 'SUPPORT REQUEST'
        message = 'REQUEST GENRATED ON BEHALF OF :\n {} \n email id={} \n {}'.format(name,
                                                                                                            emailid,
                                                                                                            desp)
        recepient = 'support@webenv.in'

        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def about(requests):
    return render(requests, 'about.html')


def pp(requests):
    return render(requests, 'privacypolicy.html')


def tnc(requests):
    return render(requests, 'termsandconditions.html')


def pr(requests):
    return render(requests, 'pricing.html')


def fe(requests):
    return render(requests, 'features.html')
