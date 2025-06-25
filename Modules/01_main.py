import math

x = math.pi

def cal_circle_area(radius):
    '''คำนวณ พท. วงกลม'''
    return pi * radius ** 2

def cal_rect_area(width,lengh):
    '''คำนวณ พท. สี่เหลี่ยม'''
    return width * lengh

radius = 10
result = cal_circle_area(radius)
print(result)