# მომხმარებლისგან პირველი რიცხვის შეყვანა
first_number = int(input("enter the fisrt number: "))  # იქმნება ცვლადი პირველი რიცხვისთვის

# მომხმარებლისგან მეორე რიცხვის შეყვანა
second_number = int(input("enter the second number: "))  

# ორივე რიცხვის მე-3 ხარისხში აყვანა
first_number_cubed = first_number ** 3  
second_number_cubed = second_number ** 3  

# რიცხვების ჯამის გამოთვლა
result = first_number_cubed + second_number_cubed 

# შემოწმება, არის თუ არა ჯამი ლუწი
if result % 2 == 0:  # თუ ჯამი იყოფა 2-ზე
    print("Result is Even")  # დაბეჭდეთ "Result is Even"
else:  # თუ ჯამი არ იყოფა 2-ზე
    print("Result is Odd")  # დაბეჭდეთ "Result is Odd"
