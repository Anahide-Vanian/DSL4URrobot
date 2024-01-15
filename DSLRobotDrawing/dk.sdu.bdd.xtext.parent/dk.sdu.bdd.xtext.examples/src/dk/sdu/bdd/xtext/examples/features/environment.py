from msilib.schema import Feature
from pyexpat import features
from behave import fixture
import json
from behave.model import Scenario
import turtle
import time


f = open("Environment.json")
data = json.load(f)
        
def before_all(context):
    print("Let's start to play...")
    
    context.bob = turtle.Turtle()
    context.robot_name = get_robot_name()#robot name set by the user
    
    #properties for the screen
    context.arena = turtle.Screen()
    context.arena.title('DSL demo for robot drawing')
    context.arena.bgcolor("orange")
    
    context.font1 = ("Arial", 14, "bold")
    context.font2 = ("Arial", 9, "normal")
    
    
    #properties for the turtle
    # Set the pen size
    context.bob.pensize(3) 
    context.robot_home_pos = [0,0]
    
    #Location of the text to provide information to the user
    context.text4userPos = [0,70] 


def before_feature(context, feature): 
    pass

def after_feature(context, feature):
    pass

def before_scenario(context, scenario): 
    time.sleep(2)
    #pass

def after_scenario(context, scenario):
    pass
    

# Get speed based naming (if not set, returns moderately)
def get_speed(identifier = "moderate"):
    speed = data["Speeds"][identifier]
    return speed


# Get name of robot based on configured name
def get_robot_name():
    name = data["Robot"]["name"]
    return name

# Get coordinate-location based on configured name
def get_position(name):
    locations = data["Positions"]
    coordinate = locations[name]

    return coordinate

def writeText4user(context, text, text_pos):
    
    #save actual pen color because I want the center text to be black
    actual_pen_color = context.bob.pencolor()
    context.bob.pencolor("black")
        
    
    #save actual properties
    actual_speed = context.bob.speed()
    actual_pos = context.bob.pos()
    
    #Go to write the text somewhere else in the screen 
    context.bob.penup()
    context.bob.hideturtle()
    context.bob.speed("normal")
    context.bob.goto(text_pos[0], text_pos[1])
    context.bob.write(text, align="center", font=context.font1)
    time.sleep(4)
    # Erase the last text
    context.bob.undo()
    
    #Reset the robot saved properties to let it continue it's drawing 
    context.bob.penup()
    context.bob.goto(actual_pos)
    context.bob.speed(actual_speed)
    context.bob.showturtle()
    context.bob.pencolor(actual_pen_color)#reset previous pen color
    context.bob.pendown()
   
    
    
def move(context, location, speed_term):
    
    speed_val = get_speed(speed_term)
    square_size = data["Robot"]["step_size"] *10
    
    if(location == "upper right"):
        context.bob.pencolor("red")
    elif(location == "lower right"):
        context.bob.pencolor("green")
    elif(location == "upper left"):
        context.bob.pencolor("blue")
    elif(location == "lower left"):
         context.bob.pencolor("black")
        
        
    #Move to draw a side of the  square
    context.bob.forward(square_size) # Forward robot by square_size
    context.bob.speed(speed_val)#set the robot speed
    context.bob.write(location, font=context.font2)# Forward robot by square_size
    context.bob.left(-90) # Turn robot by 90 degree
    