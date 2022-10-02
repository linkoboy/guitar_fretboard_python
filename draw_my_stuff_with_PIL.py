import os
from PIL import Image, ImageDraw, ImageFont

# font 
circle_font = ImageFont.truetype(os.getcwd() + '/fonts/consola.ttf', 30) 
circle_font_ascent, circle_font_descent = circle_font.getmetrics()
#print('a=' + str(circle_font_ascent)+ ' d=' + str(circle_font_descent))

grid_w_px = 100
grid_h_px = int(grid_w_px * (0.55))
circle_diam_px = grid_h_px * (0.35)

nb_fret = 22;
nb_strings = 6;
marge_w, marge_h = grid_w_px, grid_h_px
image_width = grid_w_px * nb_fret + (2*marge_w) 
image_height = grid_h_px * 6 + (2*marge_h)

image = Image.new("RGB", (image_width, image_height), "white")
draw = ImageDraw.Draw(image)

def draw_grid():
    line_w = 2
    rect_w = grid_w_px//8
    #horizontal lines
    for i in range(nb_strings):
        points = [(marge_w, marge_h + i * grid_h_px ), (marge_w + nb_fret * grid_w_px, marge_h + i * grid_h_px)]
        draw.line(points, width=line_w, fill="dimgrey", joint="curve")
    #vertical lines
    for i in range(nb_fret+1):
        points = [(marge_w + i * grid_w_px, marge_h), (marge_w + i * grid_w_px, marge_h + (nb_strings-1) * grid_h_px)]
        draw.line(points, width=line_w, fill="dimgrey", joint="curve")
    #left black rectangle
        draw.rectangle(((marge_w-rect_w, marge_h), (marge_w, marge_h + (nb_strings-1)*grid_h_px + (line_w+1)/2)), fill="dimgrey")
        
def test():
    global image
    draw.ellipse((100, 100, 150, 150), fill="lightgrey", outline='black', width=2)
    
    text = 'F#'
    bbox = draw.textbbox((125, 125), text, circle_font, align ="center") 
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    draw.text((125, 125 + circle_font_descent/3), text, 'red', font=circle_font, anchor="mm") 
    draw.point((125, 125), 'black')
    
    # export image to file
    export_filename = os.getcwd() + '/export/freatboard.png'
    export_filename_resampling = os.getcwd() + '/export/freatboard_resampling.png'
    image.save(export_filename)
    
    # resampling
    image = image.resize((image_width, image_height), resample=Image.Resampling.LANCZOS)
    image.save(export_filename_resampling)
    
    os.system('start '+ export_filename)

draw_grid()
test()

