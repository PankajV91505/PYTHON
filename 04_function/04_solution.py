import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2)
    circumference = round(2 * math.pi * radius)
    return area, circumference

a ,c = circle_stats(10)

print(f"Area: {a}, Circumference: {c}")