type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a':[]})
# What data type would best represent:
# A term or phrase typed into a search box? String
# If a user is logged in? Boolean
# A discount amount to apply to a user's shopping cart? Float
# Whether or not a coupon code is valid? Boolean
# An email address typed into a registration form? String
# The price of a product? Float/Int
# A Matrix? Set
# The email address collected from a registration form? Dictionary
# Information about applicants to Codeup's data science program? List of dictionaries
# Output Error:
 '1' + 2
 # Output: 2
 6 % 4
# Output: Int
type(6%4)
# Output: type
type(type(6%4))
# Output: Error
'3 + 4 is' + 3 + 4
# Output: False
0 < 0
# Output: False
'False' == False
# Output: False
True == 'True'
# Output: True
5 >= -5
# Output: Error
!False or False
# Output: Error: Correction: True
True or "42"
# Output: Error
!True && !False
# Output: 1
6%5
# Output: False
5 < 4 and 1 == 1
# Output: False
"codeup" == "codeup" and "codeup" == "Codeup"
# Output: True; Correction: Error
4 >= 0 and 1 !== '1'
# Output: True
5%2 != 0
# Output: Error
[1] + 2
# Output: [1,2]
[1] + [2]
# Output: Error, Correction: [1, 1]
[1] * 2
# Output: Error
[1] * [2] 
# Output: True
[] + [] == []
# Output: {}: Correction: Error
{} + {}

def number_of_days_rented(days):
    for day in days:
        daily_cost = [day * 3 for day in days]
        total_cost = sum(daily_cost)
        return total_cost

number_of_days_rented([3,5,1])

Company_income = {"Google": 400, "Amazon": 380, "Facebook":350}
Company_hours = {"Google": 6, "Amazon": 4, "Facebook": 10}

total_income = sum({Company_income[x] * Company_hours[x] for x in Company_income})

print(total_income)

Class_avaliable = {"class":True, "Class": False}
Class_Schedule = {"class": }
def can_be_enrolled(data_1,data_2):
    for class in Class_avaliable:
        if class == data_1 and class == True:
            Can_attend = True
            Else:
             return False
    for 
        

