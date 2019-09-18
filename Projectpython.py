def start():
  print ("~~~Welcome to your terminal checkbook!~~~\n \nWhat would you like to do? \n 1) View current account balance\n 2) Record new Debt\n 3) Record new Credit\n 4) Exit")

  help_please = 0
  invalid_input = True
  global ui_choice
  while invalid_input == True:
    ui_choice = input(" \nSelect option: ")
    if ui_choice.isdigit() == True and int(ui_choice) == 5:
      print("Additional instruction: Please enter a number between 1 and 4, such as 1,2,3 or 4.")
    elif ui_choice.isdigit() == True and int(ui_choice) >= 1 and int(ui_choice) <= 5:
      invalid_input == False
      break
    elif help_please == 5:
      print ("Are you ok?")
    else:
      print ("Please enter a number or enter 5 for further direction.")
      help_please = help_please + 1
#Additional information/Balance holders
debt_ledger_add = 0
credit_ledger_add = 0
inter_exit = ()
debt_ledger = -100
credit_ledger = 500
not_exit = True
while not_exit == True: 
  
  if inter_exit == "N" or inter_exit == ():
    start()
    inter_exit = ()
  ui_choice = int(ui_choice)  
  if ui_choice == 1:    
    if inter_exit == "Y":
        inter_exit = ()
        break
    global general_ledger
    general_ledger = credit_ledger + debt_ledger
    print ('---------------------------------------')
    print ("Current Balance is:",general_ledger)
    while True:
      print ('---------------------------------------')
      inter_exit = input(" \nWould you like to remain on main menu?(Y/N)") 
      if inter_exit == "Y":
        pass
      elif inter_exit == "N":
        break
      else:
        print (" \n*Please enter 'Y' or 'N'.*")
#Following is for recording new debts
  elif ui_choice == 2:
    if inter_exit == "N":
      break
    else:
      print ("Loading Debt Recording Aparatus...")
      debtint = input("Please enter amount to debt: ")
    try:
      float(debtint)
    except:
      print ("Please enter only numbers.")
      continue
    else:
      debtint = float(debtint)
      debt_ledger_add += debtint
      debt_ledger -= debt_ledger_add
      debt_ledger = round(debt_ledger,2)
   
    while True:
      print('-----------------------------------------')
      if inter_exit == "Y":
        inter_exit = ()
        break
      else:
        inter_exit = input(" \nAccepted input\n \nWould you like to enter an additional debt?(Y/N)")
        if inter_exit == "Y":
          inter_exit = "Y"
          continue
        elif inter_exit == "N":
          break
        else:
          print (" \n*Please enter 'Y' or 'N'.*")
        
     
    
#Following if for recoding new credits
  elif ui_choice == 3:
    print ("Loading Credit Recording Aparatus...")
    creditint = float(input("Please enter amount to credit: "))
    credit_ledger_add += creditint
    credit_ledger += credit_ledger_add
    credit_ledger = round(credit_ledger,2)
    while True:
      print('-----------------------------------------')
      if inter_exit == "Y":
        break
      else:
        inter_exit = input(" \nAccepted input\n \nWould you like to enter an additional credit?(Y/N)")
        if inter_exit == "Y":
          inter_exit = "Y"
          continue
        elif inter_exit == "N":
          break
        else:
          print (" \n*Please enter 'Y' or 'N'.*")
    
#Following is for exiting program
  elif ui_choice == 4:
    not_exit == False
    print ("Thank you")
    break
#Following is additional information
  elif ui_choice == 5:
    print("Additional instruction: Please enter a number between 1 and 4, such as 1,2,3 or 4.")

print ("***PROGRAM TERMINATED***")