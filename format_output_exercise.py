# -*- coding: utf-8 -*-
"""Format Output Exercise

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cqS9tYzmTG0nQYRrH-S2CwKUgqV8L3Qc
"""

var1= int(input("please enter the first integer:"))
var2= int(input("please enter the second integer:"))

sum= var1+ var2
difference= var1 - var2
product = var1* var2
division = var1 / var2
average= (var1+var2)/2   # var1+var2/2
remainder= var1%var2
exponent= var1**var2

print()

print(f"{'sum:':<20}",f"{sum:>20}")
print(f"{'difference:':<20}",f"{difference:>20}")
print(f"{'product:':<20}",f"{product:>20}")
print(f"{'integer division:':<20}",f"{division:>20}")
print(f"{'average:':<20}",f"{average:>20}")
print(f"{'remainder:':<20}",f"{remainder:>20}")
print(f"{'exponent:':<20}",f"{exponent:>20}")