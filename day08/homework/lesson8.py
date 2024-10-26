#1
# თქვენი სახელი და გვარი
first_name = "dea"
last_name = "devidze"

# ასაკი
age = 15  

for _ in range(age):
 print(first_name, last_name)

#2
for number in range(1, 21):
 print(number)

#3
for number in range(20, -1, -1):
 print(number)

#4
total_sum = sum(range(1, 51))
print(total_sum)

#5
# 1-დან 50-ის ჩათვლით რიცხვების ჯამი
total_sum = sum(range(1, 51))
print(total_sum)

#6
for n in range(1, 6):
 print(n * n)

#7
total_sum = sum(n for n in range(1, 11) if n / 2 == 0)
print(total_sum)

#8
# მოითხოვეთ რიცხვის შეყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# შეამოწმეთ, არის თუ არა ლუწი
if number % 2 == 0:
 print("number is Even")
 print("number is Odd")
