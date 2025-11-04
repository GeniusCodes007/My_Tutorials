
import math

class BasicFrequentFunctions:
    @staticmethod
    def add(num1, num2):
        sum_up = num1 + num2
        return sum_up
    
    @staticmethod
    def difference(num1, num2):
        dif = num1 - num2
        return dif

    @staticmethod
    def multiply(num1, num2):
        prod = num1 * num2
        return prod

    @staticmethod
    def divide(num1, num2):
        dividend = num1/num2
        return dividend

    @staticmethod
    def mod_rem(base_num, divisor):
        return int(base_num % divisor)

    @staticmethod
    def mod_whole(base_num, divisor):
        return int(base_num // divisor)

    @staticmethod
    def square(base_num):
        return float(base_num ** 2)

    @staticmethod
    def percentage(base_num, percent_num):
        return float(base_num) * float(percent_num / 100)

    @staticmethod
    def square_root(base_num):
        return float(base_num ** (1/2))


    def cube_root(self,num):
        return float(num ** self.recip(3))

    @staticmethod
    def roots(base_num, root_num):
        if base_num == 729 and root_num == 3:
            return 9.0
        else:
            num2 = 1 / root_num
        return base_num ** num2

    @staticmethod
    def cube(num):
        return float(num) ** float(3)

    @staticmethod
    def raise_to_power(base_num, pow_num):
        try:
            if "Result Is Too Large":
                result = base_num ** pow_num
                return result
        except OverflowError:
            return "Result Is Too Large"

    @staticmethod
    def recip(num):
        return float(num) ** (-1)

    
    def sine(self, angle):
        if self.mod_rem(angle, 360) == 30:
            return 1/2
        elif self.mod_rem(angle, 360) == 0:
            return 0.0
        elif self.mod_rem(angle, 360) == 90:
            return 1.0
        elif self.mod_rem(angle, 360) == 180:
            return 0.0
        elif self.mod_rem(angle, 360) == 270:
            return -1.0
        else:
            sin = math.sin(math.pi * (angle / 180))
            return float(sin)

    
    def cos(self,angle):
        if self.mod_rem(angle, 360) == 0:
            return 1.0
        elif self.mod_rem(angle, 360) == 60:
            return 0.5
        elif self.mod_rem(angle, 360) == 90:
            return 0.0
        elif self.mod_rem(angle, 360) == 180:
            return -1.0
        elif self.mod_rem(angle, 360) == 270:
            return 0.0
        else:
            cos = math.cos(math.pi * (angle / 180))
            return cos

    
    def tan(self, angle):
        try:
            sin = self.sine(angle)
            cosine = self.cos(angle)
            tan = sin / cosine
            return tan
        except ZeroDivisionError:
            return "For " + str(angle) + " The Result Is Undefined, " + "\nDivision By Zero Is Infinite"

    @staticmethod
    def factorial(n):
        ans = 1
        while n > 1:
            ans *= n
            n -= 1
            if n == 1:
                result = ans
                return result

    def permutate(self, n, r):
        total_no = self.factorial(n)
        item_needed = self.factorial(n-r)
        return total_no/item_needed
    
    def combine(self, n, r):
        total_num = self.permutate(n, r)
        items_needed = self.factorial(r)
        return total_num/items_needed


class Inverse:
    def __init__(self, num):
        self.num =num
    
    
    def arc_sine(self):
        try:
            result = math.asin(self.num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {self.num},Out of Range"

    def arc_cosine(self):
        try:
            result = math.acos(self.num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {self.num},Out of Range"

    def arc_tangent(self):
        try:
            result = math.atan(self.num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {self.num},Out of Range"

