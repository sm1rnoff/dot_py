input_string = input()
unique_chars = {}
for char in input_string:
    if char in unique_chars:
        unique_chars[char] = input_string.count(char)
    else:
        unique_chars[char] = 1

[print(f'{key}: {value} time/s')
 for key, value in sorted(unique_chars.items())]
