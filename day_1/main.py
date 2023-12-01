import re

def convert_string_to_digit(value: str) -> str:
    """Convert a digit into a string. Ignore if already a digit.
    Example: 'one' returns '1', '1' returns '1'
    """
    match_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    if value in match_dict:
        return match_dict[value]
    else:
        return value

def get_digits_in_string(value: str) -> list[str]:
    """Returns a list of digits in a string. Regex allows overlapping matches.
    Example: twone will return ['two', 'one']
    """
    pattern = r'(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))'
    result = re.findall(pattern, value)
    return result

def keep_first_and_last_digit(list_of_digits: list) -> str:
    """Returns the first and last digit of a list of digits as a string. Not summed.
    Example: ['one', 'two', '3'] returns '13'
    """
    return convert_string_to_digit(list_of_digits[0]) + convert_string_to_digit(list_of_digits[-1])

def get_calibration(value: str):
    """Returns the calibration of a string. Converts the digit string into an integer.
    Example: 'one' returns 1, '1' returns 1
    """
    return int(keep_first_and_last_digit(get_digits_in_string(value)))

if __name__ == '__main__':
    total = 0
    with open("day_1/input.txt") as input_file:
        for line in input_file:
            print("{0}\t{1}".format(get_calibration(line[:-1]), line[:-1]))
            total += get_calibration(line)
    print("Total: {0}".format(total))