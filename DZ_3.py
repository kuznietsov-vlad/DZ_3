import re

def normalize_phone(phone_number: list):
    pattern=r'[^0-9]'
    num_array=[]
    num_cleaned=re.sub(pattern, '', phone_number)
    if num_cleaned.startswith('0') and len(num_cleaned)==10:
        num_cleaned = '+38'+ num_cleaned
    if num_cleaned.startswith('38'):
        num_cleaned = '+38' + num_cleaned
    num_array.append(num_cleaned)

    return ', '.join(num_array)

raw_numbers = "067\\t123 4567"


print(normalize_phone(raw_numbers))
