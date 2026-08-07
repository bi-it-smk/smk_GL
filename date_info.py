from datetime import datetime
from datetime import date
from gui import confirm_non_workday

def date_info():   
    #cur_date = date.today()
    cur_date = date(2026,8,15)
    weekday = cur_date.weekday()
    workday =  weekday < 5

    if not workday:
        if not confirm_non_workday():
            return None
    if workday:
        int_workday = 1
    else:
        int_workday = 0
    return cur_date, int_workday


    
        


