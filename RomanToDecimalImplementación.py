import unittest

def roman_to_decimal(roman):
    total = 0
    for letter in roman:
        if letter == 'I':
            total += 1
        elif letter == 'V':
            total += 5
        elif letter == 'X':
            total += 10
        elif letter == 'L':
            total += 50
        elif letter == 'C':
            total += 100
        elif letter == 'D':
            total += 500
        elif letter == 'M':
            total += 1000
    if 'IV' in roman:
        total -= 2
    if 'IX' in roman:
        total -= 2
    if 'XL' in roman:
        total -= 20
    if 'XC' in roman:
        total -= 20
    if 'CD' in roman:
        total -= 200
    if 'CM' in roman:
        total -= 200
    return total
