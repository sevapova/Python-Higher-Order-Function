'''12. Talabalarni baho bo‘yicha tartiblang
Baholar bo‘yicha saralash (kichikdan katta):

students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]
'''

def baho_boyicha_saralash(students):
    return sorted(students , key = lambda x: x['grade'])


students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

saralash = baho_boyicha_saralash(students)

print("Baho bo'yicha saralash:",saralash)