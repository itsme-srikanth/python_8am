# String Methods:

# print(dir(str))

# startswith,endswith,islower,isupper,lower,upper,isalpha,isalnum,isdigit,title,capitalize,swapcase,index,find,count,split,strip,replace,zfill,format.....

# startswith() - to check whether the main string is starting with what i have specified. 

str1 = "Python is a programming language"

# print(str1.startswith('p'))

# print(str1.startswith('Python'))

# # endswith() - to check whether the main string is ending with what i have specified.

# str1 = "Python is a programming language"

# print(str1.endswith('e'))

# print(str1.endswith('guage'))

# islower() & isupper()

# Its just for checking whether the string is upper or lower.

str1 = "Python is a programming language"

# print(str1.islower())

# str2 = "python is a programming language"

# print(str2.islower())

# print(str1.isupper())

# lower() & upper() - It will convert all the alphabets into respective lower and upper cases..

# print(str1.lower())

# print(str1.upper())

# isalpha() -- its for just checking whether everything inside the string are alphabets only..


# str1 = "Python is a programming language"

# print(str1.isalpha())

# isalnum() -- its for checking whether everyhting inside the string are alphanumerics. 

# str1 = "Pythoon123"

# print(str1.isalnum())

# isdigit() -- Its to just check whether everything inside the string are numbers only..

# str1 = "994499494444"
# print(str1.isdigit())

# title() -- It convert the string into title format(each word starting character will be converted to uppercase inside the string.)

# str1 = "Python is a programming language"

# print(str1.title())

# capitalize() - - It will convert the starting character of your string into uppercase..

# str1 = "Python is a ProgramminG language"

# print(str1.capitalize())

# swapcase() -- Its for converting lower to upper and upper to lower case..

# print(str1.swapcase())

# index - It will return the index of the element inside the main string..
    # if the element is repeated multiple times inside the string, it will return the starting occurence of the element inside the string..

str1 = "python is a programming language"

# print(str1.index('g'))

# print(str1.index('program'))

# print(str1.index('p'))

# find - It will return the index of the element inside the main string..
    # if the element is repeated multiple times inside the string, it will return the starting occurence of the element inside the string..

# str1 = "python is a 165programming language"

# print(str1.find('g'))

# print(str1.find('program'))

# print(str1.find('p'))

# print(str1.find('1'))


# print(str1.index('z')) # this will throw the error as the element is not present..

# print(str1.find('z')) # this will return -1...
# print(3+4)

# count() - It will return how many times a particular substring is repeated isnide the main string,

str1 = "python is a programming language"

# print(str1.count('g'))

# print(str1.count('python'))

# split() -- It will split the string into multiple strings based on the space..

# print(str1.split())

# print(str1.split('g'))

# print(str1.split('z'))

# print(str1.split('ng'))


# username
# firstname
# lastname
# email

# email = "sanjeeva.reddy@gmail.com"

# print(email)
# print(email.split('@'))
# username = email.split('@')[0]
# print(username)

# if '.' in username:
#     print(username.split('.'))
#     first_name = username.split('.')[0]
#     lastname = username.split('.')[1]
#     print(first_name)
#     print(lastname)
# elif '_' in username:
#     print(username.split('_'))
#     first_name = username.split('_')[0]
#     lastname = username.split('_')[1]
#     print(first_name)
#     print(lastname)
# else:
#     first_name = username
#     print(first_name)


# strip() -- its for removing the escape sequences(\n,\t) at starting and ending of the string..
# \n - new line
# \t - tabspace
# str2 = "\n\tPython is \t used in \n webdevelopment using \t Django framework\n"

# # print(str2)

# print(str2.strip())

# sample = "\n\n\nhdhjahjsajhjhajh\n\n\n\n"

# # lstrip() - same strip operation but only towards left side..
# # rstrip() - same strip operation but only towards right side..

# zfill() -- Its for filling up with zeros..


# 00001
# 00002

# 99999

# str1 = "748474"

# print(str1.zfill(10))

# str2 = "74738389983498"

# print
# print(str2.zfill(10))