# -*- coding: cp1252 -*-
import pokehelp                             ## Needed for Pokémon-related calculations
import scoring                              ## Needed for scoring and various config functions
from random import choice, randint, shuffle ## Needed for random generation
from os import remove as osremove           ## Needed for deleting files
from collections import Counter             ## Needed for duplicate removal

typel_local = pokehelp.typel[:] ## Dummy variable for later use

## Good to know:
##  All parameter generators' first parameter output should be/is
##  the type that dynamiclearning counts.

def configOps():
    """Loads or creates a configuration file."""
    global config
    try:
        config = scoring.cVars('trainerc.cfg') ## Loads config. Next few lines convert entries to desired datatypes.
        config['numtries'] = abs(int(config['numtries']))
        config['dynamiclearning'] = scoring.stringToBool(config['dynamiclearning'])
        config['numques'] = int(config['numques'])
        config['savescores'] = scoring.stringToBool(config['savescores'])
        if config['numques'] < 3:
            print "'numques' is too small. Adjusted to the minimum value, 4."
            config['numques'] = 4
    except IOError: ## Following indent creates config if such does not already exist.
        print "Creating config..."
        config = {'name': "trainer", 'savescores': True, 'numtries': 1, 'dynamiclearning': True, 'numques': 6, 'learnfile': 'learning.lrn', 'scorefile': 'trainerscores.txt'}
        scoring.createConfig(config, 'trainerc.cfg')

configOps() ##Runs configOps for use in future functions.

def dlOps(learnfile=config['learnfile'], dl=config['dynamiclearning']):
    """Loads or creates dynamic learning file."""
    global dynamiclearningDict ## Since the variable will be used in future functions
    global typel_local ## Ditto.
    if dl: ## If the user has set not to use dynamiclearning, this indent doesn't execute.
        learnfile = 'learning.lrn' ## Default filename.
        try:
            dynamiclearningDict = scoring.cVars(learnfile) ## Tries to load and subsequently convert entries.
            for x in dynamiclearningDict:
                dynamiclearningDict[x] = int(dynamiclearningDict[x])
        ## The dynamic learning in this program works by counting how often you answer
        ## correctly about every type. Once you reach a certain number, that type has a
        ## chance to be deleted from the local list of types to be used, so that you
        ## only train with types you haven't fully grasped yet.
        except IOError: ## Creates dynamic learning file and dictionary if such does not already exist.
            dynamiclearningDict = {'Ghost': 0, 'Dark': 0, 'Poison': 0, 'Electric': 0, 'Normal': 0, 'Fire': 0, 'Psychic': 0, 'Flying': 0, 'Ice': 0, 'Dragon': 0, 'Water': 0, 'Fighting': 0, 'Steel': 0, 'Rock': 0, 'Grass': 0, 'Bug': 0, 'Ground': 0}
            scoring.createConfig(dynamiclearningDict, learnfile)
            print "Creating dynamic learning file..."
        dk = dynamiclearningDict.keys()
        shuffle(dk)
        i = 0
        for typekey in dynamiclearningDict: ## Removes types that you already know about.
            if dynamiclearningDict[dk[i]] >= 12 and len(typel_local) > 9:
                typel_local.remove(typekey)
                print typel_local
            i += 1
    else:
        typel_local = pokehelp.typel[:]

dlOps() ## Runs dlOps, in order for future functions to work.

def saveDl(learnfile):
    """Saves dynamic learning dictionary to file 'learnfile'."""
    scoring.createConfig(dynamiclearningDict, learnfile) ## Simply saves using scoring.createConfig().

def clearDl(learnfile='learning.lrn', lfrepr="your dynamic learning data"):
    """Deletes file learnfile with confirmation using 'lfrepr' as representation."""
    x = 'godacetchemal'
    confirmationquestion = "Are you sure you want to delete " + str(lfrepr) + "? (Y/N) >"
    while x.lower() not in ['yes', 'no', 'y', 'n']: ## Makes sure the user's answer is valid.
        x = raw_input(confirmationquestion)
        if x.lower() in ['yes', 'y']:
            try:
                osremove(learnfile) ## Deletes file.
                print "Deleted successfully."
                break
            except (IOError, WindowsError, OSError): ## Different error for different operative systems.
                print "That file does not exist!"
                break
        elif x.lower() in ['no', 'n']: ## Aborts deletion.
            print "Deletion aborted."
            break
        print "That is not a valid answer."

