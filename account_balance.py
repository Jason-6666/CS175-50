# -*- coding: utf-8 -*-
"""account_balance

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17FiINvUS--j4v8UKyMipAK9FJJIX_bPy
"""

INTEREST_RATE = 0.005
initial_balance = 1000.00
balance_after_first_year = initial_balance * (1 + INTEREST_RATE)
balance_after_second_year = balance_after_first_year * (1 + INTEREST_RATE)
balance_after_third_year = balance_after_second_year * (1 + INTEREST_RATE)
print(f"Balance after the first year: ${balance_after_first_year:,.2f}")
print(f"Balance after the second year: ${balance_after_second_year:,.2f}")
print(f"Balance after the third year: ${balance_after_third_year:,.2f}")