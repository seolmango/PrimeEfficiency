import math

class prime_check():

    def __init__(self):
        self.data = {}

    def is_prime(self, num:int):
        if(num % 2 == 0):
            return False
        if(num % 3 == 0):
            return False
        n = 1
        while( 6*n+1 <= math.sqrt(num)):
            a = 6*n-1
            b = a + 2
            if(num % a == 0):
                return False
            if(num % b == 0):
                return False
            n += 1
        return True
        

    def check_nums(self, nums:int):
        count = 0
        for i in range(1,nums+1):
            if(self.is_prime(i)):
                count += 1
        return (nums-count)/nums

    def make_data(self, until:int):
        for i in range(1, until+1):
            self.data[i] = self.check_nums(i)
        return self.data

