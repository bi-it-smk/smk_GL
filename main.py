from gui import *
from date_info import *
from database import *
from datetime import *
from stats import *
from export import *

connect_db()
create_table()

cur_date, workday = date_info()
if cur_date is None:
    exit()

presence = main_window()

update_dates(cur_date)
insert_values(cur_date, workday, presence)

export_attendance()

# update excel

# end