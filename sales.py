# -*- coding: utf-8 -*-
"""sales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DCBtdboxdNpga99M4YZEESTThXqfsZqu
"""

commission = 0
a = input("do you want to calculate commission?")
while a == "yes":
  sales = float(input("enter a salesperson's sales"))
  rates = float(input("enter a commission rate "))
  commission = sales*rates

  print("the commission is :", commission)
  a = input("do you want to  calculate  another commission?")

print("over")