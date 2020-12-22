string = input()
cnt = 0

first = ['c','d','l','n','s','z']
second = ['c=','c-','d-','lj','nj','s=','z=']
third = ['dz=']

while True:
    if string[0] in first:
        if len(string) == 1:
            print(cnt+1)
            break
        elif string[:2] in second:
            string = string[2:]
        elif len(string) > 2:
            if string[:3] == 'dz=':
                string = string[3:]
            else:
                string = string[1:]
        else:
            string = string[1:]
    else:
        string = string[1:]

    cnt += 1

    if len(string) == 0:
        print(cnt)
        break



