from  colorgram import *

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r=rgb_colors.r
    g=rgb_colors.g
    b=rgb_colors.b
    new_color =(r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)