"""
A convert an integer to a (lower case) roman numeral for use in figure 
legends
"""

def int2roman(num, lower=True):
    # Define a lookup list of tuples (integer value, Roman numeral symbol)
    # Ordered from largest to smallest to simplify the conversion logic
    lookup = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    res = ''  # Initialize an empty string to build the Roman numeral

    # Iterate through the lookup table
    for value, roman_symbol in lookup:
        # While the current number is greater than or equal to the current value
        while num >= value:
            res += roman_symbol  # Append the Roman symbol to the result
            num -= value         # Subtract the value from the number

    if lower:
        return res.lower()
    return res
