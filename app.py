from PIL import Image,ImageColor

(width, height)=(1080,1920)

with open("colors.txt",'r') as colors:
    for color in colors.readlines():
        img = Image.new('RGB', (width, height),ImageColor.getrgb(color))
        img.save(f'Templates/template-{color}.png')

