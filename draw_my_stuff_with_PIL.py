import os
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('arial.ttf', 20) 

def line():
    width = 400
    height = 400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    points = [(100, 100), (150, 200), (200, 50), (250, 250)]
    
    draw.line(points, width=5, fill="green", joint="curve")
    draw.ellipse((100, 100, 150, 150), fill="white", outline='black', width=2)
    #draw.point((125, 125), 'red')
    text = 'F#'
    w, h = draw.textsize(text) 
    draw.text(((125-w),(125-h)), text, 'red', font = font, align ="left") 
    
    # export image to file
    export_filename = os.getcwd() + '/export.png'
    export_filename_x4 = os.getcwd() + '/export_resampling_x4.png'
    image.save(export_filename)
    
    # resampling
    image = image.resize((width * 4, height * 4), resample=Image.BICUBIC)
    image.save(export_filename_x4)
    
    os.system('start '+ export_filename)

line()

