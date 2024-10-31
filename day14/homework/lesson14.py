# 6
even_numbers = []
for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

# 7
numbers = list(range(1, 51))
for num in numbers[:]:  # ვსარგებლობთ ცალკე ასლისგან
    if num % 2 != 0:
        numbers.remove(num)
print(numbers)

# 8
fruits = ["apple", "banana", "cherry", "strawberry", "mango", "grape", "kiwi", "lemon", "melon", "orange"]
while len(fruits) > 2:
    fruits.pop()
    print(fruits)

#9
numbers = [1, 2, 0, 1, 32, 1, 30, 1, 1, 21, 1, 1, 1]
count = 0
for num in numbers:
 if num == 1:
    count += 1
print(count)

# 10
list_short = []
list_long = []
for _ in range(5):
 word = input("შეიტანეთ სიტყვა: ")
 if len(word) <= 5:
    list_short.append(word)
else:
    list_long.append(word)
print("სიტყვები, სიგრძე <= 5:", list_short)
print("სიტყვები, სიგრძე > 5:", list_long)
