from datetime import datetime,date,timedelta    
import time

today = date.today()
birth_day = date(1996,11,16)

def cal_age(birth_date):
    
    age = today.year - birth_date.year
    return age

age = cal_age(birth_day)
print(f"อายุของฉัน : {age} ปี")

