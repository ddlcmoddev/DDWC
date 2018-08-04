label day2_end:
stop music fadeout 2.0
play music t3
scene bg club_day
with wipeleft_scene
show monika 4b at f43 zorder 3
show sayori 1a at t41 zorder 1
show natsuki 1a at t42 zorder 1
show yuri 1a at t44 zorder 1
m "okay everyone! that's for today"
m 1b "Now, we've been writing poems for a while."
m "and I thought it might be time for something different!"
m "So, we won't be writing poems any longer"
s 4s "yay!"
y 3d "that's a relief"
n 5d "that's better!"
m 2l "I didn't realize it was so bad"
mc "well I mean it was a bit awkward at first"
mc "but I got use to it after a while"
m 1b "okay so as I was saying, we won't be writing poems."
m "but instead reading books, of your own choice."
y 1u "that sounds lovely"
n 2a "I guess I could go with that"
s 1a "I like that"
m 4b "After you read a bit, you choose a partner and discuss the book with her or him!"
"So long at it doesn't end up in a fight like last time"
m 1a "Okay So I want you to all pick a book and we'll discuss it tommorow!"
"one by one the girls started to pack their stuff. Yuri packed her books, I guess she must be thrilled for this. Since all she does is reading. "
hide yuri 
hide natsuki
hide monika
hide sayori
python:
    renpy.notify("minigame updated!")
    renpy.iconify()
"But there is something odd. All the girls, including sayori. Have a concerned look on their face."
"like they were thinking"
"I see sayori approach me"
show sayori 1q at h42 zorder 1
s "hey [player]!"
mc "hello sayori"
s 1b "So have you thought about your partner?"
mc "huh?"
s 1q "for the books silly!"
mc "oh right, well I don't know yet. I'll decide tommorow"
"this will be a hard descion. I don't want to disapoint any of the girls"
"but I also don't want to start a fight again"
s 1a "okaaay, I'll be avaible as partner too you know"
s 5l "hehe"
mc "I know sayori. I'll decide tommorow, for now let's walk home"
s 1a "okay!"
