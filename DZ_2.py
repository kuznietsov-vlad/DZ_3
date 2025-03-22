import random

def get_numbers_ticket(min, max, quantity):
    ticket_array=set()
    get_ticket= tuple(sorted(random.sample(range(min, max), quantity)))
    ticket_array.add(get_ticket)
    return ticket_array

print(get_numbers_ticket(1, 49, 6))
