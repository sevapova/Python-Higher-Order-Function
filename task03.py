'''3. Eng kichik va eng katta
min() va max() yordamida quyidagi ro'yxatdan eng kichik va eng katta sonni toping.

numbers = [18, 29, 3, 45, 7, 12]
'''

def x(numbers):
    if not numbers:
        return None, None
    return max(numbers) , min(numbers)


numbers = [18, 29, 3, 45, 7, 12]

eng_katta, eng_kichina = x(numbers)

print("Eng kattasi: ", eng_katta)
print("Eng kichkina: ", eng_kichina)