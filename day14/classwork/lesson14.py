# რიცხვების სიის შექმნა
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
 if number % 2 == 0:
    print("{number} არის ლუწი")
else:
    print("{number} არის კენტი")

    # სახელების სიის შექმნა
names = ["Ana", "luka", "dachi", "Nini", "mari", "lizi", "erekle", "anano", "zur", "miriani"]
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i])

# რიცხვების სიის შექმნა
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
odd_sum = 0

for number in numbers:
 if number % 2 == 0:
     even+= number
else:
 odd_sum += number

print("ლუწი რიცხვების ჯამი: {even_sum}")
print("კენტი რიცხვების ჯამი: {odd_sum}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
for number in numbers:
 if number % 2 == 0:
    even_numbers.append(number)

# საშუალო არითმეტიკის გამოთვლა
average = sum(even_numbers) / len(even_numbers)
print("ლუწი რიცხვების საშუალო: {average}")

