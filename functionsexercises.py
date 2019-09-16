

def is_two(x):
    return x in [2, '2', 'two']

assert is_two(2) == True
assert is_two('2') == True
assert is_two('four') == False
assert is_two(3) == False
assert is_two(4) == False
assert is_two('two') == True


def is_vowel(c):
    if len(c) > 1:
        return False
    c = c.lower()
    if c == 'a':
        return True
    elif c == 'e':
        return True
    elif c == 'i':
        return True
    elif c == 'o':
        return True
    elif c == 'u':
        return True
    else:
        return False


def is_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len(c) == 1 and c.lower() in vowels
    
def is_vowel(c):
    return len(c) == 1 and c.lower() in 'aeiou'
    
assert is_vowel('a') == True
assert is_vowel('e') == True
assert is_vowel('i') == True
assert is_vowel('o') == True
assert is_vowel('u') == True
assert is_vowel('b') == False
assert is_vowel('y') == False
assert is_vowel('A') == True
assert is_vowel('ab') == False
assert is_vowel('aa') == False


def is_consonant(c):
    return not is_vowel(c)

assert is_consonant('c') == True
assert is_consonant('C') == True
assert is_consonant('a') == False


def cap_if_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

def cap_if_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    return word

def cap_if_consonant(word):
    return word.capitalize() if is_consonant(word[0]) else word

assert cap_if_consonant('codeup') == 'Codeup'
assert cap_if_consonant('bayes') == 'Bayes'
assert cap_if_consonant('aardvark') == 'aardvark'



def calculate_tip(percentage, bill_amount):
    if percentage > 1:
        percentage /= 100
    amount_to_tip = percentage * bill_amount
    return amount_to_tip

assert calculate_tip(.2, 20) == 4.0
assert calculate_tip(20, 20) == 4.0
assert calculate_tip(.25, 80) == 20.0

x = 3
x /= 1


def calculate_tip(bill_amount, percentage=.2):
    if percentage > 1:
        percentage /= 100 # percentage = percentage / 100
    amount_to_tip = percentage * bill_amount
    return amount_to_tip

assert calculate_tip(20) == 4.0
assert calculate_tip(20, .2) == 4.0
assert calculate_tip(20, 20) == 4.0
assert calculate_tip(80, .25) == 20.0


def apply_discount(original_price, discount_percent):
    discount_amount = original_price * discount_percent
    return original_price - discount_amount
    
def apply_discount(original_price, discount_percent):
    return original_price * (1 - discount_percent)

assert apply_discount(20, .1) == 18
assert apply_discount(100, .2) == 80.0




def handle_commas(s):
    s = s.replace(',', '')
    return float(s)

def handle_commas(s):
    return float(s.replace(',', ''))

def handle_commas(s):
    return float(''.join([c for c in s if c != ',']))

assert handle_commas('1,000') == 1000.0
assert handle_commas('10') == 10.0
assert handle_commas('1,000,000') == 1000000



'a,b,c,d'.split(',')



list('abcde')



# .join will use a string as "glue" to put a list together
"---".join(['a', 'b', 'c'])
"".join(['a', 'b', 'c'])


# In[74]:


def get_letter_grade(numeric_grade):
    if numeric_grade > 90:
        return 'A'
    elif numeric_grade > 80:
        return 'B'
    elif numeric_grade > 70:
        return 'C'
    else:
        return 'F'

assert get_letter_grade(93) == 'A'
assert get_letter_grade(88) == 'B'
assert get_letter_grade(12) == 'F'


# In[72]:




grade_minimums = (
    ('A+',98.5),('A',91.5),('A-',89.5),
    ('B+',88.5),('B',81.5),('B-',79.5),
    ('C+',78.5),('C',71.5),('C-',69.5),
    ('D+',68.5),('D',61.5),('D-',59.5),
    ('F',0)
)

def get_letter_grade(numeric_grade):
    ubound = max(100, numeric_grade + .01)
    for grade in grade_minimums:
        if numeric_grade < grade[1]:
            ubound = grade[1]
        else:
            return grade[0]
        

assert get_letter_grade(150) == 'A+'
assert get_letter_grade(98.4) == 'A'
assert get_letter_grade(91) == 'A-'
assert get_letter_grade(59.4) == 'F'
assert get_letter_grade(81.5) == 'B'
assert get_letter_grade(89.5) == 'A-'

get_letter_grade(90)


# In[73]:


grades = {
    'A': range(94, 101),
    'B': range(87, 94),
    'C': range(80, 87),
    'D': range(70, 80),
    'F': range(0, 70)
}

def get_letter_grade(n):
    for grade_letter, grade_range in grades.items():
        if round(n) in grade_range:
            return grade_letter
    return 'Error: don\'t know how to get a letter grade for %s' % n

get_letter_grade(80)


# In[78]:


grades.items()


# In[77]:


1.5 in range(0, 3)


# In[79]:


list(range(1, 7))


# In[81]:


name = 'world'

def sayhello():
    return 'hello, {}!'.format(name)

sayhello()


# In[83]:


# name = 'world'

def sayhello(name=name):
    return 'hello, {}!'.format(name)

name = 'codeup'
sayhello()


# In[123]:


x = 14

def changeit():
    x = 37
    return x

x = 27

print(x)
print(changeit())

x = -3

print(x)

