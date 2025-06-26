'''10. Matndan raqamlarni ajratish
Berilgan matndan faqat sonlarni ajrating:

text = ["apple", "34", "banana", "100", "abc", "75"]
'''

def faqat_sonlar(text):
    return sorted(filter(str.isdigit, text))

text = ["apple", "34", "banana", "100", "abc", "75"]

c = faqat_sonlar(text)

print(c)