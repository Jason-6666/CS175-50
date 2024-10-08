# -*- coding: utf-8 -*-
"""Extract First Name .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ckZJvn1fCoqTCx_iONBsw7_FL8k7Vnjr
"""

def extract_first_name(full_name):
    return full_name.split()[0]

def main():
    full_name = input("Please enter your full name: ")
    first_name = extract_first_name(full_name)
    print(f"Your first name is: {first_name}")

if __name__ == "__main__":
    main()