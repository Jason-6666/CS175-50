# -*- coding: utf-8 -*-
"""Remove empty string.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15FAC8QqPvEfRJXtumlvk5sGSBAp6UJVG
"""

def remove_empty_strings():
    non_empty_strings = []
    user_input = input("Enter a list of strings separated by commas: ")
    string_list = user_input.split(',')
    for s in string_list:

        if s.strip():
            non_empty_strings.append(s.strip())

    return non_empty_strings


output = remove_empty_strings()
print(output)