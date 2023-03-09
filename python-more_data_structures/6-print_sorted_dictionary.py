#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for key_1 in sorted_dictionary:
        print(F'{key_1}: {a_dictionary[key_1]}')
        
