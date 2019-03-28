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
from django.http import HttpResponse
from . import const
import json

#this is a decarator
def cookie_auth(func):
    def wrapper(request, *args, **kwargs):
        cookies = request.get("user_name")
        if(cookies):
            #means user pass authentication, return requested pages
            return func(request)
        else:
            return const.NET_RESPONSE.OPERATION_ERROR
    return wrapper

def SignIn(request):
    if(len(request.POST) > 0):
        #some authenticating here
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        try:
            #search user info in database
            #user = xxx.get(user_name = user_name)
            pass
        except Exception(e):
            #if not exist
            return HttpResponse(const.NET_RESPONSE.USER_NOT_EXIST)
        #if exist, verify password
        if(user.password == password):
            index = render(request, "index.htm", {})
            #if authenticated, set cookies and sessions
            #cookies must have expire time and should not be changed by javascript
            return index
        else:
            return HttpResponse(const.NET_RESPONSE.PASSWORD_WRONG)
    else:
        return render(request, "login.htm", {})

def RegistrationDetails(request):
    return render(request, "registration.htm", {})

def Index(request):
    return render(request, "index.htm", {})

@cookie_auth
def Home(request):
    if(len(request.GET)>0):
        page = request.GET['page'] if request.GET['page'] else 1
        rows = request.GET['rows'] if request.GET['rows'] else 10
        sortOrder = request.GET['sortOrder'] if request.GET['sortOrder'] else "desc"
        ret = {"total":2,"rows":[{
                    "date":"2019/2",
                    "amount":"123"
                },
                {
                    "date":"2019/1",
                    "amount":"293"
                }]}
        return HttpResponse(json.dumps(ret, ensure_ascii = False))
    else:
        return render(request, "home.htm", {})

@cookie_auth
def AddReport(request):
    report = {}
    if(len(request.POST) > 0):
        #get details of report correspond to the date
        try:
            report = json.loads(request.POST['report'])
        except Exception(e):
            return HttpResponse(const.NET_RESPONSE.OPERATION_ERROR)
        #save data into database and report is dictionary contains all data.
        return HttpResponse(const.NET_RESPONSE.OPERATION_SUCCESS)
    else:
        for flow_name in const.FLOW_NAMES:
            report[flow_name] = "0"
        return render(request, "report.htm", {"FLOWS":report, "MODE":"ADD"})

@cookie_auth
def ViewReport(request):
    report = {}
    if("month" in request.GET):
        #get details of report correspond to the date
        #then fill details in report
        month = request.GET['month']
        #report = ....
        income_name = ["SUPPORT_FEE","NURSING_FEE","MORTUARY_FEE","INCOME_FEE"]
        overhead_name = ["FOOD_FEE","UTILITY_FEE","MAINTENANCE_FEE","BUILD_FEE","COMSUMABLES_FEE","FACILITY_FEE","OTHER_FEE","RENT_FEE","TRASH_FEE","RETURNED_NURSING_FEE"]
        for flow_name in income_name:
            report[flow_name] = [{"date":"2019-2-11","name":"hello","amount":"233"}]
        for flow_name in overhead_name:
            report[flow_name] = [{"date":"2019-2-11","name":"hello","amount":"233"}]
        report["SALARY_FEE"] = [{"date":"2019-2-11","name":"hello","title":"boss","amount":"233"}]
        report["MODE"] = "READ"
        return render(request, "viewReport.htm", report)
    else:
        return render(request, "viewReport.htm", {"MODE":"READ"})

@cookie_auth
def EditReport(request):
    report = {}
    if(len(request.POST) > 0):
        try:
            report = json.loads(request.POST["report"])
        except Exception(e):
            return HttpResponse(const.NET_RESPONSE.OPERATION_ERROR)
        #update corresponding report
        return HttpResponse(const.NET_RESPONSE.OPERATION_SUCCESS)
    if("month" in request.GET):
        #get details of report correspond to the date
        #then fill details in report
        month = request.GET['month']
        #report = ....
        income_name = ["SUPPORT_FEE","NURSING_FEE","MORTUARY_FEE","INCOME_FEE"]
        overhead_name = ["FOOD_FEE","UTILITY_FEE","MAINTENANCE_FEE","BUILD_FEE","COMSUMABLES_FEE","FACILITY_FEE","OTHER_FEE","RENT_FEE","TRASH_FEE","RETURNED_NURSING_FEE"]
        for flow_name in income_name:
            report[flow_name] = [{"date":"2019-2-11","name":"hello","amount":"233"}]
        for flow_name in overhead_name:
            report[flow_name] = [{"date":"2019-2-11","name":"hello","amount":"233"}]
        report["SALARY_FEE"] = [{"date":"2019-2-11","name":"hello","title":"boss","amount":"233"}]

        flows = {}
        for flow_name in const.FLOW_NAMES:
            #flows[flow_name] = report[flow_name]
            sum = 0.0
            for record in report[flow_name]:
                sum = sum + float(record["amount"])
            flows[flow_name] = sum
        return render(request, "report.htm", {"FLOWS":flows, "MODE":"EDIT", "REPORT_DETAILS":json.dumps(report, ensure_ascii=False)})
    else:
        return render(request, "viewReport.htm", {"MODE":"EDIT"})




