from math import *
from constants import *
class Measurement:
    @staticmethod
    def perimeter_of_rectangle(length, breadth):
        print(float(2 * length + 2 * breadth))
    @staticmethod
    def area_of_rectangle(length, breadth):
        print(f"{length * breadth} sq. cm")
    @staticmethod
    def perimeter_of_triangle(A, B, C):
        print(float(A+B+C))
    @staticmethod
    def area_of_right_triangle(height, base):
        print(f"{height * base * 1 / 2} sq. cm")
    @staticmethod
    def perimeter_of_square(side):
        print(float(4 * side))
    @staticmethod
    def area_of_square(side):
        print(float(side * side))
    @staticmethod
    def circumference_of_circle(radius):
        print(float(2 * radius * pie))
    @staticmethod
    def area_of_circle(radius):
        print(float(pie * radius ** 2))
    @staticmethod
    def area_of_cube(side):
        print(float(6 * side ** 2))
    @staticmethod
    def area_of_cuboid(length, breadth, height):
        print(float(2 * (length * breadth + breadth * height + length * height)))
    @staticmethod
    def area_of_sphere(radius):
        print(float(4 * pie * radius ** 2))
    @staticmethod
    def volume_of_cube(side):
        print(float(side ** 3))
    @staticmethod
    def volume_of_cuboid(length, breadth, height):
        print(float(length * breadth * height))
    @staticmethod
    def volume_of_sphere(radius):
        print(float((4 / 3) * pie * radius ** 3))