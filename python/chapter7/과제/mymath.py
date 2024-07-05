import math

def triangle_area(base:float, height:float) -> float:
    area = base*height/2
    return area
def circle_area(radius:float) -> float:
    area = math.pi*radius*radius
    return area

def rectangle_area(width:float, height:float) -> float:
    area = width*height
    return area
