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
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import const
import json
from secretary_db.models import User
from secretary_db.db_use import user_operate
from secretary_db.show_cope import add_report_content,show_report_content,update_report_content
#this is a decarator
'''
def cookie_auth(func):
    def wrapper(request, *args, **kwargs):
        cookies = request.get("user_name")
        if(cookies):
            #means user pass authentication, return requested pages
            return func(request)
        else:
            return const.NET_RESPONSE.OPERATION_ERROR
    return wrapper
'''
def SignIn(request):
    if(len(request.POST) > 0):
        #some authenticating here
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        try:
            #search user info in database
            #user = xxx.get(user_name = user_name)
            user=User.objects.get(account=user_name)
            pass
        except:
            #if not exist
            return HttpResponse(const.NET_RESPONSE.USER_NOT_EXIST)
        #if exist, verify password
        if(user.password == password):
#            index = redirect("/user-api/report/index")
            
            print(request.POST)
            #if authenticated, set cookies and sessions
            #cookies must have expire time and should not be changed by javascript
            return HttpResponse(0)
        else:
            return HttpResponse(const.NET_RESPONSE.PASSWORD_WRONG)
    else:
        return render(request, "login.htm", {})

def Register(request):
    if(len(request.POST) > 0):
        user_name="root"
        name=request.POST.get("user_name")
        pwd=request.POST.get("password")
        operate="add"
        authority=1
        user_operate(user_name,operate,name,pwd,authority)
        #save user info into database
        #now all registered users have less power
        return HttpResponse(const.NET_RESPONSE.OPERATION_SUCCESS)
    else:
        return render(request, "registration.htm", {})

def Index(request):
    return render(request, "index.htm", {})

#@cookie_auth
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

#@cookie_auth
def AddReport(request):
    report = {}
    if(len(request.POST) > 0):
        #get details of report correspond to the date
        try:
            report = json.loads(request.POST['report'])
        except Exception(e):
            return HttpResponse(const.NET_RESPONSE.OPERATION_ERROR)
        #save data into database and report is dictionary contains all data.
        add_report_content(report)
        return HttpResponse(const.NET_RESPONSE.OPERATION_SUCCESS)
    else:
        for flow_name in const.FLOW_NAMES:
            report[flow_name] = "0"
        return render(request, "report.htm", {"FLOWS":report, "MODE":"ADD"})

#@cookie_auth
def ViewReport(request):
    report = {}
    if("month" in request.GET):
        #get details of report correspond to the date
        #then fill details in report
        month = request.GET['month']
        #report = ....
        income_name = ["SUPPORT_FEE","NURSING_FEE","MORTUARY_FEE","INCOME_FEE"]
        overhead_name = ["FOOD_FEE","UTILITY_FEE","MAINTENANCE_FEE","BUILD_FEE","COMSUMABLES_FEE","FACILITY_FEE","OTHER_FEE","RENT_FEE","TRASH_FEE","RETURNED_NURSING_FEE"]
        report=show_report_content(month)   
        report["MODE"] = "READ"
        return render(request, "viewReport.htm", report)
    else:
        return render(request, "viewReport.htm", {"MODE":"READ"})

#@cookie_auth
def EditReport(request):
    report = {}
    if(len(request.POST) > 0):
        try:
            report = json.loads(request.POST["report"])
            month = request.POST["month"]
        except:
            return HttpResponse(const.NET_RESPONSE.OPERATION_ERROR)
        #update corresponding report
        update_report_content(month = month, report = report)
        return HttpResponse(const.NET_RESPONSE.OPERATION_SUCCESS)
    if("month" in request.GET):
        #get details of report correspond to the date
        #then fill details in report
        month = request.GET['month']
        #report = ....
        income_name = ["SUPPORT_FEE","NURSING_FEE","MORTUARY_FEE","INCOME_FEE"]
        overhead_name = ["FOOD_FEE","UTILITY_FEE","MAINTENANCE_FEE","BUILD_FEE","COMSUMABLES_FEE","FACILITY_FEE","OTHER_FEE","RENT_FEE","TRASH_FEE","RETURNED_NURSING_FEE"]
        
        report=show_report_content(month)                   
        
        flows = {}
        for flow_name in const.FLOW_NAMES:
            #flows[flow_name] = report[flow_name]
            sum = 0.0
            if(report[flow_name] != -1):
                for record in report[flow_name]:
                    sum = sum + float(record["amount"])
            flows[flow_name] = sum
        return render(request, "report.htm", {"FLOWS":flows, "MODE":"EDIT", "REPORT_DETAILS":json.dumps(report, ensure_ascii=False)})
    else:
        return render(request, "viewReport.htm", {"MODE":"EDIT"})




