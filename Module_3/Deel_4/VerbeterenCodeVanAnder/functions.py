from time import sleep
from colorama import Fore
import os
from Data import *


def clear():
    os.system('cls')
    return


def dead():
    print("***you died***")
    global lives
    lives -= 1
    if lives <= 0:
        "Game Over :("
        sleep(10)
        start()
    else:
        print(f"{lives} lives remaining, respawning")
        sleep(5)
        clear()
        arrival_at_dungeon()


def start():
    clear()
    print(startscherm)

    name_input=(input("What's your name: "))
    print(f"hello {name_input} Welcome to dungeon quest.")
    begin = (input("Press enter to begin"))
    if begin == "":
        print('Loading...')
        sleep(1)
        print("Downloading data...")
        sleep (2)
    else:
        print ('Nevermind 🖕🏻')
        exit()
    clear()
    story()      
    return

def story():
    story = input("Would you like to start with the story. Yes/No ")
    if story == "yes":
        sleep(1)
        print("The story begins I hope you're ready.")
        sleep(1)
        print(storytext)
        print("You wake up *UGH* another day.")
        input("Press enter to continue.")
    elif story == "no":
        print ("Okay then lets start.")
        sleep (5) 
        print("You wake up.")
    clear()
    choice()
    return

def choice():
    print("You stand up and walk down the hall what do you do? \n(A) You go downstairs. \n(B) You go to the bathroom to shower.")
    choice = input (">> ")
    if choice in ["A" , "a"]:
        clear()
        breakfast()
    elif choice in ["B" , "b"]:
        clear()
        bathroom()

    return

def breakfast():
    print ("You go downstairs what do you do? \n(A) Eat breakfast. \n(B) You grab yourself a drink.")
    downstairs = input (">> ")
    if downstairs in ["A" , "a"]:
        print("You make yourself a sandwich.")
        clear()
        going_on_a_adventure()
    elif downstairs in ["B" , "b"]:
        print("You grab yourself a drink.")
        clear()
        going_on_a_adventure()
    return

def going_on_a_adventure():
    print ("You ate your breakfast and you are ready to go on your adventure, but do you check your inventory before you go? \n(A) Yes, check your inventory. \n(B) No, go without checking.") 
    inventory = input (">> ")
    if inventory in["A" , "a"]:
        print("**inventory**", "Sword" , "Shield" , "Candle")
        heading_out()
    elif inventory in["B" , "b"]:
        print("I have to check my inventory before I go.")
        going_on_a_adventure()
        clear()

    return   
        
def bathroom():
    print ("Went to the bathroom what are you going to do? \n(A) Shower. \n(B) Brush your teeth.")
    bathroom = input(">> ")
    if bathroom in["A", "a"]:
        print("You showered and went downstairs.")
        breakfast()
    elif bathroom in ["B","b"]:
        print("You brushed your teeth and went downstairs.")
        clear()
        breakfast()
    return
        
def heading_out():
    print("Your gonna head to the dungeon but which route do you take? \n(A) Through the village. \n(B) Through the woods.")
    heading_out = input(">> ")
    if heading_out in["A","a"]:
        print("You go trough the village.")
        sleep(0.5)
        clear()
        arrival_at_dungeon()
    elif heading_out in["B","b"]:
        print("You go trough the woods.")
        clear()
        arrival_at_dungeon()
    return
    
def arrival_at_dungeon():
    print ("You arrived at the dungeon do you go inside? \n(A) Yes, I go inside. \n(B) No, I'm not ready yet.")
    entering_the_dungeon = input(">> ")
    if entering_the_dungeon in ["A","a"]:
        print("It's pretty dark in here do you wanna equip your candle? \n(A) Yes.  \n(B) No.")
        equip_candle = input(">> ")
        if equip_candle in ["A","a"]:
            print ("*Equiped Candle.*")
            clear()
            first_chambers()
        elif equip_candle in ["B","b"]:
            print("You are killed by a unknown entity.")
            clear() 
            dead()
            
    elif entering_the_dungeon in ["B" , "b"]:
        print("Wrong choice returning to start.")
        sleep(1)
        clear()
        start()
    return

