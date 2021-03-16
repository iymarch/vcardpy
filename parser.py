import re


def parse_telephone_object(line: str):
    line = line.replace(' ', '')
    telephone_type = re.findall(r'=(.*);', line)
    telephone_number = re.split(':', line)

    if telephone_type and telephone_number:
        telephone_type = telephone_type[0]  
        telephone_number = telephone_number[1]

    return telephone_type, telephone_number


