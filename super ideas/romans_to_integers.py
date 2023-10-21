# Define the Roman numeral symbols and their values
roman_numerals = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
]

integer_value = int(input("Введите цифру: "))

roman_numeral = ""

# Iterate through the Roman numeral symbols and values
for symbol, value in roman_numerals:
    while integer_value >= value:
        roman_numeral += symbol
        integer_value -= value

# Print the Roman numeral representation
print(roman_numeral)  # Output: "XXVII"

