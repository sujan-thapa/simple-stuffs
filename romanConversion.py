# Seven different symbols represent Roman numerals with the following values:

# Given an integer, convert it to a Roman numeral.


def int_roman(num):
    romanNumeral = []
    symbols = {
        "I": 1,
        "v": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        
    }

    # for ones
    ones = num%10

    # for tens
    tens = (num // 10) % 10

    # for hundres 
    hundred = (num // 100) % 10

    # for thousand 
    thousand = (num// 1000) % 10

    for i in symbols:
        
        if ones == symbols[i]:





num = 3749
int_roman(num)