#GOAL IS I WILL NOT FIND ANY COMMENTS AT THE END AKA ALL THE TO DO MESSAGES

define h = Character("Human")
define a = Character("Alien")
define ma = Character("Market Alien") # I should change his name some time...
define ga = Character("Grocery Store Alien")

init python:
    translation = False
    progress = 0
    ewords =    ["zinky zoogle", "vorp", "zeeky", "booble"   , "zeekybooble"   , "beeble", "mee", "eep", "Forp", "zilk", "lort", "zort", "bartle", "yuckle", "birt", "corm", "harkle", "horp", "beekyfooble", "quarkle", "feep" , "geekyduckle", "veepy"    , "bogos" , "binted" , "meep"]
    awords =    ["hey"         , "what", "just" , "wondering", "just wondering", "if"    , "you", "got", "your", "is"  , "a"   , "is a", "hello" , "let"   , "me"  , "show", "around", "pick", "whatever"   , "want"   , "apple", "thank you"  , "diet coke", "photos", "printed", "you got"]
    kwords = ewords
    seenWords = [False         , False , False  , False      , False           , False   , False, False, False , False , False , False , False   , False   , False , False , False   , False , False        , False    , False  , False        , False      , False   , False    , False]

label start:
    $ progress = 0

    scene bg warning

    scene bg photosPrinted1
    show human talking at left # to be made
    h "Hey, just wondering if you got your photos printed?"
    scene bg photosPrinted2
    show human idle at left # to be made
    show alien responding at right # to be made
    a "[kwords[23]] [kwords[24]]?"
    scene bg photosPrinted3
    show human talking at left # to be made
    show alien idle at right # to be made
    h "What"
    scene bg photosPrinted4
    show human idle at left # to be made
    show alien idle at right # to be made
    a "-confused alien noises-"
    python:
        for i in [23, 24]:
            seenWords[i] = True

    # insert cutscene
    
    scene bg bogosBinted1
    show alien talking at left # to be made
    a "[kwords[0]], [kwords[2]][kwords[3]] [kwords[5]] [kwords[25]] [kwords[8]] [kwords[23]] [kwords[24]]?"
    scene bg bogosBinted2
    show alien idle at left # to be made
    show human responding at right # to be made
    h "Photos printed?"
    scene bg bogosBinted3
    show alien talking at left # to be made
    show human idle at right # to be made
    a "[kwords[1]]?"
    scene bg bogosBinted4
    show alien idle at left # to be made
    show human idle at right # to be made
    h "- confused human noises-"
    python:
        for i in [0, 1, 2, 3, 5, 8, 23, 24, 25]:
            seenWords[i] = True

    menu:
        "I want a translation":
            jump dictionary
        "I had no idea what that was about":
            jump transportToPlanet

label transportToPlanet:
    $ progress = 1

    # to insert cutscene
    h "What was that..."
    h "This was probably the weirdest interactions ever"
    # showing human on spaceship and bro looks out the window or smth
    h "hey... where am I?"
    h "Am I in space?!?!?"

    "uh oh. Mr Human seems to be landing on another planet... Just look outside and see"
    # insert cutscene where my guy lands on alien planet
    
    # spaceship about to land, alien walks up to that guy still inside spaceship
    # here's where I proceed to make up a whole entire language...
    show  alien talking at center # to be made
    a "[kwords[0]]!"
    h "Whaat... what should I respond with"
    python:
        seenWords[0] = True

    jump selection1

label selection1:
    $ progress = 2
    menu: 
        "Hey!":
            $ response1 = "ignores"
        "Zinky zoogle!":
            $ response1 = "greeting"
        "Vorp?":
            $ response1 = "explanation"
    jump planet

label planet:

    scene bg planet # to be made

    if response1 == "ignores":
        jump selection1
    
    show alien talking at center
    if response1 == "explanation":
        # Hey is hello
        a "[kwords[12]] [kwords[9]] [kwords[0]]"
        h "[kwords[0]]"
        python:
            for i in [0, 9, 12]:
                seenWords[i] = True

    # Hello! Let me show you around
    a "[kwords[12]]! [kwords[13]] [kwords[14]] [kwords[15]] [kwords[6]] [kwords[16]]"
    python:
        for i in [6, 12, 13, 14, 15, 16]:
            seenWords[i] = True

    menu:
        "What is going on? I better keep moving":
            jump fruitStall
        "I think I might need to take some notes":
            jump dictionary

