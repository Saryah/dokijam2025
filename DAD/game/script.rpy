# The script of the game goes in this file.

# Character definitions

define dad = Character("D.A.D.", who_color="#e9a30d")
define doki = Character("Dokibird", who_color="#b6a9fe")
define chat = Character("Chat", who_color="#FFFFFF")
define mint = Character("Maid Mint Fantôme", who_color="#a2f4c5")
define dooby = Character("Manager Dooby", who_color="#4e6f89")
define chibi = Character("CEO Chibidoki", who_color="#e6aacf")
define saryah = Character("Labour Unit Saryah", who_color="#05878a")
define pancake = Character("Labour Unit Pancake", who_color="#E0BA1C")
define bitsy = Character("Labour Unit Bitsy", who_color="#0013FF")
define gil = Character("Labour Unit Gil", who_color="#c87763")
define nic = Character("Labour Unit Nic", who_color="#F63A37")
define everyone = Character("Everyone", who_color="#FFFFFF")
define lucy = Character("Coordinator Lucy Pyre", who_color="#e7e5f2")
define comm1 = Character("Commentator Mike", who_color="#FFFFFF")
define comm2 = Character("Commentator Mick", who_color="#FFFFFF")
define nimi = Character("Hostess Nimi Nightmare", who_color="#b2c6e4")
define radio = Character("Mysterious Radio Voice", who_color="#FFFFFF")
define bao = Character("Rocket Scientist Bao the Whale", who_color="#b2c6e4")
define dragoonengi = Character("Dragoon Engineer", who_color="#fee5ad")
define neuro = Character("President Neuro-sama", who_color="#6ce0d8")
define dragoonassist = Character("Dragoon Assistant", who_color="#fee5ad")

#Transition and Transform definitions

define charfade = Dissolve(1.5)

define fadeslow = Fade(1.0, 2.0, 1.0)

transform centre:
    xalign 0.5
    yalign 0.5
    zoom 0.75
    
transform slightleft:
    xalign 0.15
    yalign 0.5
    zoom 0.75
    
transform slightright:
    xalign 0.85
    yalign 0.5
    zoom 0.75
    
transform dokicentre:
    xalign 0.5
    yalign 0.3
    zoom 1.1
    
transform dragooncentre:
    xalign 0.6
    yalign 0.3
    zoom 0.75

