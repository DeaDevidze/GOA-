first_name = "dea"
last_name = "devidze"

full_name = first_name + " " + last_name  # აქ ორი სტრინგი და დამატებითი სივრცე ერთმანეთს ემატება
print(full_name)  # შედეგი იქნება: dea devidze

age = 15
message = "I am " + str(age) + " years old."  # რიცხვი age უნდა გადავიყვანოთ სტრინგში, რომ შევძლოთ მისი კონკატენაცია
print(message)  # შედეგი იქნება: I am 15 years old.

# დღის ჩამონათვალი
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# მომხარებლისგან რიცხვის მიღება
number = int(input("enter a number 1 through 7: "))
print(days_of_week[number - 1])
# ორი რიცხვის მიღება
num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))

result = num1 == num2

print(result) 

age = int(input("enter you age: "))
 # ასაკის შედარება
 # if age = 18:
print("You are adult")
print("You are kid")


num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))
num4 = float(input("enter fourth number: "))

# საშუალო არითმეტიკული
average = (num1 + num2 + num3 + num4) / 4

number_str = "42"
number_int = int(number_str)
print(number_int)  # შედეგი: 42

float_number = 3.14
number_int = int(float_number)
print(number_int)  # შედეგი: 3

binary_str = "1010"
number_int = int(binary_str, 2)
print(number_int)  # შედეგი: 10 (ბაზაში 2)