def first_chambers():
    print("You reach the first chamber in the dungeon and you find 2 hallways each hallway has a sign which says: left chamber the haunted prisons , right chamber the suspicious library which do you go first choose wisely \n(A) chamber on the left side of you. \n(B) chamber on the right side of you.")
    chamber = input(">> ")
    if chamber in ["A" , "a"]:
        print("You decide to go in the hallway to your left you look around and find multiple prison cells and you find a key do you pick it up \n(A) yes. \n(B) no. ")
        key= input(">> ")
        if key in["A","a"]:
            print ("You picked up the key and saw a little tag on it do you read the text on the tag \n(A) yes. \n(B) no.")
            text_on_tag= input(">> ")
            if text_on_tag in ["A", "a"]:
                print ("the tag says 12b it looks like the key of a cell i should look for the correct cell")
                print("finaly i found the correct celldoor now do i open the key or wait \n(A) open the door \n(B) wait" )
                open_cell_door = input(">> ")
                if open_cell_door in ["A" , "a"]:
                    print ("you opened the door and found another key you wonder what it is for")
                    print("i should head back to the main chamber")
                    global chestkey
                    chestkey = True
                    sleep(2)
                print("Im finaly back.")
                clear()
                first_chambers()
            elif open_cell_door in ["B" , "b"]:
                print("I should wait a little and come back here later.")
                print("I should head back to the main chamber.")
                sleep(2)
                print("Im finaly back.")
                clear()
                first_chambers()
            elif text_on_tag in ["B" , "b"]:
                print ("I wonder what it says but i will come back to it later.")
        elif key in["B" , "b"]:
            print("You did not pick up the key and keep wandering trough the prison.")
            print ("You decided to go back to the main chamber.")
    elif chamber in ["B" , "b"]:
        clear()
        second_chamber()
            
            
def second_chamber():
    print("You decide to take the right halway to the suspicious library you enter the chamber and see a lot of ancient books and bookshelves you also hear some strange sounds behind a closed door do you check it out? \n(A) yes. \n(B) no im good. ")
    strange_sound= input(">> ")
    if strange_sound in ["A" , "a"]:
        print ("You force open the closed door and find out that there's a big monster type of fugure sleeping in the corner what do you do \n(A)  investigate the area around the sleeping monster with the chance of waking him up. \n(B) walk away." ) 
        investegate = input(">> ")
        if investegate in["A" , "a"]:
            print("You deside to go investegate but you trip and wake up the monster.")
            clear()
            dead()
        elif investegate in["B","b"]:
            print ("You decide to walk away and wander trough the rest of the library you find a chest but its locked what do you do now \n(A) try to lockpick it. \n(B) look for the key.")
            chest = input(">> ")
            if chest in ["A" , "a"]:
                print("You tried to lockpick the chest but it failed you have to look for the key.")
                second_chamber()
            elif chest in ["B","b"]:
                global chestkey
                if chestkey != False:
                    print("You opened the chest and found another key.")
                    clear()
                    third_chamber()
                    global doorKey
                    doorKey = True
                else:
                    print("You don't have a key.")
                    print("I should return to the other chamber and look for the key.")
                    print("Returning to chamber one...")
                    sleep(3)
                    clear()
                    first_chambers()                   
    elif strange_sound in ["B" , "b"]:
        print("You walk away from the door and deside to walk further until you find a locked chest what do you do \n(A) try to lockpick it. \n(B) look for the key.")
        chest = input(">> ")
        if chest in ["A" , "a"]:
                print("You tried to lockpick the chest but it failed you have to look for the key.")
        elif chest in ["B" , "b"]:
            if chestkey == True:
                print("You opened the chest and found another key.")
                print ("Do i wanna look further into the room \n (A)yes. \n (B)no.")
                continue_ = input("")
                if continue_ in ["A" , "a"]:
                    clear()
                    third_chamber()
                elif continue_ in ["B" , "b"]:  
                    clear()
                    #global doorKey
                    #doorKey = True
            else:
                print ("You dont have a key!")
                print("I should return and look for the key or continue looking in this room what do you do \n(A) continue back to the main hall to look for the key. \n(B) you go to look further in the room.")
                return_or_continue = input(">> ")
                if return_or_continue in ["A" , "a"]:
                    print ("You decide to go back to the main room.")
                    clear()
                    first_chambers()     
                elif return_or_continue in ["B" , "b"]:
                    clear()
                    third_chamber() 
        return
     
    
