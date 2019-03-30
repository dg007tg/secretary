# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:54:46 2019

@author: win8
"""
import re
from secretary import const
from.db_use import salary_operate,fee_operate,get_report_by_month,delete_report_by_month
income_name = ["SUPPORT_FEE","NURSING_FEE","MORTUARY_FEE","INCOME_FEE"]+["FOOD_FEE","UTILITY_FEE","MAINTENANCE_FEE","BUILD_FEE","COMSUMABLES_FEE","FACILITY_FEE","OTHER_FEE","RENT_FEE","TRASH_FEE","RETURNED_NURSING_FEE"]
def add_report_content(report):
    def filter_date(date):
        ret = re.sub(r'\u200e',"",date)
        ret =re.sub(r'[\u4e00-\u9fa5]','-',ret)
        ret = re.sub('-$',"",ret)
        return ret 

    for key,values in report.items():
        if key =='SALARY_FEE':
            for item in values:    
                date = filter_date(item["date"])
                salary_operate(user='root',date=date,name=item["name"],title=item["title"],amount=item['amount'],operate="add")           #user=root需要改变
        elif report[key]==-1:pass
        elif key in income_name:
            for item in values:  
                date = filter_date(item["date"])
                fee_operate(user='root',types=const.FEE_TYPES[key],date=date,name=item["name"],amount=item['amount'],operate="add")

def show_report_content(month):
    report = get_report_by_month(month)
    return report   

def update_report_content(month, report):
    def filter_date(date):
        ret = re.sub(r'\u200e',"",date)
        ret =re.sub(r'[\u4e00-\u9fa5]','-',ret)
        ret = re.sub('-$',"",ret)
        return ret
    month = filter_date(month)
    if(delete_report_by_month(month)):
        add_report_content(report)
    return True
        
        