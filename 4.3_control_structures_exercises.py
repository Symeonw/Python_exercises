Day_of_week=  input("Enter the day of the week: ")

if Day_of_week == "Monday" or "monday":
  print ("Today is Monday")

day_of_week = input("Enter day of week: ")
weekdays = ["monday", "tuesday","wednesday", "thursday", "friday"]

if day_of_week.lower() in weekdays:
  print ("Today is a weekday")
else:
  print ("Today is a weekend")

  hours_worked = 40
hourly_rate = 30
total_paycheck = hours_worked * hourly_rate

hours_worked1 = input("Enter hours worked: ")
hourly_rate2 = input("Enter houly rate: ")

if int(hours_worked1) > 40:
  hours_worked1 = (int(hours_worked1) - 40) * 1.5 + 40
else:
  hours_worked1 = hours_worked1

weekly_paycheck = int(hours_worked1)  * int(hourly_rate2)
print ("Your total paycheck this week is: ",weekly_paycheck)


i = 5
while i <= 15:
  print (i)
  i += 1

  i = 0
while i <= 100:
  print (i)
  i += 2

  i = 100
while i >= -10:
  print (i)
  i -= 5

  i = 2
while i <= 1000000:
  print (i)
  i =i**2

  i = 100
while i >= 5:
  print (i)
  i -= 5

invalid = True 
while invalid==True:
 numbers = input("Enter odd number between 1 and 50: ")
 if numbers.isdigit() == True and int(numbers) >= 1 and int(numbers) <= 50 and int(numbers) % 2 != 0:
   invalid = False
   break
print ("Number to skip is: ", numbers)

for n in range(50):
    if n % 2 == 0:
      continue
    elif n == int(numbers):
      print ("Skipping number: ", numbers)
      continue
    print ("Here is an odd number: {}" .format(n))
    


 
invalid = True
while invalid==True:
  pos_num = input("Enter positive number: ")
  if int(pos_num) % 2 == 0 and pos_num.isdigit() == True and int(pos_num) > 0:
    invalid == False
    break
for n in range(int(pos_num) + 1):
  print ("Your numbers are: ", n)


invalid = True
while invalid==True:
  pos_num = input("Enter positive number: ")
  if int(pos_num) % 2 == 0 and pos_num.isdigit() == True and int(pos_num) > 0:
    invalid == False
    break
for n in range(int(pos_num), -1, -1):
 print ("Your numbers are: ", n)

for n in range(1,101):
  print (n)



for n in range(1,100):
  if n % 5 == 0 and n % 3 == 0:
    print ("FizzBuzz")
  elif n % 5 == 0:
      print ("Buzz")
  elif n % 3 == 0:
      print ("Fizz")
  continue
  print(n)

num = input("Enter number: ")
not_proceed = True
while not_proceed == True:
  ques = input("Do you want to continue? (Y/N): ")
  if ques == "Y":
    not_proceed == False
    break

for n in range(int(num) + 1):
  n1 = n ** 2
  n2 = n ** 4
  print(n,n1,n2)


