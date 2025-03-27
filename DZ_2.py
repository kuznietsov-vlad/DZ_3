import random

def get_numbers_ticket(min, max, quantity):
    try:
        if max < 1000 and min>=1:
            get_ticket= sorted(random.sample(range(min, max), quantity))
            return get_ticket
        else:
            return []
    except ValueError or NameError:
        return []

print(get_numbers_ticket(10, 20, 5))
