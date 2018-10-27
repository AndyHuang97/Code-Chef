def loadstr(string):
    pos = 1
    di = dict()
    for c in string:
        if c == '.':
            pos += 1
            continue
        di[str(pos)] = c
        pos += 1
    return di

def safe(string):
    safe = 1
    di = loadstr(string)
    flag = 0
    # print(di)
    for key in di:
        if flag == 0 : # 1st iteration
            tempKey = int(key)
            tempValue = int(di[key])
            flag = 1
        else:
            if (tempKey + tempValue) < (int(key) - int(di[key])) :
                tempKey = int(key)
                tempValue = int(di[key])
                safe = 1
            else:
                # print(str(tempKey), str(tempValue))
                # print(key,di[key])
                safe = 0
                break
    if safe :
        print('safe')
    else:
        print('unsafe')

# ------------------------------- Main ----------------------------------------
T = input() #num of test cases

for i in range(int(T)):
    string = input()
    # print(string)
    safe(string)
