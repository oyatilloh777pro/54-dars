# 1-vazifa
import math

son = 3
natija = math.pow(son, 3)
print(int(natija))

# 2-vazifa
import random

list_sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(list_sonlar)
print(list_sonlar)

# 3-vazifa
import datetime

vaqt = datetime.datetime.now()

for i in range(1, 10001):
    pass

oxirgi = datetime.datetime.now()
vaqting = (oxirgi - vaqt).total_seconds()
print(f"Natija: {vaqting} s")

# 4-vazifa

import calendar

oy = int(input("1-12 oralig'ida oy raqamini kiriting: "))

yil = datetime.datetime.now().year
oy_kalendar = calendar.month(yil, oy)
print(oy_kalendar)

# Misol
#      April 2024
# Mon Tue Wed Thu Fri Sat Sun
#  1   2   3   4   5   6   7
#  8   9  10  11  12  13  14
# 15  16  17  18  19  20  21
# 22  23  24  25  26  27  28
# 29  30
