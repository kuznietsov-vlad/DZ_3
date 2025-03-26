import random

def get_numbers_ticket(min, max, quantity):
    try:
        if max < 1000:
            if quantity < max - min:
                return []
            get_ticket= sorted(random.sample(range(min, max), quantity))
            return get_ticket
        else:
            return []
    except ValueError or NameError:
        return []

print(get_numbers_ticket(1000, 999, 1))
