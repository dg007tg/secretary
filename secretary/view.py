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


def SignIn(request):
    return render(request, "login.htm", {})

def RegistrationDetails(request):
    return render(request, "registration.htm", {})

def Index(request):
    return render(request, "index.htm", {})

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
        return render(request, "report.htm", {"FLOWS":report})

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

def EditReport(request):
    report = {}
    if("month" in request.GET):
        #get details of report correspond to the date
        #then fill details in report
        month = request.GET['month']
        #report = ....
        flows = {}
        for flow_name in const.FLOW_NAMES:
            #flows[flow_name] = report[flow_name]
            flows[flow_name] = flow_name
        return render(request, "report.htm", {"FLOWS":flows})
    else:
        return render(request, "viewReport.htm", {"MODE":"EDIT"})




