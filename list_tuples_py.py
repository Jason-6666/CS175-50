# -*- coding: utf-8 -*-
"""list tuples.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fjb54gCMiOIrvJ0oLtIKQagD4F2Mng85
"""

# Q1:
# scores = [2.5, 7.3, 6.5, 4.0, 5.2]
# total = 0

# for score in scores:
#     total += score

# average = total / len(scores)

# print("The average of the element is:", average)

# Q2:
filename = 'cities.txt'
cities = []

with open(filename, 'r') as file:

  for line in file:
    cities.append(line.strip())

print(cities)