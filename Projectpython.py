print ("~~~Welcome to your terminal checkbook!~~~")
print(" ")
print ("What would you like to do? \n 1) View current account balance\n 2) Record new Debt\n 3) Record new Credit\n 4) Exit")
print(" ")

invinp = True
while invinp == True:
  ui_choice = input("Select option: ")
  if ui_choice.isdigit() == True and int(ui_choice) == 5:
    print("Additional instruction: Please enter a number between 1 and 4, such as 1,2,3 or 4.")
  elif ui_choice.isdigit() == True:
    invinp == False
    break
  else:
    print ("Please enter a number or enter 5 for further direction.")
ui_choice = int(ui_choice)  
if ui_choice == 1:    
  print ("***Current acount balance place holder***")
elif ui_choice == 2:
  print ("****New Debit palce holder*****")
elif ui_choice == 3:
  print ("***New Credit placeholder***")
elif ui_choice == 4:
  print ("Thank you")
elif ui_choice == 5:
  print("Additional instruction: Please enter a number between 1 and 4, such as 1,2,3 or 4.")

