import re

def normalize_phone(phone_number: list):
    pattern=r'[^0-9]'
    num_array=[]
    num_cleaned=re.sub(pattern, '', phone_number)
    if num_cleaned.startswith('0') and len(num_cleaned)==10:
        num_cleaned = '+38'+ num_cleaned
    if num_cleaned.startswith('38'):
        num_cleaned = '+' + num_cleaned
    num_array.append(num_cleaned)

    return ', '.join(num_array)

raw_numbers = "067\\t123 4567"
# "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   "

print(normalize_phone("    +38(050)123-32-34"))
