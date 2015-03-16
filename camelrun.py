#A simple Camel run style game
import random

#functions for the game

def newgame():
    """function to set up newgame with global vars"""
    global drinks,dist_to_trav,on_run,nat_dist,camel_tiredness,miles_traveled,thirst
    thirst=0
    miles_traveled=0
    nat_dist=-20
    camel_tiredness=0
    drinks=3
    dist_to_trav=200
    on_run=True
    print "Welcome to Camel!"
    print "You have stolen a camel to make your way across the great Mobi desert."
    print "The natives want their camel back and are chasing you down! Survive your"
    print "desert trek and out run the natives."  
def display_menu():
    print 'A. Drink from your canteen.'
    print 'B. Ahead moderate speed.'
    print 'C. Ahead full speed.'
    print 'D. Stop for the night.'
    print 'E. Status check.'
    print 'Q. Quit'
def get_user_input():
    global user_choice
    display_menu()
    user_choice=raw_input('Your choice: ')
def processinput():
    global on_run
    uchoice=user_choice.upper()
    try:
        if uchoice == "Q":
            on_run=False
        elif uchoice == 'A':
            drink()            
        elif uchoice == 'B':
            print ''
            moderate_rate()
            print ''
        elif uchoice == 'C':
            print ''
            full_rate()
            print ''
        elif uchoice == 'D':
            print ''
            night_stop()
            print ''
        elif uchoice == 'E':
            print ''
            status()
            print ''
        else:
            print "Not a valid input"
    except:
        print 'Not a valid input'
def status():
    print ''
    print "Miles traveled: ",miles_traveled
    print "Drinks left in canteen",drinks
    print "The Natives are",nat_dist*-1,"miles behind"
    print ''  
def night_stop():
    global camel_tiredness,nat_dist
    camel_tiredness=0
    nat_dist=random.randrange(7,15)+nat_dist
    print 'The camel is happy'    
def full_rate():
    global thirst,miles_traveled,nat_dist,camel_tiredness
    thirst=thirst+1
    miles=random.randrange(10,21)
    miles_traveled=miles+miles_traveled
    nat_dist=(random.randrange(7,14)-miles)+nat_dist
    camel_tiredness=camel_tiredness+random.randrange(1,4)
    print ''
    print 'Miles traveled this run:',miles
    print ''
    status()    
def drink():
    global drinks,thirst
    if drinks > 0:
        drinks=drinks-1
        thirst=0
    else:
        print 'Your canteen is empty!!!'        
def moderate_rate():
    global thirst,miles_traveled,nat_dist,camel_tiredness
    thirst=thirst+1
    miles=random.randrange(5,13)
    miles_traveled=miles+miles_traveled
    nat_dist=(random.randrange(7,14)-miles)+nat_dist
    camel_tiredness=camel_tiredness+random.randrange(0,2)
    print ''
    print 'Miles traveled this run:',miles
    status()
def game_logic_loop():
    global on_run,thirst,drinks,camel_tiredness
    if thirst >=4 and thirst < 6:
        print 'You are thirsty'
    elif thirst >=6:
        print 'You died of thirst'
        on_run=False
    if camel_tiredness > 5 and camel_tiredness < 8:
        print 'The camel is getting tired'
    elif camel_tiredness >=8:
        print 'Your camel is dead!!!'
        on_run=False
    if nat_dist*-1 <= 15 and nat_dist*-1 >0:
        print 'The natives are getting close!'
    elif nat_dist*-1 <=0:
        print 'The natives have caught and beheaded you'
        on_run=False
    if miles_traveled >=200:
        print 'You have escaped with your life intact'
        print "Good job! I bet you couldn't do it again"
        on_run=False
    if random.randrange(0,21) == 20: #one in 20 chance of finding an oasis
        print 'An oasis is found'
        print 'You refill your canteen, rest and drink'
        drinks=3
        thirst=0
        camel_tiredness=0
        
#start a newgame
newgame()

#main game loop
while on_run:
    get_user_input()
    processinput()
    game_logic_loop()
    

quit()
