'''7. Narxlarni $ belgisiz olish
Quyidagi narxlar ro’yxatidan $ belgisiz faqat raqamlarni ajrating (lambda bilan).

prices = ["$120", "$340", "$50", "$90"]
'''

def x(prices):
    return list(map(
        lambda price: float(price.replace("$","")),
        prices))

prices = ["$120", "$340", "$50", "$90"]

y = x(prices)

print("Saralangan narxlar:",x)