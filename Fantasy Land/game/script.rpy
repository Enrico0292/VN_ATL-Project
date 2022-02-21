# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miki")
define r= Character("Rin")
image miki:
    "miki1.png" with dissolve
    pause  1.0
    "mikic1.png" with dissolve
    pause 2.0
    repeat
image mikiescape:
    "mikic1.png"
    xalign 0.1 yalign 0.01
    linear 2.0 xalign 2.0
image rin:
    "rin1.png"
    xalign 0.1 yalign 0.01

   
image classroom:
    "Classroom.jpg"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene classroom
    show miki:
        xalign 0.1 yalign 0.01
    m "Hi, i'm Miki, and i'm a magical cat "
    hide miki
    
    show mikiescape
    m "Goodbye"
    
    scene  hallway1
    with fade
    show rin  with moveinleft
    r "Did you see Miki?"
    
    r "What  was that?" with vpunch
   
    show miki1:
         xalign 0.9 yalign 0.01
    with moveinright
    m "Are you looking for me?" 
    hide miki1
    show miki1:
         xalign 0.9 yalign 0.01
         ease .5 zoom 1.5 xoffset 100 yoffset 50
    m "Did you miss me?" 
    
    

    show  bc2
    play music  "audio/rubia.mp3"
    "Enjoy this image that i stole from Pixiv"

   



    return