def eParamGen(dynamiclearning=False, STABtf=True):
    """Generates parameters for effectivityQuestion.
    Parameters 0 - 3, inclusive, work for pokehelp.attackEffectivity, too."""
    atype = choice(typel_local) ## Sets attack type according to a random choice in typel_local.
    type1 = choice(pokehelp.typel) ## Same thing, DL independent
    type2 = None
    type2TF = choice((True, False))
    if type2TF:
        templ = pokehelp.typel[:]
        templ.remove(type1) ## Makes sure type2 isn't the same as type1.
        type2 = choice(templ)
    STAB = 1.0
    STABtf = choice((False, False, False, True))
    if STABtf:
        STAB = 1.5
    return atype, type1, type2, STAB, True, dynamiclearning ## Returns parameters in a format effectivityQuestion understands.

def effectivityQuestion(atype, type1, type2=None, STAB=1.0, STABtf=True, dynamiclearning=False):
    """Generates a question where the answer is the effectivity multiplier for an attack
    of type 'atype' against a Pokémon of types 'type1' and 'type2', using
    STAB as the STAB multiplier. STABtf can be set to False to not incorporate
    STAB at all."""
    type2str = ""
    if type2 != None and type2 != "":
        type2 = type2.title()
        type2str = "/" + type2 ## Makes it easier to format the question later.
    STABstr = " without STAB" ## Ditto.
    if STAB > 1.0:
        STABstr = " with STAB" ## Ditto.
    if not STABtf: ## Only if STABtf is true, otherwise STAB isn't even taken into account.
        STAB = 1.0
        STABstr = ""
    correctanswer = pokehelp.attackEffectivity(atype.title(), type1.title(), type2, STAB) ## Uses pokehelp.attackEffectivity to determine the correct answer.
    question = "What is the effectivity multiplier for a " + atype + " attack against a " + type1.title() + type2str + " Pokémon" + STABstr + "?" ## Generates a question based on earlier parameters.
    useranswer = raw_input(question + " >")
    while True:
        try:
            if float(useranswer) == correctanswer: ## Simple conditionals test correctness.
                if dynamiclearning:
                    return True, atype
                return True
            if dynamiclearning:
                return False, atype
            return False
        except ValueError:
            useranswer = raw_input("That is not a number. Please input a valid effectivity multiplier. >")

def typegen(dynamiclearning=False):
    """Generates a random type."""
    if dynamiclearning: ## From typel_local only if dynamic learning is on.
        return choice(typel_local)
    return choice(pokehelp.typel)

def tHelp(typec=None, dynamiclearning=False): ## Pretty much all of this function is just returning random choices from different advantages and defenses.
    """Generates part of the parameters for typeInfoQuestion.""" 
    if typec == None:
        typec = typegen()
    if typec == None and dynamiclearning:
        typec = typegen(True)
    try:
        setype = choice(pokehelp.typedict[typec][2.0])
    except IndexError:
        setype = ""
    try:
        nvetype = choice(pokehelp.typedict[typec][0.5])
    except IndexError:
        nvetype = ""
    try:
        dsetype = choice(pokehelp.typedefdict[typec][2.0])
    except IndexError:
        dsetype = ""
    try:
        dnvetype = choice(pokehelp.typedefdict[typec][0.5])
    except IndexError:
        dnvetype = ""
    return setype, nvetype, dsetype, dnvetype

def tParamGen(dynamiclearning=False):
    """Generates random parameters for typeInfoQuestion."""
    x = typegen()
    if dynamiclearning:
        x = typegen(True)
    args = [i for i in tHelp(x)] ## Basically, it's just a random type, tHelp() and dynamiclearning.
    args.insert(0, x)
    args.append(dynamiclearning)
    return args

