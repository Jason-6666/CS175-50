# -*- coding: utf-8 -*-
"""stocks.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URgQoB3Exkhq6g4w-sJDDaZiNov6pXnb
"""

q_1 = float (input ("enter commission rate percentage on stock purchase"))
q_2 = float (input ("enter commission rate percentage on stock sale"))
a_1 = int(input ("enter number of shares purchased"))
a_2 = int(input ("enter number of shares sold"))
p_1 = int(input ("enter purchased price per share"))
p_2 = float (input ("enter sell price per share"))

A_1 = a_1*p_1
A_2 = A_1*q_1
A_3 = a_2*p_2
A_4 = A_3*q_2
e = A_3 - A_1 - A_2 - A_4

print ("amount paid for the stock:", A_1)
print ("commission paid on the purchase:", A_2)
print ("amount the stock sold for:", A_3)
print ("commission paid on the sale:", A_4)
print ("profit(or loss if negative):", e )