# The game starts here.
label start:
    play music "Vtuber_game_with_fake_whale_v2.mp3" loop fadein 1.0 fadeout 1.0

    ############################# ACT 1 - Doki's House #####################################

    scene bg dokiroom with fade
    
    dad "{i}It was a beautiful morning in Dokiville.{p}The sun was shining.{p}The birds were chirping."
    dad "{i}The smell of freshly baked dog treats wafted through the streets."
    
    show doki smile at dokicentre
    
    dad "{i}As Dokiville slowly awakens to another beautiful day, Dokibird prepares to start her stream."
    
    show doki happy at dokicentre

    doki "Hello everybody!{p}Welcome to today\'s stream!"
    
    chat "Hi Doki{nw=0.5}"
    chat "Hello Doki{nw=0.5}"
    chat "Where\'s Dokikitty?{nw=0.5}"
    chat "May we has loop?{nw=0.5}"
    chat "👏👏👏{nw=0.5}"
    chat "DO DO DO..DODODO DOKI DO DO DO DODOD DOKI{nw=0.5}"
    chat "🎸🎸🎸🎸🎸🎸{nw=0.5}"
    chat "🎸🎼🎶🎵🎶{nw=0.5}"
    chat "Zen is literally playing Peak right now lol{nw=0.6}"
    chat "Heeeeey{nw=0.5}"
    chat "hello dokster{nw=0.5}"
    chat "Hell yea good timing. just got out of work"
    
    
    scene bg kitchen with fade
     
    show dad smile at centre
    
    play sound "motorbike.mp3"
    
    dad "{i}As Doki is streaming, I hear the familiar sound of the postman\'s motorbike rolling up to our mailbox."
    
    hide dad smile at centre with charfade
    pause 1.5
    show dad newspaper at centre with charfade
    
    dad "{i}I returned with the newspaper and placed it down on the kitchen table."
    dad "{i}As I eat breakfast I look at the cover of the newspaper, and I notice something. {p}It\'s a job advertisement for Dooby\'s Pizza Express."
    dad "Hmmm... With Doki streaming all the time I don\'t have much to do. Working at a pizza place sounds like fun."

    ############################# ACT 2 - Dooby's Pizza Express #####################################

    scene bg pizzaplace with fadeslow
    
    show dad smile at centre with charfade
    
    dad "{i}Somehow I got the interview that morning so I headed over. Everyone was patting me, it was like they never saw a dog before!"
  
    show dad smile: 
        linear 0.5 xpos 0.25
    show dooby happy at slightright with charfade 
  
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
    
    show mint happy at slightright with charfade
    
    mint "Thank you for coming! Hope you enjoyed your food! Come back soon!"
    
    show dad smile at slightleft with charfade
    
    mint "Oh wow D.A.D. that was our 100th customer of the day, that was a lot of work!"
    mint "I\'m glad you are here D.A.D, without you this would have been exhausting!"
    mint "I can see why Dooby hired you, you are a really good worker!"
    
    show dad happy
    show mint smile
    
    dad "*Mouth full of pizza* *Munching sounds*"
    dad "Mmmmmmmmm. {w}Working at a pizza place is really fun! {w}The pizza here is so delicious!"
    dad "Plus you get free pizza too! {w}... {w}This is free right?"
    
    show dad smile
    show mint happy
    
    mint "Haha! I\'m glad you like the pizza!"
    mint "And no, it's not free, you will need to pay in full, in the form of 10 mandatory pats per slice."
    mint "Oh yeah, Dooby wants to see you in her office. {w}Its nothing bad she said, she has something special she wants to tell you."

    show dad happy
    show mint smile
    
    dad "Ok, I\'ll be right there!"
    
    ############################# ACT 3 - Pizza Express Management #####################################

    scene bg office with fadeslow
    
    show dad worried at slightleft with charfade
    
    dad "{i}I enter the office worried I did something wrong."
    
    show dooby happy at slightright with charfade
    
    dooby "No need to worry about anything you haven\'t done anything wrong, in fact you’ve done better than ever!"
    dooby "I want to promote you to manager!"
    
    show dooby smile with vpunch
    
    dad "Wait... How, where, who, why, when, also what? I just ate pizza!?"
    
    show dooby happy
    
    dooby "I mean quality control is one of the traits of a good manager."
    
    show dad happy
    show dooby smile
    
    dad "If that\'s the case... When do I start?"

    show dad smile
    show dooby happy

    dooby "{b}{size=+15}Right now!{/size}{/b} {w}I\'ve already let corporate know and I\'ve put a dog-sized suit in the back office where you\'ll be working from. {w}Good luck and make sure to work well!"
    dooby "Alright, I\'mma peace out, time to work on my tan!"
    
    show dad smile
    show dooby smile
    
    dad "{i}I see Dooby slide on some shades and throw a towel onto her shoulder."
    
    hide dooby with Dissolve(2.5)
    show dad happy
    
    dad "Huh? Ok I guess I\'m in charge now. Better get to it!"
    
    scene bg office with fadeslow
    
    show dad suitsmile at slightleft with charfade
    
    dad "{i}I made myself comfortable clicked around the computer and I ended up scrolling through Leashed-In."
    dad "{i}A notification reminder popped up for a management meeting in Xoom starting in a few minutes."
    dad "{i}It\'s normally pretty difficult for me to use a human mouse, but I took out my pawdapter I always carry with me, and attached it, joining the meeting without issue."
    
    play sound "xoomjoin.mp3"
    
    show chibi happy at slightright with charfade
    
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
    play sound "clapmediumwithwoof.mp3"
    chibi "So I would like to say well done to everyone, you have all done really well!"
    
    chibi "Additionally, since our new equipment arrived our equipment downtime has made the coffee machines much more reliable which is good."
    
    show chibi smile
    
    nic "That’s good to hear, the coffee machines have been working... erratically for a bit now. {w}I need my coffee! {w}You don’t want to see me without my coffee."

    show chibi happy
    
    chibi "Yeah those machines were awful, I took the pleasure of getting the best machines on the market this time."

    show chibi smile
    show dad suithappy

    dad "I have a question to ask, if I may?"
    
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
    pancake "{cps=130}in a mix of Gaelic and Flat German, {cps=140}the Proof of Edibility Authenticity Certificate {cps=150}typed up using a vintage typewriter, specifically a Olivetti Lettera 32 version a5x {cps=10}aaaand... {cps=160}The updated version of the Food Safety Matrix on my desk by yesterday at sundown."

    gil "Oh also, as acting Chief Legal Coordinator all actions must also be in full compliance with how"
    gil "{cps=140}Article 14 Section 9 Subsection 15 Paragraph 5, Article 17 Section 15 Subsection 21 Paragraphs 7 and 10, Article 23 Section 7 Subsection 29 Paragraph 4, Sections 15, 16, 17, and 21 of the Food Safety Handling Act and the Law Compliance {cps=10}Simplification Act." 
    gil "Welcher, ironischerweise, alles 10 mal komplizierter macht."
    
    show dad suithappy
    
    dad "Uhhhhhhhhhhhhhhhhhhhhhhhhhh. Okay... where can I get the salt from?"
    
    show dad suitsmile
    
    nic "The Himalayas. Duh."
    
    pancake "{cps=140}And can I have all of those forms delivered on the back of a medieval warhorse thanks."
    
    show chibi happy
    
    chibi "Any other business from the floor?"

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
    
    scene bg office with fadeslow
    
    show chibi happy at slightright with charfade
    
    chibi "And that concludes the meeting, I must say you were extremely professional D.A.D., we are very lucky to have such a wonderful dog like you on our team."

    show dad suitsmile at slightleft with charfade 

    dad "{i}I just nod in agreement pretending to know what i’m doing."
    
    chibi "Actually... {w}There was something I was going to offer to Dooby but she’s not here today for some reason..."
    
    dad "{i}I wonder why."
    
    chibi "so D.A.D., you can have it instead. It\'s a free ticket to some pro tournament for something, I don't know what it\'s about."
    
    show dad suithappy
    show chibi smile
    
    dad "Oh nice awesome that\'s great, when is it?"

    show dad suitsmile  
    show chibi happy
    
    chibi "Like in half an hour. You better get going!"
    chibi "Oh the event organisers sent a free mystery merch coupon you can pick it up at check-in."
    
    ############################# ACT 4 - Pro Gaming Tournament #####################################
    
    scene bg progameoutside with fadeslow
    
    show dad jerseysmile at slightleft with charfade
    
    dad "{i}I get to the tournament a few minutes before the event started. I\'m not sure who\'s playing or even what game they\'re playing, but I don\'t know what to do as a manager, so I guess I\'ll do this."
    dad "{i}I figure I should get into the spirit of thing so, I pull on the free player jersey I got in my mystery box at the merch counter."
    dad "{i}It looks a little different to everyone else\'s... hmmm I guess that's why it\'s a \"mystery\" box."
    
    show lucy stressedtalking at slightright  with charfade
    
    lucy "{size=+15}Where the fuck were you?!{/size} We\'ve been looking all over for you! You\'re meant to be playing in a few minutes!"
    
    show lucy stressed
    show dad jerseytalking
    
    dad "What do you mean? I\'m just here as a vie-"
    dad "{i}Before i’m able to finish my sentence she drags me by my collar into the arena."
    dad "Wait a secon-"
    
    show lucy stressedtalking
    show dad jerseysmile
    
    lucy "{size=+15}You {/size}wait a second, you gotta have some balls to show up so late in the finals! Do you know how long I\'ve been running around looking for you? {size=+15}People are waiting to see you live!"

    dad "{i}I realise that there\'s no arguing with this woman, so I just go along with her, as my attempt to break away fails. {w} I try to follow as best I can."
    
    scene bg progameinside with fadeslow
    
    show dad jerseysmile at centre with charfade
    
    play sound "clapbig1.mp3"
    
    comm1 "{cps=100}Let me tell you something Mick, i don\'t know where this dog came from but he\'s won every fight solo!"
    
    comm2 "{cps=100}A better question is, Mike, why he didn\'t have a team beside him? Does he not have a team? Is he here by mistake? But at the end of the day it doesn\'t really matter because he\'s DOMINATED the competition every, single, fight!"

    dad "{i}I have no clue what the commentators are talking about, I\'ve never played the game before, but I guess I'm a natural. Maybe all those hours of watching Doki play helped me somehow."
    
    comm1 "{cps=100}Well regardless of what happened, D.A.D. is now going straight to the international competition! Let\'s have a big round of applause!"
 
    play sound "clapbig2.mp3"
    
    scene bg plane with fadeslow
    
    show dad smile at slightleft with charfade
    
    dad "{i}I end up on a plane to the international tournament, I didn\'t particularly want to play more, but anything beats the boredom of doing nothing at home. At least it\'s only a short flight."
    
    show nimi smile at slightright with charfade
       
    dad "{i}Some time after the flight starts, a flight attendant comes over."
    
    show nimi happy
    
    nimi "Hi there, would you like anything today?"
    
    show dad happy
    show nimi smile
    
    dad "No thanks, I'\m all good."
    
    show dad smile
    show nimi happy
    
    nimi "No worries, enjoy your flight!"
    
    show nimi smile:
        linear 2.8 xpos -0.2

    dad "{i}She smiles at me and walks off."
    dad "{i}I watch as she walks into the captains quarters to see if they want anything, then run back out looking panicked but still remaining calm."
    
    show nimi worriedtalking:
        linear 1.3 xpos 0.9
     
    dad "{i}As I watch and strain my neck to see what was happening, I couldn\'t help but feel that the plane was in a slight diving bank, but as we only left the airport a short while ago we couldn\'t have already begun descending for landing."

    nimi "Does anyone know how to fly a plane? Not to panic anyone, but both of the pilots have passed out and it's my first day!"
    
    show nimi worried
    
    dad "{i}I look around to see if anyone responds, but it seems that everyone else is in deep sleep with no sign of waking up."
    dad "{i}I’ve played flight simulator while Doki was away so I think I probably know how to, besides nobody else seems to be awake to take over anyway."
    
    show dad worriedtalking
    
    dad "{i}Uhh hi, I might be able to help."
    
    show dad worried
    show nimi worriedtalking
    
    nimi "But... But... How... You\'re a dog? How can you fly...?"
    
    show dad worriedtalking
    show nimi worried
    
    dad "I've played my fair share of flight simulators."
    
    show dad worried
    
    dad "{i}Shimmying past her in the aisle, I make my way towards the cockpit."
    
    scene bg planecockpit with fadeslow
    
    show rin sleep at slightleft
    show lime sleep at slightright

    show dad worried at centre with charfade

    dad "{i}I enter the cockpit and see two women in pilot uniform passed out, and... a snail sitting on the shoulder of one of them?"
    dad "{i}I jump on the lap of the woman who appears to be the main pilot and look at the controls in front of me."
    
    show dad worriedtalking
    
    dad "Oh my gosh, this is way more complicated than mouse and keyboard!"

    show dad worried

    dad "{i}I start to panic, but then I see a big red button on the yolk."
    dad "{i}I don\'t know what it does but, it\'s sure to do something."
    dad "{i}So I boop it. {w}I feel the plane begin to level out of its dive."
    
    show nimi happy behind dad with charfade :
        xalign 0.7
        yalign 0.5
        zoom 0.75
    
    nimi "Oh wow! Nicely done D.A.D.!"
    
    dad "{i}After I pressed the button I grabbed the controls and tried to steer. I seem to be keeping the plane in the air at the very least so I keep doing that."
    
    nimi "Well D.A.D., you keep doing what you’re doing here, I need to go back to my station in case any passengers need help. I\'m not sure why none of them have woken up at all."
    
    hide nimi with charfade
    
    dad "{i}I just nod, eyes fixed on what's I think is the plane\'s spirit level, and keeping it steady.  Occasionally, I check my position on the map on one of the screens and follow the big red line, hoping it\'s taking us to our destination."

    scene bg planecockpit with fadeslow
    
    show dad worried at centre
    show rin sleep at slightleft
    show lime sleep at slightright

    dad "{i}After what seemed like ages, I suddenly realise I don\'t remember how to land a plane and the pilots are still passed out."
    
    show dad worriedtalking
    
    dad "Oh dear! Oh dear! What do I do???"
    
    dad "{i}I hastily look around the cockpit again and notice that the two women are both wearing gaming headsets or something. {w}I\'ve seen Doki wear something like it in her streams so I pluck the thing off one of the women\'s head and put it on."
    
    show dad headset
   
    dad "{i} I immediately hear the very panicked voice of a human shouting into the mic."
    
    radio "DOKIWINGS FLIGHT 5248 COME IN. I REPEAT. DOKIWINGS FLIGHT 5248 COME IN. THIS IS AIR TRAFFIC CONTROL. PLEASE. IS ANYONE THERE."
    
    show dad headsettalking
    
    dad "Geez calm down, I’m here whats up? Whats an air trafficky controller thingy. Is that food?"
    
    show dad headset
    
    radio "CALM DOWN!? {w}YOU WERE DIVING TOWARDS THE GROUND EARLIER!!! {w}HOW CAN ANYONE REMAIN CALM IN THIS SITUATION??? {w}Thank god someone responded, I thought the plane was going to crash!!! {w}What in the name of Dokiville is going on???"

    show dad headsettalking
        
    dad "Wellllll... the flying people passed out and I pressed some buttons and fiddled around with the stick thing and the plane flew itself! Fascinating stuff this all is, a lot more exciting than the simulator stuff on the computer."
    
    show dad headset
    
    radio "Wait, who are you??? What are you doing in the cockpit!? What do you want? Don\'t crash the plane!!!"
    
    show dad headsettalking
    
    dad "Chill out, I’m not gonna crash the plane. {w}I’m D.A.D, I’m a dog."
    dad "I was on the plane and the food-serving human came around saying that there was an emergency because the flying people passed out and there was no one able to fly the plane because everyone else was asleep."
    
    show dad headset
    
    radio "W- w- w- what??? H- h- h- How? Y- you know what, forget I asked, do you know how to land the plane? The plane only has so much fuel and if you don\'t land soon, it\'ll crash and you\'ll all be pancakes!"
    
    show dad headsettalking
    
    dad "Ooh nom nom nom panacakes... *cough* wait... What do you mean fuel? I thought the plane just ran on plane energy or wind or something?"
    
    show dad headset
    
    radio "If you don\'t do something the plane is going to crash. So listen to me and listen carefully. I\'ll explain how to fly the plane. You said you\'ve been in a simulator before right?"
    
    show dad headsettalking
    
    dad "Uhhh a little bit I guess."
    
    show dad headset
    
    radio "So do you know how to use the autopilot feature and the flaps and throttle and all that stuff?"

    show dad headsettalking

    dad "Wut..."
    
    show dad headset
    
    radio "Well this is going to be difficult. Is the autopilot on? It should be a red button on the stick thing in front of you."
    
    show dad headsettalking
    
    dad "I think it is? I pressed it earlier and the plane just flew straight."
    
    show dad headset
    
    radio "Ok very good, I need you to find a knob labelled direction heading, {w}{cps=20}d-i-r-e-c-t-i-o-n h-e-a-d-i-n-g {cps=0}and turn it to 330 degrees. {w}It should be in front of you. I have you on radar, I\'ll vector you in."

    show dad headsettalking

    dad "The knobbly thing that I can barely turn with my paws?"
    
    radio "Yup, that’ll be it."
    
    show dad headsettalking

    dad "Uhhh ok got it."
    
    show dad headset
    
    radio "Ok, I\'ll walk you through how to slow down the plane and activate all the stuff it needs to land."
    
    scene bg explain with fade
    pause 2.0
    scene bg planecockpit with fade 
    
    show dad headsettalking at centre
    show rin sleep at slightleft
    show lime sleep at slightright
    
    dad "Wait, I see the airport in the distance I think! There's a bunch of lights."
    
    show dad headset
    
    radio "Alright good, you\'re doing really well D.A.D, I\'m proud of you. Let\'s bring this plane home."
    
    show dad headsettalking
    
    dad "Planes have homes?"
    
    show dad headset
    
    radio "Yep that\'s what an airport is basically. {w}Now you need to fully extend the flaps like we\'ve done before, and slow down the plane a bit more. {w}Keep on course descending for the runway."
    
    show dad headsettalking
    
    dad "Crap this is terrifying."
    
    show dad headset
    
    radio "You\'re doing good, keep focused."
    radio "In a moment, just before the plane touches down I need you to pull back on the yolk slightly and then pull the throttle all the way back. {w}You need to flare to slow down the plane\'s descent otherwise you\'ll slam the plane into the ground."
    
    show dad headsettalking
    
    dad "Ok, I\'ve got this I think."
    
    show dad headset
    
    radio "You\'re nearly here, I\'ve got emergency services on standby."
    
    dad "{i}I manage to land the plane and we eventually come to a stop."
    
    show dad headset
    
    radio "Nice! That was an awesome landing, well done D.A.D.! You saved everyone and the plane! We\'re all cheering for you in the tower."
    
    scene bg planetarmac with fadeslow
    
    show bao happy at slightright
    show dad smile at slightleft 
    with charfade
    
    bao "I just saw what happened - that was amazing! How would you like a tour of NASA and to watch the rocket launch this afternoon?"
    
    show dad happy
    show bao smile
    
    dad "Sure, why not? Sounds cool."
    
    show bao happy
    show dad smile
    
    bao "Awesome! Let’s go now!"
    
    scene bg nasarocket with fadeslow
    
    show bao happy at slightright
    show dad smile at slightleft
    with charfade
    
    bao "Here we are! Behold... The Doki 5 rocket!" 
    
    show dad happy
    show bao smile
    
    dad "Woah, that\'s pretty tall!"
    
    show dad smile
    show bao happy
    
    bao "Yup! The tallest rocket we\'ve ever made. Doki 5 will soon be on its way to the outer planets of the Doki Planet System."
    
    show dad happy
    show bao smile
    
    dad "I heard about something called planets before, sounds cool."
 
    show dad smile
    show bao happy
    
    bao "Truly a once in forever opportunity, {w}the outer planets will be perfectly aligned so we can visit them all in one go. {w}The spacecraft in Doki 5\'s cargo compartment is our most advanced yet."
    bao "It will help us gain a lot of data on the outer planets. {w}What makes up their atmospheres, if there\'s water, stuff about their moons and a bunch of other information."

    show dad happy
    show bao smile
    
    dad "Sounds pretty complicated and expensive."

    show dad smile
    show bao happy
    
    bao "It is, but the information and knowledge we stand to learn from this mission is priceless."

    show dad happy
    show bao smile
    
    dad "This whole mission sounds fascinating, I am so excited to be able to watch the rocket launch in person!"

    show dad smile
    show bao happy
    
    bao "Let’s get to the viewing platform, the rocket will launch in about 10 minutes, we gotta be quick!"
    
    scene bg nasaplatform with fade
    
    show dragoon distressedtalking at dragooncentre with charfade
    
    dragoonengi "😬⛔💨🥵👎🙅‍♂️🚀"
    
    show bao worriedtalking at slightright
    show dad worried at slightleft
    with charfade
    show dragoon distressed
    
    bao "What\'s that? There\'s a blockage in the vent which is preventing the launch?"
    
    show dragoon distressedtalking
    show bao worried
    
    dragoonengi "😨⌛🚀⏰🪟🛑📅‼️"

    show dragoon distressed
    show bao worriedtalking
    
    bao "You\'re right! We don\'t have a lot of time before the launch and we can\'t afford to delay, it would set us back months! We could miss our once in forever launch window!"

    show dragoon distressedtalking
    show bao worried
    
    dragoonengi "😱🔥💣‍🚀️💥💰💸💀"

    show dragoon distressed
    show bao worriedtalking
    
    bao "WAIT WHAT!? Oh crap, that rocket costs billions! We don’t even have the budget to build another rocket!"
        
    dad "{i}I don\'t know a lot about those pointy things, but I do know that an explosion probably wouldn\'t be too good."

    show dragoon distressed
    show bao worriedtalking
    
    bao "How do we fix this? We can\'t lose everything!"

    show dragoon distressedtalking
    show bao worried
            
    dragoonengi "🤏🐕🛠️🐶🪛🚀🤞"
    
    show dragoon distressed
    show bao worriedtalking
        
    bao "Oh! You’re saying that someone like a small dog could fit through and fix the problem?"

    show dad worriedtalking
    show bao worried
    
    dad "Say less fam. I got this."
    
    hide dad with Dissolve(2.5)
    
    pause 1.5
    
    show dad happy at slightleft with charfade
    
    dad "I think I fixed the problem, there was a giant tomato blocking the critical ventilation pathway."

    show dragoon distressedtalking
    show dad smile
    
    dragoonengi "🤔🍅⁉️🤯"
    
    show dragoon distressed
    show bao worriedtalking
    
    bao "How in the name of Dokiville did that get there?"
    
    show dad happy
    show bao smile
    
    dad "I don\'t know, pretty tasty though."
    
    show bao happy
    show dad smile
    
    bao "Well you just saved the entire rocket launch! You saved everything! The rocket launch can go on!"
    
    show dad happy
    show bao smile
    
    dad "Oh cool! Nice."
    
    hide dragoon with charfade
    hide bao with charfade
    
    dad "{i}The rocket launch was beautiful and went without any further hiccups, the afternoon sun rays forming an impressive backdrop. (Source: Trust us.)"

    show neuro happy at slightright with charfade
    
    neuro "Hello, I am Neuro-sama, President of Dokiland. I saw you save this crucial mission, and I’d like to thank you officially with a ceremony the Beige-House on behalf of everyone in Dokiland. Please step into this limo."
    
    scene bg beigehouse with fadeslow
    
    play sound "bigclap2.mp3"
    
    show neuro happy at slightright
    show dad suitsmile at slightleft with charfade

    neuro "On behalf of this great country and under the powers given to me as President of Dokiland, I bestow upon you the Medal of Honour for your small size... Ahem, bravery and selfless service to our nation."
    
    scene bg beigehouse with fadeslow
    
    show neuro happy at slightright
    show dad suitsmile at slightleft with charfade
    
    neuro "Thank you again for your incredible work."
    
    show neuro smile
    show dad suithappy
    
    dad "No worries, was pretty fun, and the tomato was kind of tasty too."
    
    show neuro happy
    show dad suitsmile
    
    neuro "I would like to ask you to lead my new department \"Management of Memology\"."
    
    show neuro smile
    show dad suithappy
    
    dad "Cool. \"M.O.M. Department\" sounds like fun."
    
    show neuro happy
    show dad suitsmile
    
    neuro "Great, here\'s your team please get to work right away."
    
    show neuro smile
    show dad suithappy
        
    dad "No sweat."

    scene bg boardroom
    
    show dragoon distressedtalking at slightright
    show dad worried at slightleft
    with charfade
    
    dragoonassist "🖼️💻😡⚠⚔️️"
    
    show dad worriedtalking
    show dragoon distressed
    
    dad "Uh oh. That\'s very not good."
    
    show dragoon distressedtalking
    show dad worried
    
    dragoonassist "🤬🪖💢🧑‍💻☢️"
    
    show dad worriedtalking
    show dragoon distressed
    
    dad "I didn\'t think posting that meme would cause this to happen! {w}Everyone loves that meme!  {w}Tell the nuclear command not to launch the nukes! {w}I repeat, DO NOT LAUNCH THE NUKES..."
    
    show dragoon distressedtalking
    show dad worried
    
    dragoonassist "⌛🫣☢️💥🫠☠️"
    
    show dad worriedtalking
    show dragoon distressed
    
    dad "I KNOW, I KNOW! {w}Let me think! Oh gosh how do we solve this... {w}Wait. {p}I know! I’ll call Doki for help."
    
    show dad worried

    play sound "phone.mp3"
    
    doki "D.A.D.??? {w}Where are you??? {w}What\'s going on??? {w}Why are you calling me from the other room...{w} How are you calling me???"

    show dad worriedtalking

    dad "Well actually I’m at the Beige House, and there’s a bit of a memergency. Check your feed."
    
    show dad worried
    
    doki "WHAT THE FUCK DAD. HOW DID THIS HAPPEN? WHAT EVEN... HOW... WHAT... WHY... PLEASE EXPLAIN???"

    show dad worriedtalking

    dad "Well its a long story... {p}It all started when..."
    
    jump start
    
    # This ends the game.

    return
