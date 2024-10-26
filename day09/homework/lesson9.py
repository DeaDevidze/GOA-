#while - სანამ
#infinite loop - უსაასრულო მარყუჟი
#iteration, repeat - გამეორება
#condition - პირობა
#colon - ორწერტილი :
#inital - საწყისი
#range - დიაპაზონი

number = 1
total_sum = 0

while number <= 50:
 total_sum += number
number += 1
print("total_sum")

pin_code = ""

while pin_code != "1234":
 pin_code = input("please,enter PIN code(4 numbers): ")

print("PIN კოდი სწორია!")

target_number = 7
guessed_number = 0

while guessed_number == target_number:
 guessed_number = int(input("enter a number thought 1 _ 10: "))

