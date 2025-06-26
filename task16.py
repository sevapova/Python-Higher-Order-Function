'''16. lambda bilan ro'yxatni qisqartirish
Berilgan ro’yxatdagi faqat string va uzunligi 5 dan katta bo‘lganlarni ajrating:

data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
'''

def uzunligi_5_dan_katta_bolgan_royxatni_saralash(data):
    return list(filter(lambda x: type(x) == str and len(x) > 5, data))


data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

x = uzunligi_5_dan_katta_bolgan_royxatni_saralash(data)

print("Ro'yxatni saralash:", x)