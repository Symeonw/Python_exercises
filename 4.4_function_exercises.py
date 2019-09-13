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
    for n in x:
        x = x.replace(",", "")
        try:
            int(n)
            return x
        except:
            return "not int"
        
handle_commas("1,2,3,4")

def get_letter_grade(x):
    grade = ()
    if isinstance(x, int) == False or x > 100 or x < 0:
        print ("Must enter numerical grade greater than zero and less than 100!")
    elif x > 89:
        grade = "A"
        return f"Grade is: {grade}"
    elif x > 79:
        grade = "B"
        return f"Grade is: {grade}"
    elif x > 69:
        grade = "C"
        return f"Grade is: {grade}"
    elif x > 59:
        grade = "D"
        return f"Grade is: {grade}"
        
get_letter_grade(60)


def remove_vowels(word):
    z = list(word)
    vowel = ["a","e","i","o","u"]
    for n in z:
        if set(vowel).intersection(n.upper().lower()):
            z.remove(n)
    word = ''.join(z)
    return word

remove_vowels("Dogsiodfaosdfaoefhasdof")

def normalize_name(word):
    vpi = ["@","%","$","#","^","&","*","(",")","+","=","~","`"]
    word = word.replace(" ", "_").strip().lower()
    z = list(word)
    for n in z:
        if set(vpi).intersection(n):
            z.remove(n)
        
    word = ''.join(z)
    return word

normalize_name("DGOIDFUS(^D&$&A%$D&SAf f ad a    )")



