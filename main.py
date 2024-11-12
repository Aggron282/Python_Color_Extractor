import colorgram;
import turtle;
colors = colorgram.extract('image.jpeg',3);
import random;

extracted_colors = [];

for color in colors:
    #Each color comes out in a object with rgb property
    # the rgb property is seperated into r , g , b each of these property holds the respective hues for red,green,blue
    rgb = color.rgb
    new_rgb = (rgb.r,rgb.g,rgb.b)
    extracted_colors.append(new_rgb);


print(extracted_colors);
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
   
    painter.dot(20,random_color);
   
    painter.forward(incr_x);
   
    if(painter.xcor() >= width / 2):
        painter.setx(-width / 2);
        painter.sety(painter.ycor() - incr_y);
    if(painter.ycor() <= -height / 2):
        isDrawing = False;

