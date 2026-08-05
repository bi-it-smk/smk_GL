from gui import *
from date_info import *
from database import *
from datetime import *

connect_db()
create_table()

cur_date = date_info()
print(cur_date)
if cur_date is None:
    exit()

presence = main_window()
print(presence)


insert_values(cur_date, presence)

# validate

# save

# update statistics

# update excel

# end