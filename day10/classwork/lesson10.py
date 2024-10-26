# მოითხოვეთ ასაკის შეყვანა
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

# შეამოწმეთ, არის თუ არა ლუწი
if age %2 == 0:
 print("თქვენი ასაკი არის ლუწი: age")
 print("თქვენი ასაკი არის კენტი: age")

for number in range(10, 51):
 if number % 2 == 0:
  print(number)



# რიცხვის შრყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# გამოთვალეთ, რამდენჯერ შედის რიცხვი 100-ში
count = 100 // number

number = 1
total_sum = 0

while number <= 20:
 if number % 2 != 0:  # შევამოწმოთ, არის თუ არა კეტი
  total_sum += number
 number += 1

print("ჯამი:", total_sum)

# ორი რიცხვის შეყვანა
number1 = float(input("შეიტანეთ პირველი რიცხვი: "))
number2 = float(input("შეიტანეთ მეორე რიცხვი: "))

# შეადარეთ რიცხვები
if number1 > number2:
 print("მეტი რიცხვია: number1")
print("მეტი რიცხვია: number2")
print("Both numbers are equal")

#ფაქტორიალი არის მთელი რიცხვის (n) ნამრავლი მისი ყველა მთელ დადებით რიცხვზე, რომელიც ნაკლებია ან ტოლია n-ის. ფაქტორიალზე სიმბოლურად წერენ n!.
# მოითხოვეთ რიცხვის შეყვანა
number = int(input("შეიტანეთ რიცხვი: "))

# გამოთვალეთ ფაქტორიალი
factorial = 1

for i in range(1, number + 1):
 factorial *= i


#რიცხვის შეყვანა
number = int(input("შეიტანეთ რიცხვი: "))

# კვადრატების ჯამი
total_sum = sum(i * i for i in range(1, number + 1))
print(total_sum)


# შეინახეთ ჩაფიქრებული რიცხვი
secret_number = (1, 20)
guessed_number = 0

print("გამოიცანით რიცხვი 1-დან 20-ის ჩათვლით!")

# while loop, სანამ მომხმარებელი არ გამოიცნობს რიცხვს
while guessed_number != secret_number:
 guessed_number = int(input("შეიტანეთ თქვენი ვარაუდი: "))
    
 if guessed_number  < secret_number:
   print("Too high!")
   guessed_number < secret_number
 print("Too low!")

# მომხმარებელი სწორად გამოიცნო
print("You win!")
