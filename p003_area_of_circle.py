# 计算圆的面积

import math

print(math.pi)


def compute_area_of_circle(r):
    return round(math.pi * r * r, 2)


print("area of 2 is :", compute_area_of_circle(2))
print("area of 3.14 is :", compute_area_of_circle(3.14))
print("area of 5.14 is :", compute_area_of_circle(5.14))
