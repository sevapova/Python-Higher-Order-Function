'''11. Juft sonlarning kvadratlari
Faqat juft sonlarni tanlab, ularning kvadratlarini filter() + map() bilan hisoblang.

nums = list(range(1, 21))
'''
def juf_sonlar(nums):
    x = filter(lambda x: x % 2 == 0,nums )
    y = map(lambda x: x ** 2, x)
    return list(y)


nums = list(range(1, 21))
x = juf_sonlar(nums)

print("Juft sonlar:",x)