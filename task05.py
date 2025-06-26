'''5. lambda bilan ko'paytirish
Har bir elementni 5 ga ko'paytirish uchun map() va lambdadan foydalaning.

nums = [2, 4, 6, 8]
'''

def multifly (nums):
    return list(map(lambda x: x * 5,nums))

nums = [2, 4, 6, 8]
x = multifly(nums)

print("Ko'paytirish:",x)