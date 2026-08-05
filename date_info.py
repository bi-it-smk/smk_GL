from datetime import date

def date_info():   

    curDate = date.today()
    weekDay = curDate.weekday()
    
    if weekDay < 5:
        workDay = 1
    else:
        workDay = 0

    return workDay


