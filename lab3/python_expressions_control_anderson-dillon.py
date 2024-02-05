#python boolean
print(f"a: {30 > 14}")
print(f"b: {7 == 10}")
print(f"c: {2 == 3}")
print(f"d: {3 == 3}")

print("two is equal to 3:",int(2==3))
print("three is equal to 3:",int(3==3))

#literals and variables
myname = "Dillon"
myage = 31
print(f"a: {73}")
print(f"b: {'Whats Up'}")
print(f"c: {False}")
print(f"d: {myname}")
print(f"e: {myage}")

#precedence
print((3 - 4 + 5),(4 - 7 + 8))
print((3 * 6 + 2),(5 * 2 + 3))

#Relational Operators
print(f"is 'Bob'=='robert'? {'bob'=='robert'}")

#Equality Operator
my_name = "bob"
print("assignment: ",my_name)
print("equality: ",my_name == "bob")

#Comparison Operator
print("comparison:", "dd" < "e")
print("comparison:", 4 < 7)

a = 6
b = 5

print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a < b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

#If Statement
bank_balance = 70
if bank_balance < 100:
  money = 2000
  bank_balance += money

#Else Statement
bank_balance = 70
if bank_balance < 100:
  money = 2000
  bank_balance += money
else:
    print("balance is less than or equal to 100.")

#Elif Statement
bank_balance = 900
savings = 300
if bank_balance < 200:
  money = 1000
  bank_balance += money
elif bank_balance > 100:
  savings +=50
  bank_balance -= 50
else:
    savings += 100
    bank_balance -= 100
print(bank_balance)
print(savings)

#Ternary Operator
fuel = 3
print("Fill tank now" if fuel <= 3 else "There's enough fuel")

#While Loop
fuel = 13
while fuel > 2:
  #keep driving
  print("There's enough fuel")
  fuel -= 2

#For Loop
books = ['The Hobbit', 'The Fellowship of the Ring','The Two Towers', 'The Return of the King']
for book in books:
  print(f'book: {book}')

for i in range(5):
    print(f'i: {i}')

for count in range(16):
    print(f"{count} times 14 is {count * 14}")
    if count ==9:
        break

for count in range(16):
    print(f"{count} times 14 is {count * 14}")
    if count ==9:
        continue
    print(f"{count} times 14 is {count * 14}")



