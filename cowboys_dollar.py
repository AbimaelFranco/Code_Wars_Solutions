def cowboys_dollars(boots):
    boot = 0
    counter = [0, 0]
    aux = ""
    for i in boots:
        for j in i:
            
            if j == "(" and aux == "":
                aux += "("
            elif j == "1" and aux == "(":
                aux += "1"
            elif j == ")" and aux == "(1" and boot == 0:
                counter[boot] = counter[boot] + 1
                aux = ""
            elif j == ")" and aux == "(1" and boot == 1:
                counter[boot] = counter[boot] + 1
                aux = ""
            elif j == "&":
                aux = ""
                break
            else:
                aux = ""
            
        boot += 1
    
    return "This Rhinestone Cowboy has {} dollar bills in his right boot and {} in the left".format(counter[1], counter[0])