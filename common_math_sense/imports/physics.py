from math import *
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