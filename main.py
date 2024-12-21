import colorgram;
import turtle;
from tkinter import filedialog;
from tkinter import *;
import random;
import os;
from tkinterdnd2 import DND_FILES, TkinterDnD;
from tkinter import messagebox;
import mimetypes
from PIL import Image
import shutil;
import requests;
import datetime;

file_path = None;
image = None;
window = Tk();
window.config(padx=50,pady=50);
window.title("Color Extractor");


def download_image(url):

     destination_folder = "images"
     print(url);
     shutil.copy(url, destination_folder);


def check_mimetype():
    file_path = filedialog.askopenfilename()
    if file_path:
        mimetype, _ = mimetypes.guess_type(file_path)
        if mimetype in ("png", "jpeg", "jpg"):
            return True;
        else:
            return False;

def RunFileUploadWindow():

    def upload():
        global filepath,image;
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")]);
        image = PhotoImage(file=filepath);
        download_image(filepath);
        filename= os.path.basename(filepath);
        filepath = f"./images/{filename}";
        canvas.create_image(0,0,image=image);
 
    button = Button(text="Upload any image here!",command=upload);
    button.grid(row=0,column=1);
    
    canvas = Canvas(width=200,height=200);
    
    if image != None:
        canvas.create_image(0,0,image);
    
    submit = Button(text="Extract Colors",command=SubmitImage);
    submit.grid(row=3,column=1);
    
    canvas.grid(row=0,column=0)

    window.mainloop()


def ExtractColors(colors):
     
     extracted_colors = [];
     colors_=[list(x.rgb) for x in colors]
     
     for rgb in colors_:
        new_rgb = (rgb[0],rgb[1],rgb[2])
        extracted_colors.append(new_rgb);
     
     return extracted_colors;

def SubmitImage():
    global filepath, window;    
    
    if filepath == None:
        messagebox.showinfo("Result", "Invalid image type")
        return;
    try:    
        extracted_colors_data = colorgram.extract(filepath,3);
        PaintColors(extracted_colors_data);
    except:
        messagebox.showinfo("Result", "Invalid Extractions");
   
    window.quit()

def PaintColors(data):

    
    extracted_colors = ExtractColors(data);
    
    height = 500;
    width = 500;
    incr_x = 25;
    incr_y = 25;

    painter = turtle.Turtle();
    isDrawing = True;
    turtle_screen = turtle.Screen();

    turtle_screen.screensize(height,width,bg="black");
   
    turtle.colormode(255);
   
    painter.hideturtle();
    painter.penup()
    painter.shape("circle");
    painter.shapesize(1);
    painter.setx(-width / 2)
    painter.sety(height / 2)

    while isDrawing:
        random_color = random.choice(extracted_colors);
        
        painter.color = random_color;
        print(extracted_colors);
    
        painter.dot(20,random_color);
    
        painter.forward(incr_x);
    
        if(painter.xcor() >= width / 2):
            painter.setx(-width / 2);
            painter.sety(painter.ycor() - incr_y);
        
        if(painter.ycor() <= -height / 2):
            isDrawing = False;


RunFileUploadWindow();