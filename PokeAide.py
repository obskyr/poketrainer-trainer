# -*- coding: cp1252 -*-

from pokehelp import *

##                                 #####
##                               ######               
##                               ##                  
##   ########          #    ##            ##   ##   
## ############       ###   ###  ######   ###  ##       ####
## ######   ####       ######   ##   ##   ### ###   ###  ###   ###
##   #####   ###  ####  ####   ### ##     ####### ###### ###   ##
##    ####   ## ###  ## ######  ########  ## ### ###  ##  ##  ##
##     ####### ###    # ### ####  ####   ### # # ####### ###### 
##      #####  ######## ##    ####      ###    ## ##### #######
##       ####    ####   ##      ###             #      ### ### 
##        ####                                              ##
##         ###                                              ## 

## -- VERY NECESSARY ASCII ART ABOVE, REMOVING IT WILL HAVE TERRIFYING CONSEQUENCES --

###############################################
##                                           ##
## TABLE OF CONTENTS:                        ##
##   0 - User interface functions            ##
##       0.0 - User interface functions      ##
##   1 - Main loop                           ##
##       1.0 - Main loop                     ##
##                                           ##
###############################################

##0     USER INTERFACE FUNCTIONS

##0.0   USER INTERFACE FUNCTIONS

def printTypes(typel=typel):
    print "There are " + str(len(typel)) + " types of Pokémon. They are:"
    for x in typel[:-2]:
        print x + ",",
    print typel[-2] + " and " + typel[-1] + "."

def aE_UI(typel=typel): ## Provides a simple user interface for inputting types to attackEffectivity(). Quite self-explanatory.
    atype = raw_input("Please input the type of the attack. >").strip()
    while atype.title() not in typel:
        atype = raw_input("Please input a VALID attack type. >").strip()
    type1 = raw_input("Please input the first type of the defending Pokémon. >").strip()
    while type1.title() not in typel:
        type1 = raw_input("Please input a VALID first type. >").strip()
    type2 = raw_input("Please input the second type of the defending Pokémon.\n(Leave blank if there is none) >").strip()
    while type2.title() not in typel and type2 != "" or type2.lower() == type1.lower():
        if not type2.lower() == type1.lower():
            type2 = raw_input("Please input a VALID second type, or nothing at all. >").strip()
        else:
            type2 = raw_input("Please enter a type separate from the first. >").strip()
    if type2 == None or type2 == "":
        print "\nThe damage multiplier for a " + atype.lower() + " attack against a " + type1.lower() + " Pokémon is " + str(attackEffectivity(atype, type1, type2)) + "."
    else:
        print "\nThe damage multiplier for a " + atype.lower() + " attack against a " + type1.lower() + "/" + type2.lower() + " Pokémon is " + str(attackEffectivity(atype, type1, type2)) + "."

def chooseTable(at=typedict, ad=typedefdict): ##This function helps with invoking printptable() in a slightly user-friendly way.
    typechoice = str.lower(raw_input("Which type would you like a table for? >")).strip()
    while typechoice not in typellc: ## This loop makes sure that the input type is valid, as to not invoke an error.
        print "That is not a valid type."
        typechoice = str.lower(raw_input("Which type would you like a table for? >")).strip()
    else: ## This else clause is kind of meaningless, since there is no break in the previous clause, and should probably be removed. OH WELL LEARNING PYTHON
        tabletypechoice = raw_input("Which type of table - advantages or defenses?\n(Valid choices are \"adv\" and \"def\") >").lower().strip()
        while tabletypechoice != 'adv' and tabletypechoice != 'def': ## These lines just set the type of table, advantages or defenses.
            tabletypechoice = raw_input("Please enter \"adv\" or \"def\". >").lower().strip()
        printptable(typechoice, tabletypechoice, at, ad)

def pMenu(): ## Prints the menu (feel free to edit, as long as you edit your menu function with it. Returns a choice.
    print "\nACTIONS:"
    print " (Type the CAPITALS to choose)"
    print " -LIST of types"
    print " -TABle of advantages/defenses"
    print " -ATTack effectivity check"
    print " -QUIT"
    return raw_input("Choose an action >")

def Menu(): #Basically the main loop, uses pMenu() to print the menu and then does things based on the user's input.
    while True:
        valid_choices = ["tab", "att", "q", "quit", "list"] ## List of valid actions, make sure to update corresponding to the actions you plan on having available.
        choice = "HAHA I'M NOT IN VALID CHOICES"
        choice = pMenu().lower().strip()
        while choice not in valid_choices: ## Makes sure the user's choice is valid.
            print "That is not a valid action."
            choice = raw_input("Please input a valid action. >").lower(),strip()
        if choice == "list":
            printTypes()
        elif choice == "tab":   ## Invokes chooseTable().
            chooseTable()
        elif choice == "att":   ## Invokes aE_UI().
            aE_UI()
        elif choice == "quit" or choice == "q":
            break               ## Invokes a break out ot Menu().


##1     MAIN LOOP

##1.0   MAIN LOOP

Menu()
