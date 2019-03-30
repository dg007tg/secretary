#-------------------------------------------------------------------------------
# Name:        const.py
# Purpose:
#
# Author:      Administrator
#
# Created:     25/03/2019
# Copyright:   (c) Administrator 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#name of incoming and outgoing current flows.
FLOW_NAMES = [
    "FOOD_FEE",\
    "UTILITY_FEE",\
    "MAINTENANCE_FEE",\
    "BUILD_FEE",\
    "COMSUMABLES_FEE",\
    "FACILITY_FEE",\
    "OTHER_FEE",\
    "RENT_FEE",\
    "TRASH_FEE",\
    "RETURNED_NURSING_FEE",\
    "SALARY_FEE",\
    "SUPPORT_FEE",\
    "NURSING_FEE",\
    "MORTUARY_FEE",\
    "INCOME_FEE"]

FEE_TYPES={ "FOOD_FEE" : 0,\
         "UTILITY_FEE" : 1,\
         "MAINTENANCE_FEE" : 2,\
         "BUILD_FEE" : 3,\
         "COMSUMABLES_FEE" : 4,\
         "FACILITY_FEE" : 5,\
         "OTHER_FEE" : 6,\
         "RENT_FEE" : 7,\
         "TRASH_FEE" : 8,\
         "RETURNED_NURSING_FEE" : 9,\
         "SALARY_FEE" : 10,\
#income types
         "SUPPORT_FEE" : 11,\
         "NURSING_FEE" : 12,\
         "MORTUARY_FEE" : 13,\
         "INCOME_FEE" : 14}
#definition of some responses
class NET_RESPONSE:
    OPERATION_SUCCESS = "0"
    OPERATION_ERROR = "1"
    USER_NOT_EXIST = "2"
    PASSWORD_WRONG = "3"