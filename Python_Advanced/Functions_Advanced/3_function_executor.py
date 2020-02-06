def sum_numbers(*nums):
    return sum(nums)


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result_list = []
    for function in args:
        result_list.append(function[0](*function[1]))
    return result_list


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
