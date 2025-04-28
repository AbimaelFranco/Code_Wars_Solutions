def sort_string(s, ordering) -> str:
    string_sorted = ""
    auxiliar = []
    ordering_fixed = ordering_fix(ordering)
    
    # Add characters from s to string_sorted based on ordering_fixed
    for m in ordering_fixed:
        for n in s:
            if m == n:
                string_sorted += n
    
    # Add characters from s that are not in ordering_fixed to auxiliar
    for n in s:
        if n not in ordering_fixed:
            auxiliar.append(n)

    # Append characters from auxiliar to string_sorted
    for n in auxiliar:
        string_sorted += n
    
    return string_sorted

def ordering_fix(ordering) -> list[str]:
    ordering_fixed = []
    letter_exists = False
    
    for l in ordering:
        for m in ordering_fixed:
            if l == m:
                letter_exists = True
                break
        if letter_exists == False:
            ordering_fixed.append(l)
        letter_exists = False
    return ordering_fixed