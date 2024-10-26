# შეინახეთ პაროლი
correct_password = "goa1234"
attempts = 3

print("გთხოვთ, შეიტანოთ პაროლი.")

# while loop, სანამ არსებობს ცდები
while attempts > 0:
  user_input = input("შეიტანეთ პაროლი: ")

if user_input == correct_password:
      print("წვდომა მიღებულია!")
        
attempts -= 1
print("სცადეთ ხელახლა.")
print("მცდელობები დარჩა: attempts")

# თუ ყველა ცდა ამოიწურა
if attempts == 0:
 print("ყველა მცდელობა ამოიწურა. პაროლი არასწორია.")
