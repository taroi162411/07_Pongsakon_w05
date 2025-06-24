# รับ parameter
'''def ชื่อ function (parameter):
    parameter1 + parameter2 = xxxx

'''

def get_name(name):
    '''show name for parameter.'''
    print(f"Hello !!! : {name}")

name = input("Enter your name : ")
get_name(name)

a = int(input())
b = int(input())
def add_num(a,b):
    '''Function ++'''
    result = a + b
    return result

sum = add_num(a,b)
print(sum)

width = int(input())
length = int(input())
def rect_cal(width,length):
    ''' หาพื้นที่สี่เหลี่ยมและเส้นกรอบ'''
    area = width * length
    frome = 2 * (width + length)
    return area,frome

area,frame = rect_cal(width,length)
print(f"พื้นที่สี่เหลี่ยม = {area} เส้นกรอบ = {frame}")