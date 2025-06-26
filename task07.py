'''7. Narxlarni $ belgisiz olish
Quyidagi narxlar ro’yxatidan $ belgisiz faqat raqamlarni ajrating (lambda bilan).

prices = ["$120", "$340", "$50", "$90"]
'''

def x(prices):
    return [''.join(filter(lambda x: x != ' ',prices)) for i in prices ]

prices = ["$120", "$340", "$50", "$90"]

y = x(prices)

print("Saralangan narxlar:",x)