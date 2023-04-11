import unittest

def decimal_to_roman(decimal):
    resultado = ''
    while decimal >= 1000:
        resultado += 'M'
        decimal -= 1000
    if decimal >= 900:
        resultado += 'CM'
        decimal -= 900
    elif decimal >= 500:
        resultado += 'D'
        decimal -= 500
    elif decimal >= 400:
        resultado += 'CD'
        decimal -= 400
    while decimal >= 100:
        resultado += 'C'
        decimal -= 100
    if decimal >= 90:
        resultado += 'XC'
        decimal -= 90
    elif decimal >= 50:
        resultado += 'L'
        decimal -= 50
    elif decimal >= 40:
        resultado += 'XL'
        decimal -= 40
    while decimal >= 10:
        resultado += 'X'
        decimal -= 10
    if decimal >= 9:
        resultado += 'IX'
        decimal -= 9
    elif decimal >= 5:
        resultado += 'V'
        decimal -= 5
    elif decimal >= 4:
        resultado += 'IV'
        decimal -= 4
    while decimal > 0:
        resultado += 'I'
        decimal -= 1
    return resultado

