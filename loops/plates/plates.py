def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # start with at least 2 letters
    if check_length(s):
        if first_two_characters(s)  & last_is_number(s) & extract_str(s).isalpha():
            return True
    else:
        return False

def first_two_characters(s):
    return s[0:1].isalpha()

def check_length(s):
    return 2 <= len(s) <= 6

def last_is_number(s):
    for i in range(len(s)):
        c =  s[i]
        if c == '0':
            return False
        if c.isnumeric():
            return s[i:len(s)].isnumeric()

def extract_str(s):
        for i in range(len(s)):
            c =  s[i]
            if c.isnumeric():
                return s[:i]

main()