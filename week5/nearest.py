from math import sqrt, hypot

x1 = 329
y1 = 158

x2 = 531
y2 = 408

print(sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))

print(hypot(x2 - x1, y2 - y1))

data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'], [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'], [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'], [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'], [117, 546, 'Y'], [507, 127, 'Z']]

#for arbitrary value e.g. "J" find the nearest N items e.g. 5

def get_top(data,letter,top_n):
    output = []
    # ...
    return output

top = get_top(data,"J",5)
print(top)