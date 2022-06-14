from PIL import Image
import numpy as np
N=25
with Image.open("corgi.jpeg") as im:

    pixels = [[[0 for k in range(3)] for n in range(N)] for o in range(N)]
    r,g,b=0,0,0

    l=im.width//N
    a=im.height//N

    for i in range(N):
        for j in range(N):
            for h in range(a):
                for w in range(l):
                    r = im.getpixel((j*l+w, i*a+h))[0]
                    g = im.getpixel((j * l + w, i * a + h))[1]
                    b = im.getpixel((j * l + w, i * a + h))[2]
                    pixels[i][j]=[r,g,b]

    b=np.array(pixels, dtype=np.uint8)
    print(b)
    Image.fromarray(b,mode='RGB').show()