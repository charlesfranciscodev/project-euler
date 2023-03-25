# Counting Sundays
# Answer: 171

import datetime
from dateutil.relativedelta import *

current_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)
total = 0
while current_date < end_date:
    if current_date.weekday() == 6:
        total += 1
    current_date += relativedelta(months=+1)
print(total)
