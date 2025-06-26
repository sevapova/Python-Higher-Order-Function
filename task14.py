'''14. list.sort bilan joyida o'zgartirish
Quyidagi ro’yxatni uzunlik bo‘yicha joyida sort qiling:

words = ["sun", "mountain", "a", "apple"]
'''

def uzunlik_buyicha_saralash(words):
    words.sort(key=lambda x: len(x))
    return words

words = ["sun", "mountain", "a", "apple"]
x = uzunlik_buyicha_saralash(words)

print("Joyida saralangan:", x)
