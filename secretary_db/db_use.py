# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:54:30 2019

@author: win8
"""
from.import config
from.models import User,Salary,Fee
def user_operate(user,operate,name,pwd,authority=1):
    try:
        permit=User.objects.get(account=user)
    except User.DoesNotExist:
        return config.USER_NOT_EXIST
    if permit.authority==config.ROOT:
        if operate=="add":
            user_add=User(account=name,password=pwd,authority=authority)
            user_add.save()
        
        elif operate=="delete":
            user_delete=User.objects.get(account=name)
            user_delete.delete()
        elif operate=="modify":
            source=User.objects.get(account=name)
            source.update(password=pwd)
        elif operate=="search":
            dest=User.objects.filter(account=name)
            return dest
        else:
            return config.NO_SUCH_OPERATION
    else:
        return config.PERMISSION_DENIED
def salary_operate(user,date,name,title,amount,operate):
    try:
        permit=User.objects.get(account=user)
    except User.DoesNotExist:
        return config.USER_NOT_EXIST
    if permit.authority==config.ROOT:
        if operate=="add":
            
            user_add=Salary(date = date, name=name,amount=amount,title=title)
            user_add.save()
        elif operate=="delete":
            try:
                user_delete=Salary.objects.get(name=name,date=date)
                user_delete.delete()
            except Exception:
                return config.RECORD_NOT_FIND                
        elif operate=="modify":
            source=Salary.objects.get(date=date,name=name)
            source.update(amount=amount,title=title)
        elif operate=="search":
            dest=Salary.objects.filter(name=name,date=date)
            return dest            
    else:
        return config.PERMISSION_DENIED
def fee_operate(user,types,date,name,amount=0,operate="search"):
    try:
        permit=User.objects.get(account=user)
    except User.DoesNotExist:
        return config.USER_NOT_EXIST
    if permit.authority==config.ROOT:
        if operate=="add":
            user_add=Fee(types=types,date=date,name=name,amount=amount)
            user_add.save()
        elif operate=="delete":
            try:
                user_delete=Fee.objects.get(types=types,name=name,date=date)
                user_delete.delete()
            except Exception:
                return config.RECORD_NOT_FIND                
        elif operate=="modify":
            source=Fee.objects.get(types=types,date=date,name=name)
            source.update(types=types,name=name,date=date,amount=amount)
        elif operate=="search":
            dest=Fee.objects.filter(types=types,date=date)                                          
            return dest            
    else:
        return config.PERMISSION_DENIED
    

def get_report_by_month(month):
    #month should be in form "year-month" or "year/month
    import datetime
    import re
    import calendar
    from secretary import const
    month = re.split(r"[-/]", month)
    from_ = datetime.datetime(int(month[0]), int(month[1]), 1, 0, 0, 0)
    to_ = datetime.datetime(int(month[0]), int(month[1]), calendar.monthrange(int(month[0]), int(month[1]))[1], 23, 59, 59)
    
    ret = {}
    for fee in const.FEE_TYPES:
        if(fee == "SALARY_FEE"):
            fees = Salary.objects.filter(date__gte = from_).filter(date__lte = to_)
            if(len(fees) == 0):
                ret[fee] = -1
                continue
            else:
                ret[fee] = []
            for item in fees:
                tmp = {\
                        "name": item.name,\
                        "date": item.date.strftime("%Y-%m-%d"),\
                        "amount": item.amount,\
                        "title": item.title}
                ret["SALARY_FEE"].append(tmp)
            continue
        fees = Fee.objects.filter(date__gte = from_).filter(date__lte = to_).filter(name = fee)
        if(len(fees) == 0):
            ret[fee] = -1
            continue
        else:
            ret[fee] = []
            
        for item in fees:
            tmp = {\
                "name": item.name,\
                "date": item.date.strftime("%Y-%m-%d"),\
                "amount": item.amount}
            ret[fee].append(tmp)
            
    return ret

def delete_report_by_month(month):
    import datetime
    import re
    import calendar
    from secretary import const
    month = re.split(r"[-/]", month)
    from_ = datetime.datetime(int(month[0]), int(month[1]), 1, 0, 0, 0)
    to_ = datetime.datetime(int(month[0]), int(month[1]), calendar.monthrange(int(month[0]), int(month[1]))[1], 23, 59, 59)
    for fee in const.FEE_TYPES:
        if(fee == "SALARY_FEE"):
            fees = Salary.objects.filter(date__gte = from_).filter(date__lte = to_)
            print(fees)
            if(len(fees) == 0):
                continue
            else:
                fees.delete()
            continue
        fees = Fee.objects.filter(date__gte = from_).filter(date__lte = to_).filter(name = fee)
        if(len(fees) == 0):
            continue
        else:
            fees.delete()
    return True
