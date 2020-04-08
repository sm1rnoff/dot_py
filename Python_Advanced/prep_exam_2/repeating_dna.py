def my_count(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in range(0, string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count += 1
    return count


def validate(temp_list, idx1):
    try:
        if temp_list[idx1]:
            return True
    except IndexError:
        return False


def get_repeating_DNA(test):
    repeated_strings = []
    for i in range(len(test)):
        if validate(list(test), i+10):
            if my_count(test, test[i:i+10]) > 1:
                repeated_strings.append(test[i:i+10])

    return list(dict.fromkeys(repeated_strings))


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
#test = "AAAAAAAAAAA"
#test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
