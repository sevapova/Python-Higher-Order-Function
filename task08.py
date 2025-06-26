'''8. Yoshi bo'yicha sortlash
Quyidagi lug’atdagi odamlarni yosh bo’yicha o’sish tartibida saralang.

people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
'''

def age_sorted(people):
    return sorted(people, key = lambda x: x['age'])

people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

age = age_sorted(people)

print("Odamlarni yoshi bo'yicha saralash:",age)

