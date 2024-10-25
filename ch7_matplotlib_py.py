# -*- coding: utf-8 -*-
"""ch7-matplotlib.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19-OWzMzmUHIp3asjJ8mPxBW2Pm_Nk-P0
"""

import matplotlib.pyplot as plt
heights = [100, 200, 300, 400, 500]
bar_width = 0.5
years = ['2016', '2017', '2018', '2019', '2020']

colors = ['red', 'green', 'blue', 'brown', 'black']
plt.bar(years, heights, color=colors, width=bar_width)

plt.title('Sales by year')

plt.xlabel('Years')
plt.ylabel('Sales')

plt.xticks(years)
plt.yticks(range(0, 601, 100), [f'${i}' for i in range(0, 601, 100)])  # parameter of the tick function. *
plt.show()