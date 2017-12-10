from PIL import Image, ImageFilter, ImageOps

with open('00-infi-img.txt') as f:
    data = [l.strip().split(' ') for l in f.readlines()]

data = [(int(x), int(y)) for x, y in data]

PADDING = 10 # Just to make it look nice

width = max(x for x, y in data) + 1 + PADDING*2
height = max(y for x, y in data) + 1 + PADDING*2

im = Image.new('RGB', (width, height), "#fff")
for x, y in data:
    pos = (x+PADDING, y+PADDING)
    im.putpixel(pos, 0)

# Try to make the text more readable/pretty
im = im.resize((width*8, height*8), Image.LANCZOS)
im = im.filter(ImageFilter.GaussianBlur(radius=3))
im = ImageOps.posterize(im, 1)
im = ImageOps.equalize(im)
im = im.filter(ImageFilter.SMOOTH_MORE)

im.save('00-infi-img.png')

