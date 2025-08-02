# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# highAndLow("1 2 3 4 5"); // return "5 1"
# highAndLow("1 2 -3 4 5"); // return "5 -3"
# highAndLow("1 9 3 4 -5"); // return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    string_list = sorted(numbers.split())
    number_list = [int(num_str) for num_str in string_list]
    number_list.sort()
    return f"{number_list[-1]} {number_list[0]}"

print(high_and_low("1 2 3 4 5"))  # returns "5 1"
print(high_and_low("1 2 -3 4 5"))  # returns "5 -3"