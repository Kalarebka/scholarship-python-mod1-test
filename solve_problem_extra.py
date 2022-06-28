"""In programming, not all floating-point numbers can be expressed in binary, 
find out why this is the case and propose a proper solution to this problem"""

# Why this equation displays wrong answer? Fix it
print(1.1 + 2.2)  # -> 3.3000000000000003

# When it comes to the floating point numbers, the decimal values don't correspond perfectly to binary numbers ().
# Numbers are stored in memory as binary with a limited number of digits after the decimal point,
# So if a binary representation of a decimal number is very long or even infinite, some precision is lost.

# I we just care about the display - print it formatted to the chosen number of decimal places:
value = 1.1 + 2.2
print(value)
print(f"{value:.1f}")
print(f"{value:.2f}")

# If we do care about the values, like when money is involved, it's better to operate on integers
# for all the calculations and number storage, and just convert to float in the end for display
value = 11 + 22
print(value / 10)
# Money representation would be calculated in 1/100s and then be formatted to 2 decimal places
cents = 110 + 220
dollars = cents / 100
print(f"${dollars:.2f}")
