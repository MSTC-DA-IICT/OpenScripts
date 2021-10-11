from PIL import Image, ImageDraw, ImageFont
import glob

# take the path of the folder
path = input("Enter the full path of folder which contains only images\n")

# Watermark text to disply on all images
watermark_txt = input("Enter the text to be written\n")

# watermark color in hex code
watermark_hex_color = input("Enter the hex code of color\n")

# for all image in given folder
for f in glob.iglob(path+"\*"):

    # open a image
    im = Image.open(f)
    width, height = im.size
    
    draw = ImageDraw.Draw(im)
    
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(watermark_txt, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width/2 - textwidth/2;
    y = height/2 - textheight/2;

    # draw watermark in the middle
    draw.text((x, y), watermark_txt, fill = watermark_hex_color, font=font)

    # Save watermarked image
    im.save(im.filename)

print("All images have been Boookmarked successfully\n\n")
