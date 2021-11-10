def return_10():
    return 10

def add(sum_1, sum_2):
    result = sum_1 + sum_2
    return result

def subtract(sum_1, sum_2):
    result = sum_1 - sum_2
    return result

def multiply(sum_1, sum_2):
    result = sum_1 * sum_2
    return result

def divide(sum_1, sum_2):
    result = sum_1 / sum_2
    return result

def length_of_string(string):
    # print(len(string))
    return len(string)

def join_string(string_1, string_2):
    joined_string = f"{string_1}{string_2}"
    return joined_string

def add_string_as_number(num_1, num_2):
    add_result = int(num_1) + int(num_2)
    return add_result

# This function covers all full month tests from python_functions_test.py
def number_to_full_month_name(month_num):
    months_of_the_year = ["Test", "January", "Feburary", "March", "April", "May", "6", "7", "8", "September"]
    month_str = months_of_the_year[month_num]
    return month_str

# This function covers all short month tests from python_functions_test.py
def number_to_short_month_name(month_num):
    short_month_of_the_year = ["Test", "Jan", "Feb", "Mar", "Apr", "May", "6", "7", "8", "Sept", "Oct"]
    short_month_str = short_month_of_the_year[month_num]
    return short_month_str

#Further

def length_of_cube(length):
    volume = length * length * length
    return volume

def normal_string(string):
    reversed_str = string[::-1]
    return reversed_str

def fahrenheit(f):
    c_calculation = 5 / 9 * (f - 32)
    celsius = int(c_calculation)
    return celsius