# Makes passed string regex safe by replacing regex key characters with an arbitrary character.
def make_regex_safe(input):
    chars_to_replace = ['*', '+', '$', '|', '^', '?']
    for char in chars_to_replace:
        input = input.replace(char, '\\'+char)

    return input

