'''13. Top 3 eng uzun so‘z
Matndagi eng uzun 3 ta so‘zni toping:

sentence = "Functional programming in Python is very powerful and elegant"
'''

def eng_uzun_soz(sentence):
    words = sentence.split()
    return sorted(words, key=len, reverse=True)[:3]

sentence = "Functional programming in Python is very powerful and elegant"
x = eng_uzun_soz(sentence)

print("Eng uzun so'zlar:", x)
