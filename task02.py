'''2. Har bir sonni kvadratga oshiring
map() yordamida quyidagi ro'yxatdagi har bir sonni kvadratga oshiring.

nums = [1, 2, 3, 4, 5]
'''

def x(nums,daraja):
    return list(map(lambda x: x** daraja,nums))

nums = [1, 2, 3, 4, 5]

result = x(nums, 2)

print(result)
    