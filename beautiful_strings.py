__author__ = 'robertb'

import sys

# for arg in sys.argv:
#     print arg

with open(sys.argv[1], 'r') as strings:
    content = strings.readlines()

for sentence in content:
    multiplier = 26
    sentence_sum = 0
    letter_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
                   'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
                   's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    sentence = sentence.lower()
    for char in sentence:
        if char.isalpha():
            letter_dict[char] += 1
            # print letter_dict[char]

    number_list = []

    for letter in letter_dict:

        if letter_dict[letter] >= 1:
            number_list.append(letter_dict[letter])

    sorted_list = sorted(number_list, key=int, reverse=True)

    for number in sorted_list:
        sentence_sum += number * multiplier
        multiplier -= 1

    print sentence_sum