def cowboys_dollars(boots):
    boot = 0
    counter_left = 0
    counter_right = 0
    aux = ""
    for i in boots:
        for j in i:
            
            if j == "(" and aux == "":
                aux += "("
            elif j == "1" and aux == "(":
                aux += "1"
            elif j == ")" and aux == "(1" and boot == 0:
                counter_left += 1
                print("billete detectado en izquierda")
                aux = ""
            elif j == ")" and aux == "(1" and boot == 1:
                counter_right += 1
                print("billete detectado en derecha")
                aux = ""
            elif j == "&":
                aux = ""
                break
            else:
                aux = ""
            
        boot += 1
    print(counter_left)
    print(counter_right)
    
    return "This Rhinestone Cowboy has {} dollar bills in his right boot and {} in the left".format(counter_right, counter_left)