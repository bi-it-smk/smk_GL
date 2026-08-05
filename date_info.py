from datetime import date
from gui import confirm_non_workday

def date_info():   

    cur_date = date.today()
    weekday = cur_date.weekday()
    workday =  weekday < 5

    if not workday:
        if not confirm_non_workday():
            return None
    return cur_date


    
        


