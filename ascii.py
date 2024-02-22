from PIL import Image, ImageOps
size = (240, 240)

def brightness(pixel_matrix):
    w = len(pixel_matrix)
    l = len(pixel_matrix[0])
    ans = []
    for x in range(w):
        a = [] 
        for y in range(l):
            avg = (pixel_matrix[x][y][0] + pixel_matrix[x][y][1] + pixel_matrix[x][y][2])/3
            a.append(avg)
        ans.append(a)
    return ans 
def interpolate_brightness(x,characters): 
    # 0 - 255 into 0 to 64 is linear interpolation
    # y = (x-xmin) * (ymax - ymin)/(xmax - xmin) + ymin
    # xmin = 0, ymin = 0 so 
    # y = x*ymax/xmax
    ymax = len(characters) - 1
    xmax = 255 
    y = x * ymax // xmax 
    return int(y) 

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

 
im = Image.open('LineSara.png')
im2 = ImageOps.contain(im, size)
im2 = im2.rotate(90)
im2.show()
W, L = im2.width, im2.height
arr = []
pixels = im2.load()
for x in range(W):
    a = []
    for y in range(L):
        cpixel = pixels[x, y]
        a.append(cpixel)
    arr.append(a)
bright = brightness(arr)

ascii_chars = ""
for x in range(W):
    char = ''
    for y in range(L):
        ind = interpolate_brightness(bright[x][y], characters)
        char += characters[ind]*3
    ascii_chars += char + '\n'

print(ascii_chars)