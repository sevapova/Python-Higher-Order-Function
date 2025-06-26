'''6. Email domenlarini ajratish
Quyidagi email ro’yxatidan faqat gmail.com domeniga tegishlilarni ajrating.

emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
'''

def saralash(emails):
    return emails.endswith('@gmail.com')

emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
x = list(filter(saralash,emails))

print(x)