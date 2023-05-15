a = 3
b = 5
c = a
a = b
b = c
print('a=',a, 'b=',b)

a = 8
b = 7
a = a + b
b = a - b
a = a - b
print('a=',a, 'b=',b)

a = 4
b = 2
a = a + b
b = a - b
a = a - b
print('a=',a, 'b=',b)



input_string = input("Введіть речення: ")
words = input_string.split("_")
capitalized_words = [word.capitalize() for word in words]
output_string = "" .join(capitalized_words)
print(output_string)



name = input("Enter name: ")
birthdate = input("Enter date of birth: ")
deathdate = input("Enter date of death: ")
age = int(deathdate[:4]) - int(birthdate[:4])
print("Name: " + name)
print(f"Age: {age}")



input_str = input("enter namber: ")
digits = list(input_str)
digits = [int(digit) for digit in digits]
print(f"сумма чисел: {sum(digits)}")


namber = int(input("enter namber: "))
namber_sum = (namber // 100) + ((namber // 10) % 10) + (namber % 10)
print(f"сумма чисел: {namber_sum}")




