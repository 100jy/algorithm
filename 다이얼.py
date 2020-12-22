letter = input()
suma = len(letter)
arr = [('ABC',2),('DEF',3),('GHI',4),('JKL',5),
       ('MNO',6),('PQRS',7),('TUV',8),('WXYZ',9)]

for i in letter:
    for j in arr:
        if i in j[0]:
            suma += j[1]

print(suma)




