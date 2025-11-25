#GOAL IS I WILL NOT FIND ANY COMMENTS AT THE END AKA ALL THE TO DO MESSAGES

define h = Character("Human")
define a = Character("Alien")
define ma = Character("Market Alien") # I should change his name some time...
define ga  Character("Grocery Store Alien")

$ translation = false
$ progress = 0

label translation:

label start:
    $ progress = 0
    $ ewords = ["zinky zoogle", "vorp", "zeeky", "booble"   , "zeekybooble"   , "beeble", "mee", "eep", "Forp", "zilk", "lort", "zort", "bartle", "yuckle", "birt", "corm", "harkle", "horp", "beekyfooble", "quarkle", "feep" , "geekyduckle", "veepy"]
    $ awords = ["hey"         , "what", "just" , "wondering", "just wondering", "if"    , "you", "got", "your", "is"  , "a"   , "is a", "hello" , "let"   , "me"  , "show", "around", "pick", "whatever"   , "want"   , "apple", "thank you"  , "diet coke"]
    $ kwords = ewords
    #known words

    scene bg textHuman # to be made

    show human talking at left # to be made
    h "Hey, just wondering if you got your photos printed?"
    show alien responding at right # to be made
    a "bogos binted?"
    h "What"
    a "-confused alien noises-"

    # insert cutscene

    scene bg textAlien # to be made
    
    show alien talking at left # to be made
    a "Zinky zoogle, zeekybooble beeble meep Forp Bogos Binted?"
    show human responding at right # to be made
    h "Photos printed?"
    a "Vorp?"
    h "- confused human noises-"

    menu:
        "I want a translation":
            jump translation
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
    # temporary translations: 
    # Zinky zoogle: Hey
    # Vorp: what
    # photos printed: bogos binted
    # zeekybooble: just wondering
    # beeble: if
    # meep: you got
    # Forp: your
    
    # spaceship lands
    # here's where I proceed to make up a whole entire language...
    a "Zinky zoogle!"
    h "Whaat... what should I respond with"

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
    
    show alien talking at truecenter
    if response1 == "explanation":
        # Hey is hello
        a "Zinky zoogle zort bartle"
        h "Zinky zoogle"

    # Hello! Let me show you around
    a "Bartle! Yuckle borm mee harkle"

    menu:
        "What is going on":
            jump fruitStall
        "I think I might need to take some notes":
            jump translation

label fruitStall:
    $ progress = 3

    scene bg fruitStall # to be made

    show marketAlien talking at left # to be made
    # Hey! Hello! Just pick whatever you want
    ma "Zinky zoogle! Bartle! Zeeky horp beekyfooble markle"
    show alien talking at right # to be made
    # Hello! Me want apple"
    a "Bartle! Barkle feep"

    show marketAlien handingApple at left # to be made
    ma "feep!"
    #pause
    show marketAlien idle at left # to be made
    show alien withApple at right # to be made
    a "geekyduckle"

    menu:
        "uhh let's just keep going":
            jump groceryStore
        "I think I'm catching on":
            jump translation

label groceryStore:
    $ progress = 4

    scene bg groceryStore # to be made

    show groceryAlien talking at right # to be made
    #Hello! Just pick whatever you want
    ga "Bartle!  Zeeky horp beekyfooble markle"
    show alien talking at left # to be made
    #Hey! Me want diet coke
    a "Zinky zoogle! Barkle veepy"

    show groceryAlien handingCoke at right # to be made
    ga "veepy!"
    show alien withCoke at left # to be made
    a "geekyduckle"

    menu:
        "I still have no idea whats going on":
            jump printShop
        "Gotta take some notes":
            jump translation

label printShop:
    $ progress = 5

    scene bg printShop # to be made

    show photoAlien talking at left # to be made
    show alien idle at center # to be made
    show human idle at right # to be made
    # Just wondering, what you want?

    $ finalAnswer = renpy.input("Zeekybooble, vorp markle?")

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

label dictionary:
    # find a way to show all of the words that the player has already entered with options to edit
    # do this with a for loop
    # absolutely do this with a for loop
    # show one translation at a time 
    # mabye show each line as a menu with options

label finalScene:
    
    scene bg finalBG # to be made
    show aliens waving at truecenter # to be made
    a "BYEEEEEE"
    a "BYEEEEEEEEEE"
    a "farewell to all of you"
    # think about inserting more ending scene stuffs here