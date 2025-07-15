# more on data types
# reference documentation:  https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/reference/expressions.html#operator-summary

### booleans
# determine if the following statement is true or false
# you can test these in the interpreter or using print statements
# True and True
# False and True
# True or False
# False and True or False
# False and (True or False)

# ### converting data types
# # what is the difference between implicit and explicit type conversion?
# # determine if the following statements result in errors or not
# # 5 + '5'
# # 5 + int('5')
# # int(5.2) + int('5')
# # 5.2 + float('5')
# # 5 and '5' # bonus question, does this evaluate to true or false?
# # [1, 2] or [3, 4] # bonus question, does this evaluate true or false?
# # True + 5
# # False + 5

# my_guess = input('Enter a guess')
# print('10 times your guess is ' + 10 * my_guess)

# can you see how implicit conversions can get you in trouble...?

### binary and hexadecimal
# Convert 10 to binary
def convert_dec_to_binary(num:int)->int:
    binary = bin(num)
    return binary

# Convert 0b10101 to decimal
# Convert 0x10101 to decimal

def convert_hex_to_dec(hex:str)->float:
    hexadecimal = int(hex,16)
    return hexadecimal

print(convert_hex_to_dec('0b10101'))
print(convert_hex_to_dec('0x10101'))

# Perform a bitwise 'or' between 0b110101 and 0b101010, what is its decimal value

def bitwise(num1,num2):
    result = num1 | num2
    print(result)

print(bitwise(0b110101,0b101010))

# Perform a bitwise 'or' between 53 and 42, what is its binary value
# Do the same with a bitwise 'and'

### string manipulation
# Convert 'hello' to bytes and then convert the bytes to an integer
# hint: use the encode method

# What's the difference between strip and replace?  When might you use both?

# Use index, len, slicing, and concatenation to 
# replace the word 'horrible' with 'beautiful'
# "It's a horrible day."
# "It's a beautiful day."

# scan through the 'is____' string methods in the documentation.
# how might you use those methods to clean a dataset?