# -*- coding: utf-8 -*-
"""Final Exam Review.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S5tLjnwXs0grYA6os4kX9fB-C0ADI1nD
"""

# Q1:
date_string = '11/26/2020'
year = date_string.split('/')[2]   # return a list
print(year)

# Q2:
a = [1, 2, 0, 3]
b = [3, 4, 6, 5]
total = 0

for x, y in zip(a, b):    # package element
    if x == 0 or y == 0:
        continue  # skip this loop, enter the next loop
    total += x * y   # total += x * b[a.index(x)] #----this one is wrong.

print(total)

# Q3: use dictionary (add item to the dictionary)
sentence = "apple banana apple orange banana apple shit shit"
dict1 = {}
words = sentence.split()  # return a list

for word in words:         # review this mythod above
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1

for word, count in dict1.items():
    print(f"{word}: {count}")

# Q4:
text = "Hello, World!"
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
      result = text.replace(char,"@")    # result = "".join('@' if char in vowels else char for char in text)

print(result)

# Q5:
sentence = "it's raining cats and dogs."
# capitalized_sentence = sentence.title()   # this function used to capitalized each word in the s.
capitalized_sentence = ' '.join(word.capitalize() for word in sentence.split())
print(capitalized_sentence)

# Q6:
sentence = "Chicago is very different from Boston"
words = sentence.split()
longest_word = max(words, key = len)  # the defalut sequence is alphabetial order

print(longest_word)

# Q7:
text = "Python 3.9 is great for 2024!"

result = "".join(char for char in text if not char.isdigit())    # review this line of code

print(result)

# Q8:
text = "Hello World! Python3"

uppercase_count = 0
lowercase_count = 0
digit_count = 0

for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1

print("Uppercase letters: ",uppercase_count)
print("Lowercase letters: ",lowercase_count)
print("Digits: ",digit_count)

# Q9:
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):  # return a list
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Q10:
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8  }
sold_items = ["apple", "banana", "grape", "apple", "orange", "banana"]

for item in sold_items:
    if item in inventory:
        if inventory[item] > 0:
            inventory[item] -= 1
        else:
            print(item,"sold out.")
    else:
        print(f"{item} is not in inventory!")

print("Updated Inventory:")
for item, quantity in inventory.items():
    print(item, quantity)

# Q11:
try:
  file_name = input ("Enter the name of the file to read: ")
  with open (file_name,'r') as file:
    lines = file.readlines()
  line_count = len(lines)
  print(f"The file '{file_name}' has {line_count} lines.")

except FileNotFoundError:
  print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
  print(f"Error: Permission denied to read the file '{file_name}'.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")


# it will print the number of the line: 1

# Q12:
total = 0
try :
  file_name = input ("Enter the name of the file to read: ")
  with open(file_name,'r') as file:
    for line in file:
      number = float(line.strip())
      total += number
  print(f"The total sum of numbers in the file is:{total}")

except FileNotFoundError:
  print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
  print(f"Error: Permission denied to read the file '{file_name}'.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")

#  The program will raise an error and terminate. it won't print the sum.

# Q13
try:
  file_name = input ("Enter the name of the file containing numbers: ")
  total = 0
  with open(file_name,'r') as file:
    for line in file:
      try:
        number = float(line.strip())
        total += number
      except ValueError:
        print(f"Invalid data found :'{line.strip()}'. skipping this line. ")
    print(f"The total sum of numbers in the file is: {total}")
except FileNotFoundError:
  print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
  print(f"Error: Permission denied to read the file '{file_name}'.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")

# it will print 60, abc line will be skipped.