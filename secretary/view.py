#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     23/03/2019
# Copyright:   (c) Administrator 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from django.shortcuts import render


def SignIn(request):
    return render(request, "login.htm", {})

def RegistrationDetails(request):
    return render(request, "registration.htm", {})

def Index(request):
    return render(request, "index.htm", {})

def Home(request):
    return render(request, "home.htm", {})

def AddReport(request):
    return render(request, "addReport.htm", {})

def ViewReport(requewst):
    return render(requewst, "viewReport.htm", {})



