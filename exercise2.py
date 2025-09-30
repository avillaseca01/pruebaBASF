from datetime import datetime

#exercise2

def convert_to_utc(timestamp):    
    dt = datetime.strptime(timestamp, "%m/%d/%Y %I:%M%p")
    
    y = dt.year
    m = dt.month
    dd = dt.day
    hh = dt.hour 
    mm = dt.minute
    ss = dt.second
    
    return f"{y}-{str(m).zfill(2)}-{str(dd).zfill(2)}T{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}Z"


print(convert_to_utc("05/05/2024 8:30AM"))