label fruitStall:
    $ progress = 3

    #cutscene of them walking into a market

    scene bg fruitStall # to be made

    show marketAlien talking at left # to be made
    # Hey! Hello! Just pick whatever you want
    ma "[kwords[0]]! [kwords[12]]! [kwords[2]] [kwords[17]] [kwords[18]] [kwords[6]] [kwords[19]]"
    show alien talking at right # to be made
    # Hello! Me want apple"
    a "[kwords[12]]! [kwords[14]] [kwords[19]] [kwords[20]]"

    show marketAlien handingApple at left # to be made
    ma "[kwords[20]]!"
    #pause
    show marketAlien idle at left # to be made
    show alien withApple at right # to be made
    a "[kwords[21]]"
    
    python:
        for i in [0, 2, 6, 12, 14, 17, 18, 19, 20, 21]:
            seenWords[i] = True

    menu:
        "uhh let's just keep going":
            jump groceryStore
        "I think I'm catching on":
            jump dictionary

label groceryStore:
    $ progress = 4

    #cutscene of them walking through the market

    scene bg groceryStore # to be made

    show groceryAlien talking at right # to be made
    #Hello! Just pick whatever you want
    ga "[kwords[12]]! [kwords[2]] [kwords[17]] [kwords[18]] [kwords[6]] [kwords[19]]"
    show alien talking at left # to be made
    #Hey! Me want diet coke
    a "[kwords[0]]! [kwords[14]] [kwords[19]] [kwords[22]]"

    show groceryAlien handingCoke at right # to be made
    show alien idle at left
    ga "[kwords[22]]!"
    show groceryAlien idle at right
    show alien withCoke at left # to be made
    a "[kwords[21]]"

    python:
        for i in [0, 2, 6, 12, 14, 17, 18, 19, 22]

    menu:
        "I still have no idea whats going on":
            jump printShop
        "Gotta take some notes":
            jump dictionary

label printShop:
    $ progress = 5

    # show them walking through the market again

    scene bg printShop # to be made

    show photoAlien talking at left # to be made
    show alien idle at center # to be made
    show human idle at right # to be made
    "Print Shop Alien" "[kwords[0]]"

    # Just wondering, what you want?
    $ finalAnswer = renpy.input("[kwords[2]] [kwords[3]], [kwords[1]] [kwords[6]] [kwords[19]]?")

    if finalAnswer.lower() == "barkle bogos binted":
        jump finalScene
    else:
        a "Vorp?"
        menu:
            "back to the beginning":
                $ progress = 0
                jump start

            "back to the planet":
                $ progress = 1
                jump planet
            "back to the fruit stall":
                $ progress = 3
                jump fruitStall
            "back to the grocery store":
                $ progress = 4
                jump groceryStore
            "I want to try again":
                $ progress = 5
                jump printShop
            "Consult my notebook":
                jump dictionary

# to finish
label dictionary:
    python:
        counter = 0
        for word in kwords:
            if seenWords[counter] == True:
                if kwords[counter] != awords[counter]:    
                    renpy.say("[awords[counter]] translated is [kwords[counter]]")
                else:
                    renpy.say("[awords[counter]] translated is _______")
                    menu:
                        "next":
                            counter += 1
                        "update translation":
                            kwords[counter] = renpy.input("Enter your translation")
                            counter += 1
                        "hint"
                        "back":
                            if progress == 0:
                                jump transportToPlanet
                            elif progress == 1:
                                jump selection1
                            elif progress == 2:
                                jump fruitStall
                            elif progress == 3:
                                jump groceryStore
                            elif progress == 4:
                                jump printShop
                            elif progress == 5:
                                jump printShop
                            else:
                                jump start
            else:
                counter +=1

label finalScene:
    
    scene bg finalBG # to be made
    show aliens waving at truecenter # to be made
    a "BYEEEEEE"
    a "BYEEEEEEEEEE"
    a "farewell to all of you"
    # think about inserting more ending scene stuffs here