# -*- coding: cp1252 -*-

###############################################
##                                           ##
## TABLE OF CONTENTS:                        ##
##   0 - Type assets                         ##
##       0.0 - List of types                 ##
##       0.1 - Dictionary of type advantages ##
##       0.2 - Dictionary of type defenses   ##
##   1 - Useful fuctions                     ##
##       1.0 - List + dictionary returns     ##
##       1.1 - Print functions               ##
##       1.2 - Return functions              ##
##                                           ##
###############################################

##0     TYPE ASSETS

##0.0   LIST OF TYPES

typel = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel']
typellc = []
for en in typel:
    typellc.append(str.lower(en))


##0.1   DICTIONARY OF TYPE ADVANTAGES
    
typedict = {
    'Normal':   {#NorTD
        2.0: [],
        1.0: typel[0:12] + typel[14:16],
        0.5: ['Rock', 'Steel'],
        0.0: ['Ghost']
    },
    'Fire':     {#FirTD
        2.0: ['Grass', 'Ice', 'Bug', 'Steel'],
        1.0: ['Normal', 'Electric'] + typel[6:13] + ['Ghost', 'Dark'],
        0.5: ['Fire', 'Water', 'Rock', 'Dragon'],
        0.0: []
    },
    'Water':    {#WatTD
        2.0: ['Fire', 'Ground', 'Rock'],
        1.0: ['Normal', 'Electric', 'Ice', 'Fighting', 'Poison', 'Flying', 'Psychic', 'Bug', 'Ghost', 'Steel'],
        0.5: ['Water', 'Grass', 'Dragon'],
        0.0: []
    },
    'Electric': {#EleTD
        2.0: ['Water', 'Flying'],
        1.0: ['Normal', 'Fire', 'Ice', 'Fighting', 'Poison', 'Psychic','Bug', 'Rock', 'Ghost', 'Dark', 'Steel'],
        0.5: ['Electric', 'Grass', 'Dragon'],
        0.0: ['Ground']
    },
    'Grass':    {#GraTD
        2.0: ['Water', 'Ground','Rock'],
        1.0: ['Normal', 'Electric', 'Ice', 'Fighting', 'Psychic', 'Ghost', 'Dark'],
        0.5: ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel'],
        0.0: []
    },
    'Ice':      {#IceTD
        2.0: ['Grass', 'Ground', 'Flying', 'Dragon'],
        1.0: ['Normal', 'Electric', 'Fighting', 'Poison', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dark'],
        0.5: ['Fire', 'Water', 'Ice', 'Steel'],
        0.0: []
    },
    'Fighting': {#FigTD
        2.0: ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
        1.0: ['Fire', 'Water', 'Electric', 'Grass', 'Fighting', 'Ground', 'Dragon'],
        0.5: ['Poison', 'Flying', 'Psychic', 'Bug'],
        0.0: ['Ghost'],
    },
    'Poison':   {#PoiTD
        2.0: ['Grass'],
        1.0: ['Normal', 'Fire', 'Water', 'Electric', 'Ice', 'Fighting', 'Flying', 'Psychic', 'Bug', 'Dragon', 'Dark'],
        0.5: ['Poison', 'Ground', 'Rock', 'Ghost'],
        0.0: ['Steel'],
    },
    'Ground':   {#GroTD
        2.0: ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
        1.0: ['Normal', 'Water', 'Ice', 'Fighting', 'Ground', 'Psychic', 'Ghost', 'Dragon', 'Dark'],
        0.5: ['Grass', 'Bug'],
        0.0: ['Flying'],
    },
    'Flying':   {#FlyTD
        2.0: ['Grass', 'Fighting'],
        1.0: ['Normal', 'Fire', 'Water', 'Ice', 'Poison', 'Ground', 'Flying', 'Psychic', 'Ghost', 'Dragon', 'Dark'],
        0.5: ['Electric', 'Rock', 'Steel'],
        0.0: [],
    },
    'Psychic':  {#PsyTD
        2.0: ['Fighting', 'Poison'],
        1.0: typel[0:6] + ['Ground', 'Flying', 'Bug', 'Rock', 'Ghost', 'Dragon'],
        0.5: ['Psychic', 'Steel'],
        0.0: ['Dark'],
    },
    'Bug':      {#BugTD
        2.0: ['Grass', 'Psychic', 'Dark'],
        1.0: ['Normal', 'Water', 'Electric', 'Ice', 'Ground', 'Bug', 'Rock', 'Dragon'],
        0.5: ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel'],
        0.0: [],
    },
    'Rock':     {#RocTD
        2.0: ['Fire', 'Ice', 'Flying', 'Bug'],
        1.0: ['Normal', 'Water', 'Electric', 'Grass', 'Poison', 'Psychic', 'Rock', 'Ghost', 'Dragon', 'Dark'],
        0.5: ['Fighting', 'Ground', 'Steel'],
        0.0: [],
    },
    'Ghost':    {#GhoTD
        2.0: ['Psychic', 'Ghost'],
        1.0: typel[1:10] + ['Bug', 'Rock', 'Dragon'],
        0.5: ['Dark', 'Steel'],
        0.0: ['Normal'],
    },
    'Dragon':   {#DraTD
        2.0: ['Dragon'],
        1.0: typel[0:14] + ['Dark'],
        0.5: ['Steel'],
        0.0: [],
    },
    'Dark':     {#DarTD
        2.0: ['Psychic', 'Ghost'],
        1.0: typel[0:6] + ['Poison', 'Ground', 'Flying', 'Bug', 'Rock', 'Dragon'],
        0.5: ['Fighting', 'Dark', 'Steel'],
        0.0: [],
    },
    'Steel':    {#SteTD
        2.0: ['Ice', 'Rock'],
        1.0: ['Normal', 'Grass'] + typel[6:12] + ['Ghost', 'Dragon', 'Dark'],
        0.5: ['Fire', 'Water', 'Electric', 'Steel'],
        0.0: [],
    },
}

##0.2   DICTIONARY OF TYPE DEFENSES

typedefdict = {}
for typec in typel:
    tempd = {2.0: [], 1.0: [], 0.5: [], 0.0: []}
    for x in typedict:
        for y in typedict[x]:
            if typec in typedict[x][y]:
                tempd[y].append(x)
    typedefdict[typec] = tempd
    

##1     USEFUL FUNCTIONS

##1.0   LIST + DICTIONARY RETURNS

##Oh my god, Samuel. Did you seriously forget you wrote these functions? These would've been useful AGES ago.
def typeadv(typec):
    """Returns 4 lists about the type typec."""
    x = typedict[typec.title()]
    return x[2.0], x[1.0], x[0.5], x[0.0]
def typedef(typec):
    """Returns 4 lists about the type typec."""
    x = typedefdict[typec.title()]
    return x[2.0], x[1.0], x[0.5], x[0.0]
def typed(typec, td=typedict):
    """Returns 4 lists about the type typec, from dictionary td."""
    x = td[typec.title()]
    return x[2.0], x[1.0], x[0.5], x[0.0]

def typeadvD(typec):
    """Returns a dict about the type typec."""
    x = typedict[typec.title()]
    return x
def typedefD(typec):
    """Returns a dict about the type typec."""
    x = typedefdict[typec.title()]
    return x
def typedD(typec, td=typedict):
    """Returns a dict about the type typec, from dictionary td."""
    x = td[typec.title()]
    return x

##1.1 PRINT FUNCTIONS

##These following functions are used to PRINT SUPER EFFECTIVE, PRINT EFFECTIVE,
##PRINT NOT VERY EFFECTIVE, PRINT NOT EFFECTIVE, PRINT DEFENSE SUPER EFFECTIVE,
##PRINT DEFENSE EFFECTIVE, PRINT DEFENSE NOT VERY EFFECTIVE, PRINT DEFENSE
##NOT EFFECTIVE, respectively.

def printse(typec, prefix="", suffix=""):
    """Prints super effective, with prefix and suffix."""
    e = typeadv(typec)[0]
    for n in e:
        print str(prefix) + n + str(suffix)
def printe(typec, prefix="", suffix=""):
    """Prints effective, with prefix and suffix."""
    e = typeadv(typec)[1]
    for n in e:
        print str(prefix) + n + str(suffix)
def printnve(typec, prefix="", suffix=""):
    """Prints not very effective, with prefix and suffix."""
    e = typeadv(typec)[2]
    for n in e:
        print str(prefix) + n + str(suffix)
def printne(typec, prefix="", suffix=""):
    """Prints not effective, with prefix and suffix."""
    e = typeadv(typec)[3]
    for n in e:
        print str(prefix) + n + str(suffix)
def printdse(typec, prefix="", suffix=""):
    """Prints defensive super effective, with prefix and suffix."""
    e = typedef(typec)[0]
    for n in e:
        print str(prefix) + n + str(suffix)
def printde(typec, prefix="", suffix=""):
    """Prints defensive effective, with prefix and suffix."""
    e = typedef(typec)[1]
    for n in e:
        print str(prefix) + n + str(suffix)
def printdnve(typec, prefix="", suffix=""):
    """Prints defensive not very effective, with prefix and suffix."""
    e = typedef(typec)[2]
    for n in e:
        print str(prefix) + n + str(suffix)
def printdne(typec, prefix="", suffix=""):
    """Prints defensive not effective, with prefix and suffix."""
    e = typedef(typec)[3]
    for n in e:
        print str(prefix) + n + str(suffix)
##HERE ENDS BORING PRINT FUNCTIONS
##FOLLOWING: SLIGHTLY MORE FUN PRINT FUNCTIONS

##Actually, the following functions prints the advantages and defenses of type 'typec', respectively, in a slightly non-friendly format.
def printadvs(typec):
    """Prints effects of type typec in a new-line list format."""
    print "The type", typec, "is super effective (2.0x damage) against the following types:"
    print
    printse(typec, "  ")
    print
    print typec, "is normally effective (1.0x damage) against:"
    print
    printe(typec, "  ")
    print
    print typec, "is not very effective (0.5x damage) against:"
    print
    printnve(typec, "  ")
    print
    print typec, "is not effective (0.0x damage) against:"
    print
    printne(typec, "  ")
    print

def printdefs(typec):
    """Prints effects against type typec in a new-line list format."""
    print "The following types are super effective (2.0x damage) against" + typec + ":"
    print
    printdse(typec, "  ")
    print
    print "The following are normally effective (1.0x damage) against" + typec + ":"
    print
    printde(typec, "  ")
    print
    print "The following are not very effective (0.5x damage) against" + typec + ":"
    print
    printdnve(typec, "  ")
    print
    print "The following are not effective (0.0x damage) against" + typec + ":"
    print
    printdne(typec, "  ")
    print

## printptable prints a table of advantages or defenses for a certain type.
def printptable(typec, t="adv", at=typedict, ad=typedefdict):
    """Prints a table of advantages or defenses (t) for type typec, using dicts at and ad."""
    typec = typec[0].upper() + typec[1:].lower() ## This line capitalizes the type correctly for future use with the dictionaries.
    if t == "adv":
        typedict = at
    if t == "def":
        typedict = ad
    else:
        typedict = at
    if typedict == at:
        tabletype = "advantages"
    else:
        tabletype = "defenses" ## Previous lines set the type of table to be printed - advantages or defenses.
    print "2.0x\t1.0x\t0.5x\t0.0x\t" + "<<" + typec.upper(), tabletype + ">>" ## Labels the columns.
    print "\t\t\t\t\t|"
    if len(typedict[typec][2.0]) > 0:
        se = 1
    else:
        se = 0
    if len(typedict[typec][1.0]) > 0:
        e = 1
    else:
        e = 0
    if len(typedict[typec][0.5]) > 0:
        nve = 1
    else:
        nve = 0
    if len(typedict[typec][0.0]) > 0:
        ne = 1
    else:
        ne = 0 ## Previous lines set boring, uneffective ways to tell if a column is empty.
    al = 0
    cur1 = 0
    cur2 = 0
    cur3 = 0
    cur4 = 0
    while al < 4: # al is a variable that stores how many columns are empty - and since there are only 3 columns, 4 is where it stops printing.
        al = 0
        if se == 1:
            try:
                print typedict[typec][2.0][cur1][0:7] + "\t",
                cur1 += 1
            except IndexError:
                se = 0
                print "\t",
                al += 1
        else:
            print "\t",
            al += 1
        if e == 1:
            try:
                print typedict[typec][1.0][cur2][0:7] + "\t",
                cur2 += 1
            except IndexError:
                e = 0
                print "\t",
                al += 1
        else:
            print "\t",
            al += 1
        if nve == 1:
            try:
                print typedict[typec][0.5][cur3][0:7] + "\t",
                cur3 += 1
            except IndexError:
                nve = 0
                print "\t",
                al += 1
        else:
            print "\t",
            al += 1
        if ne == 1:
            try:
                print typedict[typec][0.0][cur4][0:7] + "\t\t|",
                cur4 += 1
            except IndexError:
                ne = 0
                print "\t\t|",
                al += 1
        else:
            al += 1
            if al == 4:
                break
            print "\t\t|",
            
        print ## The long part before this just prints every type in the table in a "SE\tE\t\NVE\tNE\t" format.

##1.2   RETURN FUNCTIONS

def typegen(typel=typel):
    """Generates a random type."""
    return choice(typel)

def attackEffectivity(atype, type1, type2=None, STAB=None, typedict=typedict, typedefdict=typedefdict):
    """Returns the attack effectivity of atype against type1 and optionally type2, with optional STAB and dictionary choice."""
    effect1 = None ## Setting       variables     for     whole
    effect2 = None ##         dummy           fun     the       family.
    if type1.lower() == type2.lower(): ## Check for two of the same type.
        type2 = None
    if STAB == None: ## The following indent takes care of the STAB multiplier.
        STAB = raw_input("Does the attack have STAB? (Y/N) >")
        if STAB.lower() == "y" or STAB.lower() == "yes":
            STAB = 1.5
            print "Noted."
        elif STAB.lower() == "n" or STAB.lower() == "no":
            STAB = 1.0
            print "Noted."
        else:
            STAB = 1.0
            print "Uh, I'm going to take that as a no."
    while effect1 == None: ## Sets the local variable effect1 to whatever effect type1 corresponds to in the active dictionary.
        try:
            for effect in typedefD(type1):
                for comparisontype in typedefD(type1)[effect]:
                    if comparisontype.lower() == atype.lower():
                        effect1 = effect
                        break
                if effect1 != None:
                    break
        except KeyError:
            type1 = raw_input("Please input a valid first type. >")
    if type2 != None and type2 != "": ## Sets the local variable effect2 to whatever effect type2 corresponds to in the active dictionary, if type2 is valid.
        try:
            for effect in typedefD(type2):
                for comparisontype in typedefD(type2)[effect]:
                    if comparisontype.lower() == atype.lower():
                        effect2 = effect
                        break
                if effect2 != None:
                    break
        except KeyError:
            print "Type 2 is not valid, and has been ignored. Now comparing " + atype + " and " + type1 + "."
    if effect2 == None:             ## For single-typed Pokémon
        return effect1 * STAB
    return effect1 * effect2 * STAB ## For double-typed Pokémon
