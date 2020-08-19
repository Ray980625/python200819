def circle_area(x):
    a = x*x*3.14
    return a

def circle_circum(x):
    a = x*2*3.14
    return a




c = float(input("半徑:"))

z = circle_area(c)
b = circle_circum(c)
print("圓周長:",z)
print("圓面積:",b)