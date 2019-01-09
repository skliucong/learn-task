from PIL import Image
im = Image.open("westbrook.jpg")
pix = im.load()
width = im.size[0]
height = im.size[1]

ims = Image.new("RGB",(width,height))

for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        ims.putpixel((x, y), (int(r/2), int(g/2), int(b/2)) )


ims.save('Q2.jpg')