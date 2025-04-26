def replace_exclamation(st):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    is_vowel = False
    
    for counter in range(len(st)):
        
        letra = st[counter]
        
        for counter2 in range(len(vowels)):
            if letra == vowels[counter2]:
                result += "!"
                is_vowel = True
                break
                
        if is_vowel == False:
            result += letra
        
        is_vowel = False

    
    return result