import string
str = input()

alpha = string.ascii_lowercase

for i in alpha:
    if i in str:
        print(str.find(i))
    else:
        print('-1')


