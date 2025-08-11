# The script of the game goes in this file.

# Character definitions

define dad = Character("D.A.D.")
define doki = Character("Dokibird")
define mint = Character("Maid Mint Fantôme")
define dooby = Character("Dooby")

#Transition and Transform definitions

define fadeslow = Fade(1.0, 2.0, 1.0)

transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    ############################# ACT 1 - Doki's House #####################################

    scene bg dokiroom with fade
    
    dad "{i}It was a beautiful morning in Dokiville.{p}The sun was shining.{p}The birds were chirping."

    dad "{i}The smell of freshly baked dog treats wafted through the streets."
    
    show doki smile
    
    dad "{i}As Dokiville slowly awakens to another beautiful day, Dokibird prepares to start her stream."
    
    show doki happy

    doki "Hello Everybody!{p}Welcome to today\'s stream!"
    
    scene bg kitchen with fade
    
    show dad smile
    
    dad "{i}As Doki is streaming, I hear the familiar sound of the postman’\'s motorbike rolling up to our mailbox."
    
    play sound "motorbike.mp3"
    
    hide dad smile with Dissolve(2.0)
    
    show dad newspaper with Dissolve(2.0)
    
    dad "{i}I returned with the newspaper and placed it down on the kitchen table."
    
    dad "{i}As I eat breakfast I look at the cover of the newspaper, and I notice something. {p}It\'s a job advertisement for Dooby\'s Pizza Place."

    dad "Hmmm... with Doki streaming all the time I don\'t have much to do, working at a pizza place sounds like fun."
    
    hide dad newspaper with Dissolve(2.5)

    ############################# ACT 2 - Dooby's Pizza Express #####################################

    scene bg pizzaplace with fadeslow
    
    show dad smile with Dissolve(2.0)
    
    dad "{i}Somehow i got the interview that morning so i headed over, everyone was patting me it was like they never saw a dog before!"
  
    show dad smile at slightleft with Dissolve(2.0) 
    show dooby happy at slightright with Dissolve(2.0) 
  
    dooby "Well, I\'m very impressed with your resume, I\'m happy to offer you a position at my pizza place!"

    dooby "I\'m glad you showed up today, there haven\'t been many good candidates today."

    show dooby smile
    show dad happy
    
    dad "I would love to work here, thank you for accepting me."
    
    show dad smile
    show dooby happy
    
    dooby "You\'re welcome, you are already very popular with the others, so I\'m sure that you\'ll do great."
    
    dooby "All the stuff you need is on the counter. We have a busy day ahead of us, there will be many hungry customers."
    
    dooby "Make sure you do your best!"
    
    show dooby smile
    show dad happy
    
    dad "I certainly will! You can count on me!"
    
    scene bg pizzaplace with fadeslow

    # This ends the game.

    return
