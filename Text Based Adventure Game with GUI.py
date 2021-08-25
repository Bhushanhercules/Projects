from tkinter import *
from random import randint
root = Tk()
root.title("Text Based Adventure Game")
root.geometry('600x600')

global health 
health = 10

def start():
    try:
        name_label = Label(root, text="Enter your Name")
        name_label.pack()
        global name
        name = Entry(root)# Creates a input entry box
        name.pack()
        name_submit_button = Button(root, text="Submit", bg="Blue", fg="White", command=age_function)
        name_submit_button.pack()
        
    except NameError:
        error_name= Label(root, text="Please enter your age to continue")
    
def age_function():
    name_label = Label(root, text="Hi, " +name.get()+ " What's your age?")
    name_label.pack()
    global age
    age = Entry(root)
    age.pack()
    age_submit_button = Button(root, text="Submit", bg="Blue", fg="White", command=game_start_0_function)
    age_submit_button.pack()
        
def game_start_0_function():
    age_integer = int(age.get())
    try:
        if age_integer >= 18:
            welcome_label = Label(root, text="As You are,"+age.get()+"You're eligible to play the game")
            welcome_label.pack()
            play_game_button = Button(root, text="Play", bg="Dark orange", fg="White", command=game_start_1_function)
            play_game_button.pack()
                            
        else:
            cant_play_label = Label(root, text="Sorry you have to wait till you turn 18")
            cant_play_label.pack()

    except ValueError:
        error_value= Label(root, text="Please enter your age to continue")

def game_start_1_function():
    game_line_1 = Label(root, text="Road is dividing into left and right")
    game_line_1.pack()
    game_line_2 = Label(root, text="Which path you will chose?")
    game_line_2.pack()
    game_line_3 = Button(root, text="left", bg="Sky blue", command=game_start_2_function)
    game_line_3.pack()
    game_line_4 = Button(root, text="right", bg="Sky blue", command=game_start_7_function)
    game_line_4.pack()




def game_start_2_function():

    game_line_1 = Label(root, text="Now there is a house and a strange pond , So what will you chose? house or pond")
    game_line_1.pack()
    game_line_2= Button(root, text="House", bg="Purple", fg="White", command=game_start_3_function)
    game_line_2.pack()
    game_line_3= Button(root, text="Pond", bg="Purple", fg="White", command=game_start_4_function)
    game_line_3.pack()
    


def game_start_3_function():
    game_line_1 = Label(root, text="you had a fight with them and you lose your health. click health to find out your new health")
    game_line_1.pack()
    global new_health
    new_health = health - 5
    game_line_2= Button(root, text="Find out Health", bg="Light green", fg="White", command=game_start_5_function)
    game_line_2.pack()

def game_start_4_function():
    game_line_1 = Label(root, text="you have a happy life now. you live by fishing Write thankyou to me for saving you")
    game_line_1.pack()
    game_line_2= Button(root, text="Thank You", bg="Red", command=game_start_6_function)
    game_line_2.pack()


def game_start_5_function():
    find_out_health_label = Label(root, text=new_health)
    find_out_health_label.pack()

def game_start_6_function():
    thnx_label_1 = Label(root, text="Your Welcome")
    thnx_label_1.pack()

def game_start_7_function():
    game_line_1 = Label(root, text="You encounter a Monster near a cave, would you like to Run or Attack")
    game_line_1.pack()
    game_line_2=Button(root, text="Run",bg="Purple", fg="White", command=game_start_8_fuction)
    game_line_2.pack()
    game_line_3=Button(root, text="Attack",bg="Purple", fg="White", command=game_start_9_function)
    game_line_3.pack()

def game_start_8_fuction():
    game_line_1= Label(root, text="You run but the monster grabed you from behind and you lost your life")
    game_line_1.pack()
    game_line_2= Label(root, text="Better Luck Next Time!")
    game_line_2.pack()

def game_start_9_function():
    game_line_1= Label(root, text="You found two weapons nearby a Flamethrower or a Sword, which one would you choose?")
    game_line_1.pack()
    game_line_2= Button(root, text="Flamethrower",bg="Purple", fg="White", command=game_start_10_function)
    game_line_2.pack()
    game_line_3= Button(root, text="Sword",bg="Purple", fg="White", command=game_start_11_function)
    game_line_3.pack()

def game_start_10_function():
    game_line_1= Label(root, text="You burned that monster with flamethrower")
    game_line_1.pack()
    game_line_2= Label(root, text="As you entered in the cave you found treasure in it")
    game_line_2.pack()
    game_line_3= Label(root, text="And you lived a happy life,Write thankyou to me for saving you")
    game_line_3.pack()
    game_line_4= Button(root, text="Thank You", bg="Red", command=game_start_6_function)
    game_line_4.pack()

def game_start_11_function():
    game_line_1= Label(root, text="You barely survived with that Sword and somehow you managed to escaped")
    game_line_1.pack()
    game_line_2= Label(root, text="Write health to find out your new health")
    game_line_2.pack()
    global newhealth
    newhealth = health - 7
    game_line_3= Button(root, text="Find out Health", bg="Light green", fg="White", command=game_start_12_function)
    game_line_3.pack()

def game_start_12_function():
    find_out_health_label = Label(root, text=newhealth)
    find_out_health_label.pack()
    

start()


root.mainloop()
