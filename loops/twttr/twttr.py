def main():
    user_input = input('Input: ')
    output = ''
    for i in range(len(user_input)):
        c = user_input[i]
        if check_vowel(c):
            continue
        else:
            output += c
    print(f'Output: {output}')

def check_vowel(c):
    vowels = ['a','e','u','i','o']
    for vowel in vowels:
        if c.lower() == vowel:
            return True

main()