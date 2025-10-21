import colorgram
colors = colorgram.extract('image1.jpg', 30)
rgb_colors = []
print(colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
