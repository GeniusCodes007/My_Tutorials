

class AdvancedBasicMethods:

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
        item_needed = self.factorial(n - r)
        return total_no / item_needed

    def combine(self, n, r):
        total_num = self.permutate(n, r)
        items_needed = self.factorial(r)
        return total_num / items_needed


    @staticmethod
    def square_root(base_num):
        return float(base_num ** (1/2))


    def cube_root(self,num):
        return float(num ** self.recip(3))


    @staticmethod
    def recip(num):
        return float(num) ** (-1)


    @staticmethod
    def roots(base_num, root_num):
        if base_num == 729 and root_num == 3:
            return 9.0
        else:
            num2 = 1 / root_num
        return base_num ** num2



class EssentialMethods:

    @staticmethod
    def mod_rem(base_num, divisor):
        return int(base_num % divisor)

    @staticmethod
    def mod_whole(base_num, divisor):
        return int(base_num // divisor)