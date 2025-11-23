define h = Character("Human")
define a = Character("Alien")

label start:

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
    elif response1 == "greeting":
        show alien talking at truecenter
        a ""
    elif response1 == "explanation":
        show alien talking at truecenter
        a ""