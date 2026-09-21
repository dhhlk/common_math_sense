from math import *

class simple_math:
    @staticmethod
    def add(num1, num2):
        print(float(num1 + num2))
    @staticmethod
    def sub(num1, num2):
        print(float(num1 - num2))
    @staticmethod
    def mul(num1, num2):
        print(float(num1 * num2))
    @staticmethod
    def div(num1, num2):
        try:
            print(float(num1 / num2))
        except ZeroDivisionError:
            print('Not possible in today\'s maths!')
    @staticmethod
    def pow(num1, num2):
        print(pow(num1, num2))
    @staticmethod
    def percentage(percent, quantity):
        print(float(percent / 100 * quantity))
    @staticmethod
    def average(*numbers):
        print(float(sum(numbers) / len(numbers)))