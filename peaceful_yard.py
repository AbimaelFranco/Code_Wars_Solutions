# from math import sqrt
# def peaceful_yard(yard, min_distance):
#     Lou = [0, 0]
#     Mustache = [0, 0]
#     Raoul = [0, 0]
#     y = 0
#     cats = []
#     L = 0
#     M = 0
#     R = 0
#     DLM = 100
#     DLR = 100
#     DRM = 100
    
#     for i in range(len(yard)):
#         for j in yard[i]:
#             y +=1
#             if j == 'L':
#                 Lou = [i, y-1]
#                 cats.append('L')
#                 L = 1
#             elif j == 'M':
#                 Mustache = [i, y-1]
#                 cats.append('M')
#                 M = 1
#             elif j == 'R':
#                 Raoul = [i, y-1]
#                 cats.append('R')
#                 R = 1
#         y = 0
    
#     if len(cats) <= 1:
#         return True
#     else:
#         if L and M:
#             DLM = sqrt((Lou[0]-Mustache[0])**2 + (Lou[1]-Mustache[1])**2)
#         if L and R:
#             DLR = sqrt((Lou[0]-Raoul[0])**2 + (Lou[1]-Raoul[1])**2)
#         if R and M:
#             DRM = sqrt((Raoul[0]-Mustache[0])**2 + (Raoul[1]-Mustache[1])**2)
        
        
#         if DLM < min_distance or DLR < min_distance or DRM < min_distance:
#             print(DLM)
#             print(DLR)
#             print(DRM)
#             return False
#         else:
#             return True
            
from math import sqrt

def peaceful_yard(yard, min_distance):
    positions = {}
    
    for i, row in enumerate(yard):
        for j, cell in enumerate(row):
            if cell in {'L', 'M', 'R'}:
                positions[cell] = (i, j)
    
    cats = list(positions.keys())
    
    if len(cats) <= 1:
        return True
    
    # Calculamos distancias entre pares de gatos
    def distance(cat1, cat2):
        x1, y1 = positions[cat1]
        x2, y2 = positions[cat2]
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    pairs = [('L', 'M'), ('L', 'R'), ('M', 'R')]
    
    for cat1, cat2 in pairs:
        if cat1 in positions and cat2 in positions:
            if distance(cat1, cat2) < min_distance:
                return False
    
    return True
