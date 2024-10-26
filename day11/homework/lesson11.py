#გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი
#secret_pass = "luka1234"
#user_pass = ''
#tries = 3
#while tries > 0 and user_pass != secret_pass:
#user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
#tries = tries - 1
#if user_pass == secret_pass:
#print("Access granted!")
#elif tries == 0:
#print("You've reached the maximum number of tries. Access denied!")
#else:
#print("Access denied! Try again.")

#2
# ლუწი რიცხვების რაოდენობის საწყისი ცვლადი
even_count = 0

# for loop, 1-დან 50-მდე რიცხვების გასავლელად
for number in range(1, 51):
    if number % 2 == 0:  # არის თუ არა ლუწი
        even_count += 1

# დაბეჭდეთ შედეგი
print("ლუწი რიცხვების რაოდენობა 1-დან 50-მდე:", even_count)

#3
# ცვლადების დაწყება
sum_even = 0  # ლუწი რიცხვების ჯამი
count_even = 0  # ლუწი რიცხვების რაოდენობა
number = 1  

# while loop, 1-დან 100-მდე რიცხვების გასავლელად
while number <= 100:
 if number % 2 == 0:  
     sum_even += number  
     count_even += 1 
number += 1  

# გაანგარიშეთ საშუალო არითმეტიკული
if count_even > 0:
    average_even = sum_even / count_even
    print("1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული:", average_even)
else:print("არ არის ლუწი რიცხვები.")

#4
number = 1  
# while loop, 1-დან 30-მდე რიცხვების გასავლელად
while number <= 30:
 if number % 3 == 0: 
     print(number)
number += 1 

#5
number = int(input("შეიტანეთ რიცხვი: "))

print("number-ის ყველა გამყოფი:")

# for loop, 1-დან მიღებული რიცხვის ჩათვლით
for i in range(1, number + 1):
    if number % i == 0:  # არის თუ არა i გამყოფი
     print(i)

#6
number = float(input("შეიტანეთ რიცხვი: "))

if number > 0:
    print("ეს რიცხვი არის დადებითი.")
elif number < 0:
    print("ეს რიცხვი არის უარყოფითი.")
else:
    print("ეს რიცხვი არის 0.")

#7
year = int(input("შეიტანეთ წელი: "))

# შევამოწმოთ, არის თუ არა წელი ნაკიანი
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year არის ნაკიანი წელი.")
else:
    print("year არ არის ნაკიანი წელი.")

#8
# ქულის შეყვანა
score = int(input("შეიტანეთ ქულა (1-დან 100-ის ჩათვლით): "))

if 1 <= score <= 100:
 if score >= 90:
    print("Your grade is A")
elif score >= 80:
     print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
else:
    print("Your grade is D")