def third_chamber(): 
    print ("You see another closed door in the back of the prison what do you do \n(A) check it out. \n(B) dont check it." )
    closed_door = input(">> ")
    if closed_door in ["A" , "a"]:
        print("You decide to open the door and find a ancient lunchroom that looks like it has been abandond for a very long time you hear some weird type of growling noice behind a door what do you do \n(A)check it out \n(B)you dont and keep serching." )
        weird_noice = input(">> ")
        if weird_noice in ["A" , "a"]:
            print ("You go check it out but find a big growling wolf monster which kills you instantly.")
            clear()
            dead()
            third_chamber()
            
        elif weird_noice in ["B" ,"b"]:
            print("You did not look closer and decided to walk away and look further until you stepped on a stone like pressure plate that generates a clicking sound two hidden doors open which one do you choose? \n(A) left. \n(B) right. \n(C) keep looking.")
            hidden_door = input(">> ")
            if hidden_door in ["A" , "a"]: 
                print("You wander into the left room that has a 2 big monsters inside of it you tried to sneak out of the room but you trip and fall which wakes up the monsters but you bearly got to escape you will need to check the other chambers (B) left chamber. (C) keep looking for other secrets.")
                escaped = input(">> ")
                if escaped in ["B" ," b "]:
                    print("You wander into the right room thats filled with traps you try to back off but the door closes and you are traped there's no way out.")
                    clear()
                    dead()
                    third_chamber()
                    
                elif escaped in ["C","c"]:
                    fourth_and_final_chamber()
                    
            elif hidden_door in ["B" ,"b"]:
                print("You wander into the right room thats filled with traps you try to back off but the door closes and you are traped there's no way out.")
                dead()                
            elif hidden_door in ["C" , "c"]:
                fourth_and_final_chamber()
    elif closed_door in ["B" , "b"]:
        print ("You did not go trough the closed door and decide to go back to the first chamber.")
        clear()
        first_chambers()
    return
    
def fourth_and_final_chamber():
    print("you look around the room and see that another door opend behind you do you decide to check it out (A)check it out (B) dont check it out.")
    the_final_room = input(">> ")
    if the_final_room in["A" , "a"]:
        print("you decide to check it out and at first it didnt look like much until you looked a little closer and you find out that its a room filled with gold, diamonds, gems and a lot of other kind of tressure you only have limited time tho you you have to decide what to take so what do you do \n(A)Take gold and some gems. \n(B)Take a few diamonds and 2 other tressures.")
        tressure = input(">> ")
        if tressure in ["A" , "a"]:
            print("You took to much gold wich weighted you down as the tressure room started to collaps you didn't have enough time to escape.")
            sleep(5)
            clear()
            dead()
            fourth_and_final_chamber()
        elif tressure in ["B" ,"b"]: 
            print("You grabbed some middle sized diamonds and some gold goblets then you notice that the tressure chamber started to collaps so you made a run for it and barely made it out alive.")
            sleep(5)
            clear()
            the_Escape()
    return          
            
def the_Escape():
    print("After you barely made it out of the tressure room you decide to try and head to the exit so you started on your way back but you heard footsteps you looked behind you and noticed the wolf from earlier broke free out of the lunchroom and started running after you what do you do (A) hide (B)make a run for it.")
    hide_or_run = input(">> ")
    if hide_or_run in ["A" , "a"]:
        print("you hide and you succefully lose the big wolf you decide to check once more before you continue on your way out the coast was clear so you decide to continue on the find to the exit which you reach a copple of minutes later")
        print("you succefully reach the exit and your free from the dungeon what do you do now (A) head home (B)head into the city")
        escaped = input(">> ") 
        if escaped in ["A" , "a"]:
            print("you head home and take a well deserved rest.") 
            sleep(5)
            clear()
            the_end()
        elif escaped in ["B" , "b"]:
            print("You head into the city to sell some of your tressure and decide to grab a cold pint of beer. After that you head home and get a well deserved rest")
            sleep(5)
            clear()
            the_end()
    if hide_or_run in ["B" , "b "]:
        print ("The wolf caught up to you and he ripped you appart.")
        dead()
        the_Escape()
        return
    
def the_end():
        print(end)