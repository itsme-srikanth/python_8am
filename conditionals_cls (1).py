# conditionals : Statements that will be executed based on certain conditions..

# a=12

# print(a,"is greaterthan 30")


# if statement:
# if-else statement:
# if-elif-else statement:


# if statements:


# Indentation : 

"""
if condition:
    statements
"""

a=45

# if a>30:
#     print(a,"is greterthan 30")


# if-else statements

# if condition:
#     statements
# else:
#     statements

# comments -- 

# a=18
# if a>30:
#     print(a,"is greaterthan 30")
# else:
#     print(a,"is lessthan 30")

# if-elif-else statements:

# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# a=27

# if a==30:
#     print(a,"is equal to 30")
# elif a>30:
#     print(a,"greaterthan 30")
# else:
#     print(a,"is lessthan 30")

# marks = int(input("Enter marks:")) # '32'


# print(type(marks))
# if marks>=70:
#     print("You got distinction")
# elif marks>=60 and marks<70:
#     print("You got first class")
# elif marks>=50 and marks<60:
#     print("You got second class")
# elif marks>=40 and marks<50:
#     print("You got third class")
# else:
#     print("You are not eligible.")

# hero_name = input("Enter Hero name:")

# if hero_name == "Balayya":
#     print("Jai balayyya!")
# elif hero_name == "pavankalyan":
#     print("Babu laka babu kalyan babu")
# elif hero_name == "mahesh":
#     print("Rock star")
# elif hero_name == "NTR":
#     print("Young tiger")
# else:
#     print("Hero no found")


# Nested Conditionals.. -- Writing conditionals inside other conditional statements.. 

# if condition:
#     if condition:
#         statements
#     else:
#         statement
# elif condition:
#     if condition:
#         statement
# else:
#     statements


# hero_name = input("Enter your hero name:")

# if hero_name == 'Balayya':
#     movie_name = input("Enter balayya movie name:")
#     if movie_name == 'Legend':
#         dialogue = input("Enter dialogue")
#         # print("Seat kadu kada assembly gate kuda takanivvanu")
#         print(dialogue)
#     elif movie_name == 'Simha':
#         print("Chudu oka vipa chudu rendo vipu chudali anukoku.")
#     else:
#         print("No dialogue")
# elif hero_name == 'Chiru':
#     movie_name = input("Enter chiru movie name:")
#     if movie_name == 'Indra':
#         print("Veera shankar reddy mokka kada ani peekestha peeka kostha!")
#     elif movie_name == "khaidi150":
#         print("I'm Waiting")
# elif hero_name == "pawankalyan":
#     movie_name = input("Enter pawankalyan movie name:")
#     if movie_name == 'Gabbarsingh':
#         print("Last punch mandi ithe aa kick aa veru appa")
#     elif movie_name == "Kushi":
#         print("Nenu chudaledu")
#     else:
#         print("No found")
# else:
#     print("Hero data doesnt exist!")


# Task1:
# pin1 = 1234
# account_type1 = "saving"
# ENter your pin: 1234
    # ENter your account type : saving
        # ENter the amount to withdraw: 5000
            # 5000 has be debited from your account.. 
    # Enter your account type : current
        # Account type doesnot match
# ENter pin : 4567
    # Pin is not correct!