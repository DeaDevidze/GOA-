# ცვლადების შექმნა
integer = 10                    # მთელი რიცხვი
float = 3.14                    # ათწილადი
string = "Hello, World!"        # სტრინგი

# მონაცემთა ტიპების გამოჩენა
print("integer is: type(integer)")  
print("float is: type(float)")      
print("string is: type(string)")    
       

user_input = input("enter a number: ")

# შევამოწმოთ, არის თუ არა რიცხვი მთელი
number = int(user_input)
print("enter a number {number} არის integer.")


a = 5
b = 5
result = (a == b)
print(result)  # შედეგი: True

x = 10
y = 5
result = (x == y)
print(result)  # შედეგი: false

m = 15
n = 10
result = (m > n)
print(result)  # შედეგი: True

p = 8
q = 12
result = (p < q)
print(result)  # შედეგი: True
r = 20
s = 20
result = (r == s)
print(result)  # შედეგი: True

# and 
print("and oparation:")
print("True and True True and True")   # True
print("True and False True and False")  # False
#or
# or ოპერატორი
print("or oparation:")
print("True or True True or True")     # True
print("True or False True or False")   # True


# ასაკის მიღება როგორც სტრინგი
age_str = input("enter age: ")

print ("enter age type : type(age_str)")  # სტრინგი
#?
age_int = int(age_str)
print(" age as integer: age_int type(age_int)")  # მთელი რიცხვი

age_float = float(age_str)
print("age as float: age_float, ტიპი: type(age_float)")  



# მომხარებლის საყვარელი რიცხვის შეყვანა
favorite_number = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))

# ლუწობის შემოწმება და შესაბამისი შეტყობინების გაწერა
print("favorite_number არის ლუწი' if favorite_number 2 == 0 else კენტი.")




name = input("enter your name: ")
age = int(input("enter your name: "))

# სრულწლოვანების შემოწმება
if age <= 18:
 print("your adult age is conformed.")
print("your adult age is not comformed.")

# სახელის შედარება
my_name = "your name"  
if name == my_name:
 print("your name match")
print("your name doesnt match.")

