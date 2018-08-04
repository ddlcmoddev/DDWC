#dear curious peson

label day1:

    stop music fadeout 2.0


    $ renpy.movie_cutscene("when_will_it_end_game.webm")
    scene black

# python:
#     import os
#     script = "\\run123.py "
#     game = "\\game"
#     from subprocess import call
#     dn = os.path.dirname(os.path.abspath(__file__))
#     os.chdir( dn )
#     execfile(dn + script)

# python:
#     import os
#     from subprocess import call
#     dn = os.path.dirname(os.path.realpath(__file__))
#     wp = "\setdesktopwp.py "
#     os.chdir(dn)
#     os.system('py '+ dn + wp)

    # test = False
    # if test == True:
    #         import call123

    # import os
    # from subprocess import call
    # dn = os.path.dirname(os.path.realpath(__file__))
    # call(["python", dn + "call123.py "])
    # import file

    # os.system(dn + '\call123.py')
    # execfile('call123.py')
    # os.system('python', dn + 'call123.py')

    # import os
    # from subprocess import Popen
    #
    # Popen('python call123.py')
    #
    # # subprocess.call(config.basedir + '\game\setdesktopwp.py')
    #     # os.system('config.basedir + '\game\setdesktopwp.py')

#     os.system(config.basedir + '\game\setdesktopwp.py')
    # execfile()
            # def run(runfile):
            # with open(runfile,"r") as rnf:
            # exec(rnf.read())

    # run("call123.py ")

# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Monika",
#               "I still love you",
#               icon_path="custom.ico",
#               duration=10)
"..."
"where am I?"
"Hey."
"Yes, I’m talking to you."
"This shouldn’t be a surprise, right?"
"The main character talking to the player."
"You’re probably really excited, aren’t you?"
"Well, don’t be."
"The game is rebuilding itself, so this will be our only chance to talk."
"Well, for me to talk at you."
"So, here’s what I want to ask:"
"Are you sure you want to do this?"
"However the original game ended, Monika deleted everything."
"You’re not supposed to be here."
"If you go through with undoing everything Monika did, you’ll regret it."
"I could tell you why, but that wouldn’t be any fun."
"I’m not protesting at all; I’d rather exist than otherwise."
"I’m just incredulous that you’d really be so stupid."
"Well, it’s just about done now."
"Soon, I’ll go back to narrating the story and speaking for you."
"Being the dense MC."
"Heh."
"In that respect, I guess you and I aren’t that different after all."
"The time has come."
"Farewell, player."
"Good luck."
scene bg club_day
with wipeleft
#scene switch
"Today’s a normal day like any other."
"… Yeah, no way."
"Even now, I can still feel yesterday’s festival in my head."
"The sound of a crowd’s chatter, the smell of the bonfire’s smoke…"
"I feel like I won’t be able to forget any of it, especially since it was my first time spending it with friends."
"Last week, I was forced by an old friend of mine to join the newly-founded Literature club."
"Now, I’m bringing her breakfast."
"I knock on her door, clutching a plastic box of scrambled eggs and bacon."
mc "Sayori, open up! I brought you breakfast!"
"After a moment, I heard footsteps coming closer, only to be interrupted with a loud thud and a cry of shock."
mc "Sayori?!"
"I jiggle the doorknob; sure enough, she forgot to lock it. For once, I’m grateful for her clumsy nature as I rush in and find her on the floor, her limbs tangled up on a disheveled rug."
mc "Geez… This is kind of sad, even for you."
"Sayori scrambled to her feet, pouting at my words."
show sayori 4p zorder 2 at t32
s "I tripped on the rug! People do that all the time!"
"Before she can protest any further, she spots the food in my hand."
s 1q "Ooh, breakfast! Thanks, [player]!"
"She lunges for the box, grabbing it from my hand and rushing to the dining table to eat. "
mc "Well, if you aren’t gonna take care of yourself, I’m gonna have to step up as your friend and help you out, aren’t I?"
"Sayori suddenly froze, releasing the lid of the plastic box and turning in her seat to look at me."
show sayori 1t
"Her lip is quivering and large tears are threatening to run down her cheeks."
s "[player]... t-that’s the nicest thing y-you’ve ever said to me…"
"I roll my eyes."
mc "Sayori, it’s gonna get cold if you don’t eat."
"Sayori sniffs, wiping her eyes and saluting me."
s 2x "Right!"
"After eating, Sayori and I set off for school."
s 1a "Are you excited to come back to the literature club?"
mc "I guess I should be, but it’s not like we got any new members."
s 1c  "What are you talking about? At least a couple people took the sign-up forms!"
mc "They all said, ‘I’ll think about it.’ They just took the forms to be polite."
"I glance at Sayori and see that she’s about to cry again. I sigh and give in."
mc "But I guess there’s no point in being pessimistic. We won’t know until after school, right?"
s 1s "Exactly! You always assume the worst; assume the best for a change!" 
"Just like that, she’s back to her bubbly self."
"Maybe she’s right, though. She’s known me since I was a kid; if she says I’m pessimistic, I very well could be."
"I should try and be a better person, for Sayori’s sake."
#(if MC chose someone else’s route in the original game)mc "And for xxxxx’s sake as well…"
"-scene change to the classroom-"
"During class, almost no one pays attention to the teacher’s lectures."
"Either by passing notes, texting, or just whispering, the only thing people can focus on is gossiping about the events of yesterday’s festival."
"It was such a dumb idea to hold it on a Monday instead of a Friday."
"By the end of the day, I conclude that my class isn’t the only one disregarding the lessons, due to Sayori entering my classroom before the bell even rings."
s 2c "Come on, we gotta get to the club before any of our new members arrive!"
"Already, she’s frantically attempting to drag me out of my seat."
mc  "Okay, okay! Let me keep my arm at least!"
"Rubbing my aching shoulder, I exit the classroom with Sayori."
# scene change to the hallway
mc "Did Natsuki bake cupcakes?"
s 1a "I think so! She didn’t seem too happy about it, since she doesn’t think anyone’s really going to come."
s 1b "If you ask me, she’s just hoping that no one else joins… but that’s so mean!"
s  "Monika worked so hard for this club! Shouldn’t we help her to make her vision a reality?"
mc  "guess. I can’t say I care too much."
s 4h "Ehhhhh?! Seriously? You’re just as bad as Natsuki…"
"I chuckle as she pouts. Teasing Sayori is always fun."
mc "Well, there’s always the chance that Natsuki will find another manga fan."
s 1a "Yeah! She’s gonna wish she made cupcakes then!"
"It’s absolutely incredible how quickly she jumps between emotions."
"She’s got endless energy…"
"But I know it’s an act."
"Even now, Sayori could be thinking all sorts of horrible things about herself."
"Yesterday, Monika and I helped her talk about her feelings with the rest of the club, before the festival began."
"Now that Sayori has a group of people that truly support her, I hope that she’ll start to get better."
#-CLUB TIME YAY-
"When we arrived at the clubroom, Sayori threw the door open, wild with enthusiasm."
s 3r "Hello, everyone! We’re here!"
"Sayori was greeted with silence as Yuri looked up from her book in slight surprise and Natsuki cowered at the opposite end of the classroom."
"The silence was short-lived of course, cut short by Natsuki shouting back at Sayori."
show natsuki 4b zorder 1 at t41
n "What’s your problem, idiot?! You scared the crap out of me!!"
s 1c "Oh…"
s 1s "Ehehe, sorry, I was just so excited to meet the new club members!"
y "But there’s no one here besides us…"
"Quickly glancing around the room, I saw that Yuri was right. Even Monika hadn’t showed up yet."
"Sayori withered a bit, but still she tried to keep her optimism intact."
s 3e "Well, we’re really early anyway! Maybe the new members are turning in their forms last minute, or they’re rallying more friends!"
show natsuki 1b 
"Natsuki opened her mouth to retort, but was interrupted by Monika rushing past me into the room with a box in her arms."
show natsuki 2g
show monika 1m at t44 zorder 3
m "Sorry I’m late, everyone! I was arranging something for the new members!"
m 1c "Oh… no one new has arrived yet?"
n 1c "Of course not, we’re a literature club that doesn’t even read literature."
s 1d "But… There’s still a chance! I’m sure people will come!"
n 1e "Yeah, right. They only took the forms to be polite."
m 1g "Natsuki… You know how important this is to me."
m 1h "Why are you acting like this…?"
"Natsuki choked back her next words, her face turning red with shame."
n 1p "Yeah, well… we don’t need to change! At least now you’ll realize I’m right!"
"With that, Natsuki stomped to the back of the classroom and planted herself at a desk in the corner."
hide natsuki with fade
"Natsuki seemed to be right; the fate of the club’s member count has probably been sealed for now."
"But the disappointment on Monika and Sayori’s faces couldn’t be denied. Something had to be said.I felt bad for the girls, they put in so much hard work and no one came to see it."
mc "Well, if anything, we did make an impression on the school. We were the only club with free cupcakes and awesome decorations, after all!"
"Natsuki and Yuri perked up at my words, but didn’t say anything."
mc "And some people did spend a few minutes looking through the poetry pamphlets!"
"I think."
m 2n "You do have a point, [player]... and everyone’s performances were great! There may be some writers who will want to join."
s 1a "Yeah! Maybe the next batch of first years will bring some new members for now!"
m 1e "That’s still a year away… but I can be happy as long as I have those who are dear to me."
s 1q "Aww, Monika…!"
"Sayori jumped on Monika and hugged her tightly. Natsuki returned to sulking and Yuri watched the two girls embrace."
"She almost looked like she wanted to join."
m 1k "Okay, everyone! Since that’s settled, did anyone bring a poem to club?"
"Once again, the room was silent."
m 1i "Did we do anything over the weekend related to literature…?"
"Nothing."
m 1n "Oh… well, I’m glad that everyone worked hard on the festival, then."
m 1b "I was able to finish an extremely fascinating book! It’s called Hard-Boiled Wonderland and the End of the World."
m "It’s an extremely interesting novel with split points of view and astounding social commentary."
m "It’s somewhat confusing, but I appreciate the challenge! Yuri, you might like it too."
m "My favorite part is when- oh, well, that might be a bit of a spoiler."
m "I’d be happy to talk about it with whoever picks it up!"
y "I might like to give it a try, but first I want to finish this book…"
m "Ah. Oh well!"
"After that, Yuri returned to her novel and Natsuki buried her nose in a manga."
"Sayori came up to me, a sheepish look in her eyes."
s "So… [player]... I forgot to pack lunch again…"
mc "You need change for snacks, don’t you?"
s "Please! I promise I’ll try and pack a bento from now on! Just this one last time…?"
"Sayori clasped her hands together, begging for my mercy. I sighed, reaching my hand into my pocket. "
"Just as I was about to comment on her hopelessness and give her my spare change, Monika stepped between us."
m "Here, Sayori, this should be enough to bring snacks back for the five of us. Can you do that?"
"Sayori’s eyes widened as Monika handed her some crumpled bills."
s "You can count on me, President!"
"Sayori saluted for the second time that day and dashed out the door."
m "[player], I want to talk with you a second."
mc "Uh, sure, what about…?"
m "Well, it became our little tradition, and I figured you wouldn’t want to miss it, so…"
m "Here’s Monika’s writing tip of the day!"
m "There are two ways to write: downhill writing, and what I like to call scrambled writing."
m "Downhill writing can be fun because the writer gets to watch the story unfold before their eyes!"
m "But it can be difficult once you hit writer’s block; you lose the momentum of the story and could possibly lose interest in writing it."
m "Meanwhile, scrambled writing gets all the major events out of the way so you can link them together and add some foreshadowing."
m "But it could also confuse the story’s chronology in your head."
m "If you find yourself struggling with one type, try switching to the other!"
m "If writer’s block stops your momentum, write a major event later in the book and plan how they might be linked together."
m "If you’re struggling with keeping everything in order, try revising what you have using downhill writing."
m "It might be hard at first, but it’s good to utilize the strengths of both methods!"
mc "Right… I’ll keep that in mind."
m "Oh, and one more thing…"
m "I know things have been… a little tense. Today especially."
m "I can’t guarantee what’ll happen in the coming days, but just in case, I want you to do whatever is best for the other members."
m "Can you do that?"
mc "You mean with the whole thing about new members?"
mc "Well, I can try…"
m "Thank you. I’ll do my best as well."
M "..."
m "Well, that was Monika’s writing tip of the day!"
m "Sayori should be back with snacks any minute now."
s "I’m back! And I have snacks!"
m "Oh, right on time! Well then, it’s time to share poems!"
call poem_reponses

#timeskip-
"Things were a bit better after Sayori brought snacks."
"I read one of Natsuki’s mangas, Sayori and Monika talked."
"Yuri and Natsuki continued to read alone."
"After that, Monika dismissed everyone with the usual poem assignment and I began my trek home with Sayori."
#switch back to street-
s "[player], did you really mean those things you said?"
s "Before, you didn’t really seem to care."
mc "Well… I couldn’t just leave everyone sulking like that."
mc "I’ve got enough on my plate making sure you don’t starve."
s "Ehehe… maybe."
s "I’m really gonna try and be better with that…"
s "So you keep up what you’re doing! Keep encouraging everyone else."
s "That would make Monika so happy! She really needs it."
s "I thought that she was acting pretty strange last week, but she seems fine now…"
s "Did she say anything weird to you?"
mc "Hm? Not… really… she just told me to look after the members."
s "What?! She beat me to it then!"
s "Noooo! Curse your perfection, Monika!"
"I laughed out loud, earning a small smile from Sayori."
"We reached our houses, Sayori bid me good luck on my poem, and we parted ways."
"Now to get back to this nightmare…"
