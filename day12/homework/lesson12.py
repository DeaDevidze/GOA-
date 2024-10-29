# ცვლადი, რომელიც იწყება 1-დან
number = 1
while number <= 50:
 if number % 4 == 0: 
     print(number ** 3) 
 number += 1  # მოიმატეთ რიცხვი

# 2
for number in range(1, 101):
 if number % 3 == 0 and number % 5 == 0: 
     print("FizzBuzz", number)  # "FizzBuzz" და რიცხვი
 elif number % 3 == 0:  
    print("Fizz", number)  #"Fizz" და რიცხვი
 elif number % 5 == 0: 
    print("Buzz", number)  #"Buzz" და რიცხვი

even_sum = 0  # ლუწი რიცხვების ჯამის ცვლადი
odd_sum = 0   # კენტის რიცხვების ჯამის ცვლადი

# 3
for number in range(1, 21):
 if number % 2 == 0: 
    even_sum += number  # დაამატეთ ლუწი რიცხვი ჯამში
 else:  # თუ რიცხვი არ არის ლუწი, მაშინ არის კენტი
    odd_sum += number  # დაამატეთ კენტი რიცხვი ჯამში

# ორივე ჯამის აყვანა მე-5 ხარისხში
even_sum_power = even_sum ** 5
odd_sum_power = odd_sum ** 5

# დაბეჭდეთ ის, რაც მეტია
print(max(even_sum_power, odd_sum_power))


# 4
result = True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5
print(result)
#ერთი არის მთელი რიცხვი მეორე სტრინგი


# 5
number = int(input("enter a number: ")) 

is_prime = True 
if number < 2:  
 is_prime = False
else:
 for i in range(2, int(number ** 0.5) + 1):  
    if number % i == 0:  
     is_prime = False
    break 
# შედეგის დაბეჭდვა
if is_prime:
    print("Number is prime")  # თუ მარტივია
else:
    print("Number is not prime")  # თუ არა

