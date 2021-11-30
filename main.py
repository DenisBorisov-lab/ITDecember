import math
import random

string = input()
alphabet = list("abcdefghijklmnopqrstuvwxyz")
dictionary = {}
for i in range(len(alphabet)):
    code = str(bin(i))[2:]
    dictionary[alphabet[i]] = ((5 - len(code)) * "0") + code
word = list(string)
binary_view = ""
for letter in word:
    part = list(dictionary[letter])
    new_part = []
    for i in range(1, len(part)):
        if len(str(math.log(i, 2))) == 3:
            new_part.append("0")
        new_part.append(part[i])
    binary_view += "".join(new_part)
print(binary_view)
random_target = random.randint(0, len(binary_view) - 1)
incorrect_list = list(binary_view)
if incorrect_list[random_target] == "0":
    incorrect_list[random_target] = "1"
else:
    incorrect_list[random_target] = "0"
incorrect_word = "".join(incorrect_list)
print(incorrect_word)