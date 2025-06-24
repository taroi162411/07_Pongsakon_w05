'''def ชื่อฟังก์ชั่น (parameter):
    return value1,value2
'''
# ไม่รับ parameter
def greeting_eng():
    print("Hello World!!!")
    print("Hi")
    
def greeting_th():
    print("สวัสดีชาวโลกกกก")
    print("หวาดดีงับ")
    
def get_time():
    from datetime import datetime 
    now = datetime.now()
    print(now)   

greeting_th()
get_time()