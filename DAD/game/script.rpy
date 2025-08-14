# The script of the game goes in this file.

# Character definitions

define dad = Character("D.A.D.")
define doki = Character("Dokibird")
define mint = Character("Maid Mint Fantôme")
define dooby = Character("Manager Dooby")
define chibi = Character("CEO Chibidoki")
define saryah = Character("Labour Unit Saryah")
define pancake = Character("Labour Unit Pancake")
define bitsy = Character("Labour Unit Bitsy")
define gil = Character("Labour Unit Gil")
define nic = Character("Labour Unit Nic")
define everyone = Character("Everyone")
define lucy = Character("Coordinator Lucy Pyre")
define comm1 = Character("Commentator Mike")
define comm2 = Character("Commentator Mick")
define nimi = Character("Hostess Nightmare Nimi")

#Transition and Transform definitions

define fadeslow = Fade(1.0, 2.0, 1.0)

transform centre:
    xalign 0.5
    yalign 0.3 
    
transform slightleft:
    xalign 0.05
    yalign 0.5
    zoom 0.80
    
transform slightright:
    xalign 0.90
    yalign 0.5

# The game starts here.

label start:

    ############################# ACT 1 - Doki's House #####################################

    scene bg dokiroom with fade
    
    dad "{i}It was a beautiful morning in Dokiville.{p}The sun was shining.{p}The birds were chirping."
    dad "{i}The smell of freshly baked dog treats wafted through the streets."
    
    show doki smile at centre
    
    dad "{i}As Dokiville slowly awakens to another beautiful day, Dokibird prepares to start her stream."
    
    show doki happy at centre

    doki "Hello Everybody!{p}Welcome to today\'s stream!"
    
    scene bg kitchen with fade
     
    show dad smile at centre
    
    dad "{i}As Doki is streaming, I hear the familiar sound of the postman\'s motorbike rolling up to our mailbox."
    
    play sound "motorbike.mp3"
    
    hide dad smile at centre with Dissolve(2.0)
    
    show dad newspaper with Dissolve(2.0)
    
    dad "{i}I returned with the newspaper and placed it down on the kitchen table."
    dad "{i}As I eat breakfast I look at the cover of the newspaper, and I notice something. {p}It\'s a job advertisement for Dooby\'s Pizza Express."
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
    
    show mint happy at slightright with Dissolve(2.0)
    
    mint "Thank you for coming! Hope you enjoyed your food! Come back soon!"
    
    show dad smile at slightleft with Dissolve(1.0)
    
    mint "Oh wow D.A.D. that was our 100th customer of the day, that was a lot of work!"
    mint "I\'m glad you are here D.A.D, without you this would have been exhausting!"
    mint "I can see why Dooby hired you, you are a really good worker!"
    
    show dad happy
    show mint smile
    
    dad "*Mouth full of pizza* *Munching sounds*"
    dad "Mmmmmmmmm. {w}Working at a pizza place is really fun! {w}The pizza here is so delicious!"
    dad "Plus you get free pizza too!  ... This is free right?"
    
    show dad smile
    show mint happy
    
    mint "Haha! I\'m glad you like the pizza!"
    mint "And no, it's not free, you will need to pay in full, in the form of 10 mandatory pats per slice."
    mint "Oh yeah, Dooby wants to see you in her office. {w}Its nothing bad she said, she has something special she wants to tell you."

    show dad happy
    show mint smile
    
    dad "Ok, I\'ll be right there!"
    
    ############################# ACT 3 - Pizza Express Management #####################################

    scene office with fadeslow
    
    show dad worried at slightleft with Dissolve(2.0)
    
    dad "{i}I enter the office worried I did something wrong."
    
    show dooby happy at slightright with Dissolve(2.0)
    
    dooby "No need to worry about anything you haven\'t done anything wrong, in fact you’ve done better than ever!"
    dooby "I want to promote you to manager!"
    
    show dooby smile with vpunch
    
    dad "Wait... how, where, who, why, when, also what? I just ate pizza!?"
    
    show dooby happy
    
    dooby "I mean quality control is one of the traits of a good manager."
    
    show dad happy
    show dooby smile
    
    dad "If that\'s the case... when do I start?"

    show dad smile
    show dooby happy

    dooby "{b}{size=+15}Right now!{/size}{/b} {w}I\'ve already let corporate know and I\'ve put a dog-sized suit in the back office where you\'ll be working from. {w}Good luck and make sure to work well!"
    dooby "Alright, I\'mma peace out, time to work on my tan!"
    
    show dad smile
    show dooby smile
    
    dad "{i}I see Dooby slide on some shades and throw a towel onto her shoulder."
    
    hide dooby with Dissolve(2.5)
    show dad happy
    
    dad "Huh? Ok I guess I\'m in charge now. Better get to it"
    
    scene office with fadeslow
    
    show dad suitsmile at slightleft with Dissolve(2.0)
    
    dad "{i}I made myself comfortable clicked around the computer and I ended up scrolling through LeashedIn."
    dad "{i}A notification reminder popped up for a management meeting in Xoom starting in a few minutes."
    dad "{i}It was pretty difficult to use the human mouse with my paws but I got it figured out in the end."
    
    play sound "xoomjoin.mp3"
    
    show chibi happy at slightright with Dissolve(0.5)
    
    chibi "Thank you everyone for coming to our financial meeting for this quarter."
    chibi "Before we get started, I would like to extend a warm welcome to D.A.D. who has just joined the team recently and also congratulations on your recent promotion."
    
    show chibi smile

    gil "Welcome D.A.D.! {w}My condolences on your promotion! {w}As a fellow manager of 10 years, I regret every moment of it :D"
    gil "Die Zeiten hier sind absolut gottlos."
    
    bitsy "{color=#0000ff}Yeah congrats! {/color}{color=#ff0000}Welcome to the team!{/color}"
    bitsy "{color=#0000ff}I can recommend some great cardboard boxes to nap in if you would like! {/color}{color=#ff0000}The Metalle Cardbox Pro Max 15 with extra padding, built in tv and sound system, snack holder, drink holder, and treat dispenser!{/color}"
    
    show dad suithappy

    dad "Thanks everyone, I’m happy to be part of the team! Turns out working at a Pizza Express franchise is really fun!"
    
    show dad suitsmile
    
    gil "Hach der jugendliche Leichtsinn."
    
    show chibi happy
    
    chibi "Okay, now to business."
    chibi "Sales are up 18.7\% percent over the past quarter, {w}revenue up by 12\%, profit up by 10\% {w}and most importantly our average customer satisfaction rating has increased to 99.7\% which is really good!"
    
    show chibi smile
    show dad suithappy
    
    dad "Yay!"
    
    show dad suitsmile
    show chibi happy
    
    chibi "Oh also our operating equipment downtime is also down by 15\% as well. {w}In saying that I would like to thank our maintenance crew and their magnificent and deeply valued efforts helping keep our Pizza Express locations running!"

    show chibi smile
    show dad suithappy
    
    dad "Woof! Maintenance for the win!"
    
    show dad suitsmile
    show chibi happy
    
    chibi "Woof indeed! In other news, we are set for a 4\% salary increase to keep ahead of inflation as well as bonuses to be handed out to all employees."
    chibi "So I would like to say well done to everyone, you have all done really well!"

    play sound "applauseandwoof.mp3"
    
    chibi "Additionally, since our new equipment arrived our equipment downtime has made the coffee machines much more reliable which is good."
    
    show chibi smile
    
    nic "That’s good to hear, the coffee machines have been working… erratically for a bit now. {w}I need my coffee! {w}You don’t want to see me without my coffee."

    show chibi happy
    
    chibi "Yeah those machines were awful, I took the pleasure of getting the best machines on the market this time."

    show chibi smile
    show dad suithappy

    dad "I do have a question to ask if I may?"
    
    show dad suitsmile
    show chibi happy
    
    chibi "Certainly D.A.D.! What is your question?"

    show chibi smile
    show dad suithappy

    dad "Will there be dog treats supplied as part of employee amenities going forwards?"
    
    show dad suitsmile
    show chibi happy

    chibi "We currently don’t have dog treats being supplied as part of employee amenities, but we will certainly look into it! {w}I’ll make sure personally that the highest quality of dog food is made available to our employees!"
    
    show chibi smile
    
    pancake "{cps=50}As Chief Catering Manager, I will require Requisition Form 12A {cps=60}filled out in quadruplicate with alternating letters in italics and bold, {cps=70}the Provision Permission Slip filled out triplicate in {cps=80}blue, red, and deep purple ink and {cps=90}a digital copy with each letter in a{w=0.10}{nw}" 
    pancake "{cps=100}randomly chosen font, the Workplace Hygiene Form {cps=105}filled out using a quill and ink, the Food Safety & Handling Certificate {cps=110}stamped, and verified by a JP, signed and seasoned with the finest Himalayan sea salt, {cps=120}a Valid Permit for the Request of Permits filled out{w=0.10}{nw}"
    pancake "{cps=130}in a mix of Gaelic and Flat German, {cps=140}the Proof of Edibility Authenticity Certificate {cps=150}typed up using a vintage typewriter, specifically a Olivetti Lettera 32 version a5x {cps=10}aaaand... {cps=160}the updated version of the Food Safety Matrix on my desk by yesterday at sundown."

    gil "Oh also, as acting Chief Legal Coordinator all actions must also be in full compliance with how"
    gil "{cps=140}Article 14 Section 9 Subsection 15 Paragraph 5, Article 17 Section 15 Subsection 21 Paragraphs 7 and 10, Article 23 Section 7 Subsection 29 Paragraph 4, Sections 15, 16, 17, and 21 of the Food Safety Handling Act and the Law Compliance {cps=10}Simplification Act." 
    gil "Welcher, ironischerweise, alles 10 mal komplizierter macht."
    
    show dad suithappy
    
    dad "Uhhhhhhhhhhhhhhhhhhhhhhhhhh. Okay… where can I get the salt from?"
    
    show dad suitsmile
    
    nic "The Himalayas. Duh."
    
    pancake "{cps=140}And can I have all of those forms delivered on the back of a medieval warhorse thanks."
    
    show chibi happy
    
    chibi "Anything other business from the floor?"

    show chibi smile
    
    saryah "I was actually going to ask about whether my custom submission for a new Pizza Express recipe has been approved?"
    
    show chibi happy
        
    chibi "Ah, remind me what that was again?"
    
    show chibi smile
    
    saryah "A mouth-watering, {w}delicious, {w}Aussie meatlovers {w}with pineapple {w}and beetroot. {w}On focaccia. {w}Cheeseless."
    
    chibi "..."
    gil "..."
    bitsy "..."
    nic "..."
    pancake "..."
    dad "..."
    
    saryah "The trick is to use tomato paste instead of water in the focaccia dough."
    
    everyone "{cps=1}..."
    
    show dad suithappy
    
    dad "That sounds delicious! Can we add liver?"

    show dad suitsmile
    show chibi happy
    
    chibi "Alright, moving on. If that is all, let’s proceed with the rest of the meeting."
    
    scene office with fadeslow
    
    show chibi happy with Dissolve(2.0)
    
    chibi "And that concludes the meeting, I must say you were extremely professional D.A.D., we are very lucky to have such a wonderful dog like you on our team."

    dad "{i}I just nod in agreement pretending to know what i’m doing."
    
    chibi "Actually… {w}There was something I was going to offer to Dooby but she’s not here today for some reason…"
    
    dad "{i}I wonder why."
    
    chibi "so D.A.D., you can have it instead. It\'s a free ticket to some pro tournament for something, I don't know what it\'s about."
    
    show dad suithappy
    show chibi smile
    
    dad "Oh nice awesome that\'s great, when is it?"

    show dad suithappy
    show chibi smile
    
    chibi "Like in half an hour. You better get going!"
    chibi "Oh the event organisers sent a free mystery merch coupon you can pick it up at check-in."
    
    ############################# ACT 4 - Pro Gaming Tournament #####################################
    
    scene progameoutside with fadeslow
    
    show dad smile with Dissolve(2.0)
    
    dad "{i}I get to the tournament a few minutes before the event started. I\'m not sure who\'s playing or even what game they\'re playing, but I don\'t know what to do as a manager, so I guess I\'ll do this."
    dad "{i}I figure I should get into the spirit of thing so, I pull on the free player jersey I got in my mystery box at the merch counter."
    dad "{i}It looks a little different to everyone else\'s... hmmm I guess that's why it\'s a \"mystery\" box."
    
    show lucy stressedtalking
    
    lucy "Where the fuck were you?! We'\ve been looking all over for you! You\'re meant to be playing in a few minutes!"
    
    show lucy stressed
    show dad worriedtalking
    
    dad "What do you mean? I\'m just here as a vie-"
    dad "{i}Before i’m able to finish my sentence she drags me by my collar into the arena."
    dad "Wait a secon-"
    
    lucy "You wait a second, you gotta have some balls to show up so late in the finals! Do you know how long I\'ve been running around looking for you? People are waiting to see you live!"

    dad "{i}I realise that there\'s no arguing with this woman, so I just go along with her, as my attempt to break away fails. {w} I try to follow as best I can."
    
    scene progameinside with fadeslow
    
    comm1 "{cps=100}Let me tell you something Mick, i don\'t know where this dog came from but he\'s won every fight solo!"
    
    comm2 "{cps=100}A better question is, Mike, why he didn\'t have a team beside him? Does he not have a team? Is he here by mistake? But at the end of the day it doesn\'t really matter because he\'s DOMINATED the competition every, single, fight!"

    dad "{i}I had no clue what the commentators were talking about, I\'ve never played the game before, but I guess I'm a natural. Maybe all those hours of watching Doki play helped me somehow."
    
    comm1 "Well regardless of what happened, D.A.D. is now going straight to the international competition! Let\'s have a big round of applause!"
    
    play sound "applause.mp3"
    
    scene plane with fadeslow
    
    show dad smile
    
    dad "{i}I end up on a plane to the international tournament, I didn\'t particularly want to play more, but anything beats the boredom doing nothing at home. At least it\'s only a short flight."
    
    show nimi smile
       
    dad "{i}Some time after the flight starts, a flight attendant comes over."
    
    show nimi happy
    
    nimi "Hi there, would you like anything today?"
    
    
    
    
    # This ends the game.

    return
