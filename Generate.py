from PIL import Image,ImageColor
import os

(width, height)=(1080,1920)
def generate():
    with open("colors.txt",'r') as colors:
        for i,color in enumerate(colors.readlines()):
            print(f'Generating {i} - {color}')
            try:
                with Image.new('RGB', (width, height),ImageColor.getrgb(color)) as img:
                    img.save(f'Templates/template-{color}.png')
            except Exception as e:
                print(f'Error in Generating Picture for color : {color}')

if __name__=="__main__":
    if not os.path.exists("Templates"):
        os.mkdir("Templates")
    if not os.path.exists("colors.txt"):
        print("Please Hex Codes in colors.txt file and save it in this folder")
    else:
        generate()