def tIQPartGen(setype, nvetype, dsetype, dnvetype):
    """Generates parts in order for typeInfoQuestion.
    Needed for consistent re-asks."""
    parts = []
    types = []
    effects = []
    if setype != "":
        separt = "is super effective against " + setype
        parts.append(separt)
        types.append(setype)
        effects.append('se')
    if nvetype != "":
        nvepart = "is not very effective against " + nvetype
        parts.append(nvepart)
        types.append(nvetype)
        effects.append('nve')
    if dsetype != "":
        dsepart = "takes double damage from " + dsetype
        parts.append(dsepart)
        types.append(dsetype)
        effects.append('dse')
    if dnvetype != "":
        dnvepart = "takes half damage from " + dnvetype
        parts.append(dnvepart)
        types.append(dnvetype)
        effects.append('dnve')
    happy = randint(2, 3)
    while len(parts) > happy:
        ri = (randint(0, len(parts) - 1))
        del parts[ri]
        del types[ri]
        del effects[ri]
    shuffle(parts)
    return parts, types, effects ## Just returns everything in the order typeInfoQuestion asks for it.

def typeInfoQuestion(typec, setype=None, nvetype=None, dsetype=None, dnvetype=None, dynamiclearning=False, parts=None):
    """Asks a question where a type is the desired answer
    based on the many parameters it has. Returns True/False, typec with dynamiclearning."""
    if dnvetype == None:
        setype, nvetype, dsetype, dnvetype = tHelp(typec)
    if parts == None:
        parts, types, effects = tIQPartGen(setype, nvetype, dsetype, dnvetype)
    else:
        parts, types, effects = parts
    print "Name a type that",
    for part in parts[:-1]:
        print part + ',',
    print "and " + parts[-1] + ".",
    useranswer = raw_input('>').title()
    while useranswer not in pokehelp.typel:
        useranswer = raw_input("Please input a valid type. >").title()
    if useranswer == typec: ## Easy check
        if dynamiclearning:
            return True, typec
        return True
    for typ, effect in zip(types, effects): ## Rest of the function is the hard check, needed for alternate solutions
        if effect == 'se':
            comdict = pokehelp.typedefdict
            comeffect = 2.0
        elif effect == 'nve':
            comdict = pokehelp.typedefdict
            comeffect = 0.5
        elif effect == 'dse':
            comdict = pokehelp.typedict
            comeffect = 2.0
        elif effect == 'dnve':
            comdict = pokehelp.typedict
            comeffect = 0.5
        if useranswer not in comdict[typ][comeffect]: ## Checks if useranswer is correct, breaks if not
            break
    else: ## Only execute if previous didn't break
        if dynamiclearning:
            return True, typec
        return True
    if dynamiclearning:
        return False, typec
    return False

def tEParamGen(dynamiclearning=False, total=None):
    """Generates parameters for typeEQuestion."""
    eff = choice([2.0, 0.5])
    typec = typegen(dynamiclearning)
    if total == None:
        total = randint(1, 2)
    if total > len(pokehelp.typedefdict[typec][eff]):
        total = len(pokehelp.typedefdict[typec][eff])
    return typec, eff, total, dynamiclearning ## In typeEQuestion format!

