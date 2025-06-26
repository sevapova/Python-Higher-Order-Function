'''1. Foydali sonlarni ajratish
Berilgan ro'yxatdan musbat sonlarni filter() yordamida ajrating.

numbers = [4, -2, 0, 7, -9, 3, -1, 5]
'''

def x(numbers):
    return list(filter(lambda x: x > 0,numbers))

numbers = [4, -2, 0, 7, -9, 3, -1, 5]

positive_numbers = x(numbers)

print(positive_numbers)