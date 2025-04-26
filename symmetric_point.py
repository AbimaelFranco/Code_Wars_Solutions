from numpy import abs
def symmetric_point(p, q):
    # your code here
    
    [x_p, y_p] = p
    [x_q, y_q] = q
    
    deltax = abs((x_q - x_p))
    deltay = abs((y_q - y_p))
    
    if x_q > x_p:
        x_f = x_q + deltax
    else:
        x_f = x_q - deltax
        
    if y_q > y_p:
        y_f = y_q + deltay
    else:
        y_f = y_q - deltay
    
    return [x_f, y_f]