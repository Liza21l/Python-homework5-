# total_sum = 0
# for number in range(1, 100 +1):
#     if number % 2 != 0:
#         total_sum += number

# print("Сума всіх непарних чисел від 1 до 100:", total_sum)

#####################

user_input = input("Введіть рядок: ")
first_letter = user_input[0]
count = 0

for letter in user_input:
    if letter == first_letter:
        count += 1

print(f"Кількість входжень першої літери '{first_letter}' у рядку: {count}")


