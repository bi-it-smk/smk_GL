from datetime import date
from gui import confirm_non_workday

def date_info():   
    cur_date = date.today()
    # cur_date = date(2026,11,2)
    weekday = cur_date.weekday()
    workday =  weekday < 5

    if not workday:
        if not confirm_non_workday():
            int_workday=0
            return None, int_workday 
    int_workday = 1
    return cur_date, int_workday



        


