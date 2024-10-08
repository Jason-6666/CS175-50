# -*- coding: utf-8 -*-
"""Nested Loop.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bW-i25sWcOabJPxvVaj4JVP7BDuElrpW
"""

def main():
    outer_loop = int(input("Enter range of outside loop: "))
    inside = 4
    total = 0

    for i in range(outer_loop):
        print(f"Outer loop value: {i + 1}")

        for j in range(inside):
          value = float(input(f"  Enter value {j + 1} for iteration {i + 1}: "))

          total += value

    print(f"Total: {total:.2f}")

if __name__ == "__main__":
    main()
2