def list_animals(animals):
    
    result = ""
    
    for i in range(len(animals)):
        
        element = str(i+1) + ". " + animals[i] + "\n"
        result += element
    
    return result