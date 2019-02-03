from PIL import Image
im = Image.open('img1.jpg')

black = 0
other_color = 0

for pixel in im.getdata():
    if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        black += 1
    else:
        other_color += 1
print('black=' + str(black)+', red='+str(other_color))
covered_proc = 100*(other_color/(other_color+black))
print(covered_proc)