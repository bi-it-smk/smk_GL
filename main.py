from gui import *
from date_info import *
from database import *
from datetime import *

connect_db()
create_table()

cur_date, workday = date_info()
print(cur_date, workday)
if cur_date is None:
    exit()

presence = main_window()
print(presence)

update_date(cur_date)
insert_values(cur_date, workday, presence)

# update excel

# end