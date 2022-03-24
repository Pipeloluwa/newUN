from django.contrib.sites import requests
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


from .models import *


def index(request):
    if request.method== "POST":
        fullname= str(request.POST.get("fullname"))
        phoneno = str (request.POST.get("phoneno"))
        instagram = str (request.POST.get("instagram"))
        emailaddress= str (request.POST.get("emailaddress"))
        business= str (request.POST.get("business"))
        description = str (request.POST.get("description"))

        try:
            Information.objects.create(fullname = fullname,
                                              phone_no= phoneno,
                                              instgram_handler= instagram,
                                              email_address= emailaddress,
                                              business_idea_craft_skill= business,
                                              description= description)
            return render(request, "index.html", {"t": True})
        except:
            return HttpResponse("Registration Failed OR It might be you have already Registered.")
    else:
        return render(request,"index.html")
