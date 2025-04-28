from numpy import lcm
def kiyo_lcm(a):

    lcd = []
    
    for fila in a:
        lista = [x for x in fila if isinstance(x, int) and x%2 != 0]   
        if not lista: return 0
        lcd.append(sum(lista))
    
    return lcm.reduce(lcd)