def typeEQuestion(typec, eff=None, total=None, dynamiclearning=False):
    """Asks for one to 'total' types that fill certain criteria."""
    tempd = {2.0: " super effective", 0.5: " not very effective"}
    if eff == None:
        eff = choice(tempd.keys())
    if total == None:
        total = randint(1, 2)
    if total > len(pokehelp.typedefdict[typec][eff]): ## Once...
        total = len(pokehelp.typedefdict[typec][eff])
        if total == 0:
            if eff == 2.0:
                eff = 0.5
            elif eff == 0.5:
                eff = 2.0
        total = randint(1, 2)
        if total > len(pokehelp.typedefdict[typec][eff]): ## And twice. Needed for Normal and custom types.
            total = len(pokehelp.typedefdict[typec][eff])
    totstr = str(total) + " types (separate by comma)"
    grammaryo = "are"
    if total == 1:
        totstr = "a type"
        grammaryo = "is"
    question = "Name " + totstr + " that " + grammaryo + tempd[eff] + " against " + typec + "."
    print question,
    useranswer = raw_input('>')
    if total == 1: ## Checking for a single answer is easier than multiple.
        while useranswer.title() not in pokehelp.typel:
            useranswer = raw_input("Please enter a valid answer. >")
        if useranswer.title() in pokehelp.typedefdict[typec][eff]:
            if dynamiclearning:
                return True, typec
            return True
        if dynamiclearning:
            return False, typec
        return False
    useranswer = useranswer.split(',')
    useranswer = [t.strip().title() for t in useranswer if t.strip().title() in pokehelp.typel]
    c = Counter(useranswer)
    for x, y in c.items(): ## Checks for doubles, as anti-cheat.
            if y > 1:
                useranswer = []
                print "No doubles!"
    while len(useranswer) != total:
        uastr = "Please enter " + str(total) + " valid types, separated by comma. >"
        useranswer = raw_input(uastr)
        useranswer = useranswer.split(',')
        useranswer = [t.strip().title() for t in useranswer if t.strip().title() in pokehelp.typel] ## Shortens the list to only valid types.
        c = Counter(useranswer)
        for x, y in c.items(): ## More checking for doubles.
            if y > 1:
                useranswer = []
                print "No doubles!"
    for t in useranswer:
        if t not in pokehelp.typedefdict[typec][eff]: ## Does a break if an incorrect answer is found
            break
    else: ## Only if previous didn't break
        if dynamiclearning:
            return True, typec
        return True
    if dynamiclearning:
        return False, typec
    return False

## Following dictionary contains the question functions and their respective
## parameter generation functions.
questionparam = {effectivityQuestion: eParamGen, typeInfoQuestion: tParamGen, typeEQuestion: tEParamGen}

def losemsg(qtype, params):
    """Returns a customized lose message for every question.
    Edit every time you add a new question type."""
    if qtype == effectivityQuestion: ## Lose message for effectivityQuestion.
        return "The correct effectivity multiplier is " + str(pokehelp.attackEffectivity(*params[0:4])) + "."
    elif qtype == typeInfoQuestion: ## Lose message for typeInfoQuestion.
        return "The intended type was " + params[0] + ", but there may be more correct solutions."
    elif qtype == typeEQuestion: ## Lose message for typeEQuestion.
        try:
            l = pokehelp.typedefdict[params[0]][params[1]]
            lstr = ', '.join(l[:-1])
        except IndexError:
            lstr = pokehelp.typedefdict[params[0]][params[1]][0]
        if len(pokehelp.typedefdict[params[0]][params[1]]) < 2: ## For Normal and custom types.
            return "Correct type was " + lstr + "."
        return "Correct types were: " + lstr + " and " + l[-1] + "."

def tryAgain(numtries, questionfunc, dynamiclearning=False, qpdict=questionparam, dld=dynamiclearningDict):
    """Asks question 'questionfunc' 'numtries' times, using
    qpdict[questionfunc] as the parameter generator."""
    global dynamiclearningDict ## All of these 'global' statements are in order for other functions to work.
    params = qpdict[questionfunc](dynamiclearning)
    if questionfunc == typeInfoQuestion:
        parts = tIQPartGen(*tHelp())
    for trycount in range(1, numtries + 1):
        if dynamiclearning:
            if not questionfunc == typeInfoQuestion: ## typeInfoQuestion needs special treatment, with the 'parts' variable.
                ## If I ever optimize this code, I'm going to move the parts gen into the param
                ## gen for typeInfoQuestion.
                if questionfunc(*params)[0]:
                    dynamiclearningDict[params[0]] += 1
                    return True, trycount, params
            else:
                if trycount == 1:
                    params += (parts,) ## Only adds parts to the parameter the first time around, as to not have too many parameters.
                if questionfunc(*params)[0]:
                    dynamiclearningDict[params[0]] += 1
                    return True, trycount, params
            print "Incorrect.\n"## Generic lose message without answer, in case you have tries left.
        else:
            if not questionfunc == typeInfoQuestion:
                if questionfunc(*params):
                   return True, trycount, params
            else:
                if trycount == 1:
                    params += (parts,)
                if questionfunc(*params):
                    return True, trycount, param
            print "Incorrect.\n" ## Generic lose message before customized losemsg(), when used in play().
    dynamiclearningDict[params[0]] -= 1
    return False, trycount, params

