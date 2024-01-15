from msilib.schema import Feature
from behave import when, given, then
import time
import environment as env #modif
import os

#File created by the developer and utilizing methods form the ur_rtde library imported using "env"

@when('the position {prep} the robot "{identifier}" is "{position}"')
@then('the position {prep} the robot "{identifier}" is "{position}"')
@given('the position {prep} the robot "{identifier}" is "{position}"')
def step_given(context, identifier : str, position, prep):
     
    text =  context.robot_name + " is now at " + position + ".\n" +" Which means : " + str(context.bob.pos())
    env.writeText4user(context, text, context.text4userPos)

@when('the robot "{identifier}" moves to position "{position}" with "{speed}" speed')
@given('the robot "{identifier}" moves to position "{position}" with "{speed}" speed')
def step_when(context, identifier : str, position, speed : str):
    env.move(context, position, speed)


@then('the beautifulFigure "{identifier}" is {state}')
@given('the beautifulFigure "{identifier}" is {state}')
def step_impl(context, identifier:str, state):
    
    if(state == "DONE"):
        env.writeText4user(context, "What a beautiful square !", context.text4userPos)
        
    elif(state == "ALMOST DONE"):
        env.writeText4user(context, "We are half way to have our complete square !", context.text4userPos)
        
    elif(state == "NOT DONE"):
        position = str(context.bob.pos())
        env.writeText4user(context, "Let's draw a square with " + context.robot_name + " !\n"
                           + "He is actually located at : " + position, context.text4userPos)
    



