import time
import os
from random import randrange
from pynput import keyboard


player_name = ""
number_displayed = 0 # number displayed on screen
accepting_input = False
did_print_result = False
game_over = False # is True when arrows are 0 or kingkong is dead
didHit = False
didMiss = False


class Bowman:
    arrows = 3

    def __init__(self):
        global player_name

        player_name = input("Enter your name: ")


class Monster:
    is_dead = False
    hitpoints = 150

    def __init__(self):
        self.name = "King Kong"


def endGame():
    global game_over, accepting_input
    
    if Bowman.arrows <= 0 or Monster.hitpoints <= 0:
        game_over = True
        accepting_input = False
        outro()
        return True
    return False


def greetPlayer():
    global player_name

    print(f'Welcome {player_name}')
    time.sleep(1)
    print("You are a Bowman facing KingKong")
    time.sleep(1)
    print("You only have 3 arrows, Aim Well!!")
    print("Hit spacebar when you see the number 2")
    time.sleep(2)
    os.system("clear")


def outro():
    if Monster.hitpoints == 0:
        print("Congratulations, King Kong is dead!")
    else:
        print("You ran out of arrows")


def print_result(result):
  global did_print_result

  if did_print_result == False:
    did_print_result = True
    print(f'\n{result}')


def startGame(): 
    global number_displayed, accepting_input, did_print_result, game_over, didHit, didMiss

    player1 = Bowman()
    monster = Monster()
    greetPlayer()
    while game_over == False: # timer stops when game_over == True
        if endGame():
            break
        number_displayed = randrange(1, 4)
        os.system("clear")  
        accepting_input = True
        did_print_result = False 
        if didHit:
            Bowman.arrows -= 1
            Monster.hitpoints -= 50
            didHit = False
        if didMiss:
            Bowman.arrows -= 1
            didMiss = False
        print(f'Arrows: {Bowman.arrows}\nMonster Hitpoints: {Monster.hitpoints}\nNumber: {number_displayed}')
        time.sleep(1)
        accepting_input = False
        time.sleep(0.5)



def on_press(key):
    global number_displayed, accepting_input, didHit, didMiss
    while accepting_input:
        if key == keyboard.Key.space:
            if number_displayed == 2:
                print_result("Hit!")
                didHit = True
            else:
                didMiss = True
                print_result("Miss!")
                

listener = keyboard.Listener(on_press=on_press)
listener.start()
startGame()