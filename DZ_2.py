import random

def get_numbers_ticket(min, max, quantity):
    try:
        get_ticket= sorted(random.sample(range(min, max), quantity))
        return get_ticket
    except ValueError:
        return []

print(get_numbers_ticket(1000, 1002, 3))

