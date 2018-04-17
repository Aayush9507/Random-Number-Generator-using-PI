import datetime
from math import ceil
from math import pi
import math


class Random:
    """Generating 4 Digit Random Number using Pi
    In this program 4 values at indices of pi are calculated and concatenated  to generate a random number using
    current date and time"""
    today = datetime.datetime.now()
    time = datetime.datetime.now().time()
    str_today = today
    ymd = str_today.strftime("%Y-%m-%d")
    hms = str_today.strftime("%H-%M-%S")
    date_split = ymd.split("-")
    time_split = hms.split("-")

    def __init__(self):
        print "Initizaling"

    def generate_n1(self):
        """Generation of 1st number using current date """
        obj = Random
        self.n_1 = int(int(obj.date_split[0])-2000)+int(obj.date_split[1])+int(obj.date_split[2])
        self.n_1decimal = int(abs(pi)*math.pow(10, self.n_1)) % 10


    def generate_n2(self):
        """Generation of 2nd number using current time """
        obj = Random
        self.n_2 = int(obj.time_split[0])+int(obj.time_split[1])+int(obj.time_split[2])
        self.n_2decimal = int(abs(pi)*math.pow(10, self.n_2)) % 10

    def generate_n3(self):
        """Generation of 3rd number using current microsecond"""
        tot = 0
        str2 = self.time
        ss = float(str2.microsecond)
        n = ceil(ss * 100) / 1000.0
        while n > 0:
            dig = n % 10
            tot = tot+dig
            n = n//10
        self.n_3 = tot
        self.n_3decimal = int(abs(pi)*math.pow(10, self.n_3)) % 10

    def generate_n4(self):
        """Generation of 4th number by adding previous numbers and modulus by 7"""
        self.generate_n1()
        self.n_4 = (self.n_1+self.n_2+self.n_3) % 7
        self.n_4decimal = int(abs(pi)*math.pow(10, self.n_4)) % 10

    def random_num(self):
        """Generating a random number which is concatenation of four numbers """
        self.generate_n1()
        self.generate_n2()
        self.generate_n3()
        self.generate_n4()
        random_number = str(self.n_1decimal)+str(self.n_2decimal)+str(self.n_3decimal)+str(self.n_4decimal)
        print int(random_number)





