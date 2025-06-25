from datetime import datetime,date,timedelta    
import time

today = date.today()

print(f"วันที่ {today}")
print(f"วัน {today.day}")
print(f"เดือน {today.month}")
print(f"ปี {today.year}")

now = datetime.now()
print(f"เวลาปัจจุบัน Hr :{now.hour}")
print(f"เวลาปัจจุบัน m :{now.minute}")
print(f"เวลาปัจจุบัน s :{now.second}")

# จัด Format วัน-เดือน-ปี
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H:%M:%S")


print(formatted_date)
print(formatted_time)

# คำนวณวันที่
tomorow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)
next_week = today + timedelta(days = 7)
next_mount = today + timedelta(days = 30)

print(tomorow)
print(yesterday)
print(next_week)
print(next_mount)