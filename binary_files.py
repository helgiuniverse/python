print(0b101000100111)
print(25213)
print(0x13af)
with open('binary_file', 'bw') as binary_file:
    for number in range(21):
        binary_file.write(bytes([number]))

with open('second_binary_file', 'bw') as second_binary_file:
    second_binary_file.write(bytes(range(21)))

with open('second_binary_file', 'br') as second_binary_file:
    for number in second_binary_file:
        print(number)
