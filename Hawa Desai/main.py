
#
import time
import os
from sys import platform

'''
Game Jam 1: Basics of Python

- Name: Hawa Desai
- 25 September 2022
- Theme: Kettle

WELCOME TO KETTLE CITY!

Description: Mystery Game

The 'Prized Kettle' is Missing and you have to find it! Answer the questions
and take unexpected paths to find the Prized Kettle!

Pathway 1:

Pathway 2:


References:

- Screen clearer: https://www.scaler.com/topics/how-to-clear-screen-in-python/
- Sleep function: 

'''

'''
Part One: Function Definitions
-------------------------------
In this part there are X functions total:

* printAndIntro()
    - This function will be used to print out the welcome message for the user which will:
        ~ Provide introduction to Kettle City
        ~ Provide context
        ~ Provide the basics of how the game will run
        
* clearAndTime()
    - Automatically clears code with a test to check the OS the program is running on
    - Sets the sleep function to a certain amount of seconds to be used continuosly
    
*beginGame()
    - Actual start of game
    - First part where player gets to know everyone
        
'''
#array of strings that contain the title of the characters. (eg) Mayor.
#Each subscript corresponds to a subscript in the next array, which contains
#the names of the characters
charactListTitle = ["Mayor","Reporter" , "Business Woman", "Police Chief","Investigator"]

#array of strings that contain the names of the characters. (eg) A.Cooper Joe
#Each subscript corresponds to a subscript in the next array, which contains
#the names of the characters
charactList=["Chaila Té", "A.Cooper Joe", "Starla Bucks", "Pam.P.kin-Spice","Honey Pott"]

#beginning of function printAndIntro
def printAndIntro():
    #print statement that prints out game title
    print('''\n\n\t\t\t\t\t********
    \t\t\tKETTLE CITY: The mystery of the Golden Kettle
    \t\t\t\t\t********''')

    #sleep funnction that slows down execution of the next print command
    #allows for better readibility when the program is running
    time.sleep(5)

    #os call that clears game title
    os.system('clear') if ("linux" in platform) or ("darwin" in platform) else os.system("cls")

    #print statement that prints out welcome message
    print("*\n" * 3, "Welcome to Kettle City!")
    # sleep function that slows down execution of the next print command
    # allows for better readibility when the program is running
    time.sleep(2)

    print(
    '''A vibrant community of kettle manufacturers, 
teapot artisans, coffee machine builders,
tea and coffee connoisseurs, 
and most importantly --- CAFFEINE ADDICTS.
    ''')
    time.sleep(10)
    os.system('clear') if ("linux" in platform) or ("darwin" in platform) else os.system("cls")

    print(
        '''But alas! A terrible crime has been committed... the city's Golden Kettle Statue
has been stolen. It's your job to find out the who,what,why of this mystery!
              ''')

    time.sleep(10)
    os.system('clear') if ("linux" in platform) or ("darwin" in platform) else os.system("cls")

def beginGame():
    print(
        "\n", charactListTitle[3],
        charactList[3],
        ":Thank goodness you're here",
        charactListTitle[4],
        charactList[4],
        "!")

printAndIntro()
beginGame()







