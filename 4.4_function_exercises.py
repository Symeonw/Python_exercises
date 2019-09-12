et = input("Please enter two: ")

def is_two(x):
  if x == 2 or x == "2":
    return True
  else:
    return False

is_two(et)

def is_vowel(x):
  vowel = ["a","e","i","o","u"]
  if set(vowel).intersection(x.upper().lower()):
    return True
  else:
    return False

is_vowel("PPPPPPoPP")

def is_consonant(x):
  vowel = ["a","e","i","o","u"]
  if set(con).intersection(x.upper().lower()):
    return False
  else:
    return True

is_consonant("DJUjAysSOAq")

def cap_string(x):
    con = ["b", "c","d","f","g","h","k","l","m","n","p","q","q","r", "s", "t", "v","x", "z"]
    if type(x) != str:
        return False
    else:
         for n in con:
             if x[0].upper().lower() == n:
                 return (x.lower().upper().capitalize())
        
       
cap_string("DODGS")

def calculate_tip(tip,bill):
    if tip > 1 or tip < 0 and tip.isdigit() == False:
        print ("Error")
    elif bill < 0 and bill.isdigit() == False:
        print ("Error")
    else:
        return tip*bill

calculate_tip(.15, 10)


def apply_discount(origin_price,discount):
    if discount > 1:
        discount = discount/100
        if discount < 0:
            print ("Error: discount must be greater than zero percent.")
        if origin_price < 0:
            print ("Error: original item price must be greater than zero.")
        else:
            return origin_price - origin_price*discount

apply_discount(100, 50)

def handle_commas(x):
    if x.isdigit() == True:
        for x.replace(",","")
    else:
        print ("Error, is not digit.")

handle_commas(1,2,3,4)