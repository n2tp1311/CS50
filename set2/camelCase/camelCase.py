
def main():
    camel_case = input('camel_case: ')
    # camel_case = 'thisIsMyFirstName'
    snake_case = turn_snake_case(camel_case)
    print(snake_case)
def turn_snake_case(camel_case):
    c_pos = find_camel(camel_case)
    under_camel_case = insert_under_score(camel_case, c_pos)
    return(under_camel_case.lower())
def insert_under_score(camel_case, c_pos):
    for position in reversed(c_pos):
        camel_case = camel_case[:position] + '_' + camel_case[position:]
    return camel_case
def find_camel(camel_case):
    c_pos = []
    for i in range(len(camel_case)):
        if camel_case[i].isupper():
            c_pos.append(i)
    return c_pos
main()