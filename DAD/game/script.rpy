# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dad = Character("D.A.D.")
define doki = Character("Dokibird")
define mint = Character("Maid Mint Fantôme")
define dooby = Character("Dooby")


# The game starts here.

label start:

    ############################# ACT 1 - Doki's House #####################################

    scene bg dokiroom
    
    dad "{i}It was a beautiful morning in Dokiville.{p}The sun was shining.{p}The birds were chirping."
    
    dad "{i}The smell of freshly baked dog treats wafted through the streets."
    
    show doki smile
    
    dad "{i}As Dokiville slowly awakens to another beautiful day, Dokibird prepares to start her stream."
    
    show doki happy

    doki "Hello Everybody! {p} Welcome to today\’s stream!"
    
    scene bg kitchen
    
    show dad smile
    
    dad "{i}As Doki is streaming, I hear the familiar sound of the postman’s motorbike rolling up to our mailbox."
    
    play sound "motorbike.mp3"
    
    hide dad smile with Dissolve(3.0)
    
    show dad newspaper with Dissolve(3.0)
    
    dad "{i}I returned with the newspaper and placed it down on the kitchen table."
    
    dad "{i}As I eat breakfast I look at the cover of the newspaper, and I notice something. {p}It\’s a job advertisement for Dooby\’s Pizza Place."

    dad "Hmmm... with Doki streaming all the time I don\’t have much to do, working at a pizza place sounds like fun."
    
    hide dad newspaper with Dissolve(3.0)

    ############################# ACT 2 - Dooby's Pizza #####################################

    bg pizzaplace with fade
    
    





    # This ends the game.

    return
