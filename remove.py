def remove(st):
    word = ""
    result = ""
    count = 0

    for i in range(len(st)-1, -1, -1):
        if st[i] == "!":
            count += 1
        else:
            break
    
    result = st[0: len(st)-count]
    print(result)
    
    return result