#Write a Python program to convert a byte string to a list of integers.

#02_17_21

#Bytes literals are always prefixed with 'b' or 'B'; 
#they produce an instance of the bytes type instead of the str type. 
#They may only contain ASCII characters; 
#bytes with a numeric value of 128 or greater must be expressed with escapes.


test_str = b'Abcxtya'
print(type(test_str))
print(test_str)
print(list(test_str))

test_str2 = b'h\x65llo'
print(type(test_str2))
print(test_str2)
print(list(test_str2))

test1 = b'\x00\x00\x00\x00\x00'
print(type(test1))
print(test1)
print(list(test1))

#why only print the numbers when converted to a list?