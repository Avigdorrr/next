def double_letter(my_str):
    return "".join(map(double_letter_helper, my_str))


def double_letter_helper(letter):
    return letter*2