def play(dynamiclearning=config['dynamiclearning'], qpdict=questionparam, scoretime=True):
    """Plays a round of Trainer Trainer. Uses different parts of config."""
    totaltries = 0
    rights = 0
    for quesnum in range(0, config['numques'] + 1): ## Makes sure it uses config's number of questions
        qtype = choice(questionparam.keys())
        result, tries, params = tryAgain(config['numtries'], qtype, dynamiclearning, qpdict) ## Stays on tryAgain for config['numtries']. See tryAgain().
        ## Result is a boolean value, which decides if you answered right or not.
        ## Tries is the total number of tries you took during that question.
        ## Params is used to customize functions later, such as losemsg().
        totaltries += tries - 1
        if result: ##
            print "Nicely answered, " + config['name'] + "! Correct.\n" ## Hey, customizable name! Yeah!
            rights += 1
        else:
            print losemsg(qtype, params) ## Customized lose message for each type of question (qtype).
    if scoretime: ## You can quite easilty turn off scoring.
        try:
            hs = " with a previous high score of " + str(scoring.highScore(config['scorefile'])) ## High score string.
            hsn = scoring.highScore(config['scorefile']) ## Actual high score number.
        except IOError:
            hs = ", which is the first recorded score" ## High score string.
            hsn = 0 ## There is no high score if this executes. A negative score can't count as high score in this case.
        score = rights * (1000 / config['numques'])
        if not totaltries == 0:
            score -= totaltries * 20
        score -= (config['numques'] - rights) * 50
        ## Note to self:
        ## This scoring system might need some touching up. 1382 as max score? Whaaat?
        scoring.saveScore(score, config['scorefile'])
        if score > hsn:
            print "-- New high score! --"
        print "Your score was " + str(score) + hs + "!"

def pMenu(): ## Prints the menu (feel free to edit, as long as you edit your menu function with it. Returns a choice.
    """Prints menu, returns choice."""
    print "\nACTIONS:"
    print " (Type the number to choose)"
    print " 1. Play Trainer Trainer"
    print " 2. Reload config"
    print " 3. Reload dynamic learning file"
    print " 4. Delete dynamic learning file"
    print " 5. Delete scores"
    print " 0. Quit"
    return raw_input("Choose an action >")

def menu():
    """A main loop of sorts. Takes input from pMenu()."""
    while True:
        valid_choices = ['1', '2', '3', '4', '5', '0'] ## List of valid actions, make sure to update corresponding to the actions you plan on having available.
        choice = "HAHA I'M NOT IN VALID CHOICES"
        choice = pMenu().lower()
        while choice not in valid_choices: ## Makes sure the user's choice is valid.
            print "That is not a valid action."
            choice = raw_input("Please input a valid action. >").lower()
        if choice == '1': ## Play Trainer Trainer.
            play(scoretime=config['savescores'])
        elif choice == '2': ## Reload config.
            configOps()
            print "Config reloaded successfully."
        elif choice == '3': ## Reload dynamic learning file.
            dlOps()
            print "Dynamic learning file reloaded successfully."
        elif choice == '4': ## Delete dynamic learning file.
            clearDl(config['learnfile'])
        elif choice == '5': ## Delete scores file.
            clearDl(config['scorefile'], "your scores file")
        elif choice == '0': ## Quit.
            break               ## Invokes a break out of Menu().
    if config['dynamiclearning']: ## Saves data on proper exit.
        saveDl(config['learnfile'])
    
menu() ## Runs main loop.
