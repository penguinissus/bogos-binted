#GOAL IS I WILL NOT FIND ANY COMMENTS AT THE END AKA ALL THE TO DO MESSAGES

define h = Character("Human")
define a = Character("Alien")
define ma = Character("Market Alien") # I should change his name some time...

label start:

    $ ewords = ["zinky zoogle", "vorp", "zeeky", "booble"   , "zeekybooble"   , "beeble", "mee", "eep", "Forp", "zilk", "lort", "zort", "bartle", "yuckle", "birt", "corm", "harkle", "horp", "beekyfooble", "quarkle"]
    $ awords = ["hey"         , "what", "just" , "wondering", "just wondering", "if"    , "you", "got", "your", "is"  , "a"   , "is a", "hello" , "let"   , "me"  , "show", "around", "pick", "whatever"   , "want"]
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
    menu: 
        "Hey!"
            $ response1 = "ignores"
        "Zinky zoogle!"
            $ response1 = "greeting"
        "Vorp?"
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

    scene bg fruitStall # to be made
    # Hey! Hi! Just pick whatever you want
    ma "Zinky zoogle! Bartle! Zeeky horp beekyfooble markle"