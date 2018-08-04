label poem_responses:
    $ skip_transition = False
    $ sayori_readpoem = False
    $ monika_readpoem = False
    $ yuri_readpoem = False
    $ natsuki_readpoem = False
    $ poemsread = 0
    label poem_loop:
    if poemsread == 4:
        jump day2_end
    # else:
    #     pass
    hide monika with dissolve
    hide sayori with dissolve    
    hide natsuki with dissolve
    hide yuri with dissolve
    scene bg club_day
    with wipeleft_scene  
    if poemsread == 0:
            $ menutext = "Whom should I show my poem to first?"
    else:
            $ menutext = "Whom should I show my poem to next?"
    menu:
        "[menutext]"

        "Sayori" if not sayori_readpoem:
            $ sayori_readpoem = True
            if poemsread == 0:
                "I guess I'll show it to Sayori"
                "she likes basically everything I write and I could use a confidence boost"
            call s_poem1     
        "Nastuki" if not natsuki_readpoem:
            $ natsuki_readpoem = True
            if poemsread == 0:
                "I will show mine to natsuki"
                "I haven't spoken to her in a while"
               
            call n_poem1
        "Yuri" if not yuri_readpoem:
            $ yuri_readpoem = True
            if poemsread == 0:
                "yuri seems like a good option"
                "she can really give me good feedback"
                
            call y_poem1
        "monika" if not monika_readpoem:
            $ monika_readpoem = True
            if poemsread == 0:
                "monika is always nice to talk with"
                "I'll show it to her"
                
            call m_poem1

    $ poemsread += 1
    if poemsread < 3:
        jump poem_loop
    if poemsread > 3:
        jump day2_end


label s_poem1:
    if poemsread == 3:
        jump day2_end
    scene bg club_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    "I patiently waited for sayori to finish reading my poem"
    "it took really long"
    mc "well?"
    s 1m "what?"
    s 1s "oh the poem"
    s "I loved it!!"
    s 1a "your style is so good!"
    mc "are you okay? you spaced out there for a moment"
    s 1s "yeah sorry"
    s 1x "but I loved your poem!"
    s "now it's time to show you mine"
    call showpoem(poems1)  
    mc "I like it sayori"
    s "that's all? I guess it isn't that good..."
    mc "well I mean there isn't much else to say about it"
    s 5c "meanie..."
    mc "I'm kidding, I think it was great sayori."
    mc "I am just not very good at giving feedback that's all."
    "It wasn't like her to say this, but I guess I could have reacted a different."  
    s 1a "that's okay!"
    s "you'll learn someday"
    "I shook my head with a smile."
    jump poem_loop

label y_poem1:
    scene bg club_day
    show yuri 1a at t11 zorder 2
    with wipeleft_scene
    "I watched yuri read my creation"
    "for someone as skilled as her it must be painful to read this"
    y 1u "I can see you worked hard on it [player]"
    mc "yeah... I guess"
    "I just wanted to get this over with and get to her poem."
    "I could already tell none of the girls liked my writing"
    mc "let's see yours"
    y 1m "okay [player], here it is"
    "yuri gave me a warm smile, something I didn't see very often with her"
    call showpoem(poemy1)
    mc "wow this is very good"
    y 4a "thank you [player]"         
    y "you're too kind" 
    "yuri always hides her face when she gets compliments"
    "I guess she just isn't used to it"
    jump poem_loop

label n_poem1:
    scene bg club_day
    show natsuki 1bj at t11 zorder 2
    with wipeleft_scene
    "I was curious to find out what natsuki thought of my poem"
    "She took her time to read it"
    n "well you have gotten bit better"
    n 1by "don't think that's something good though"
    n "you still have a lot to improve"
    mc "that's true"
    mc "maybe you can teach me something by showing me yours"
    n 1bt "okay, that makes sense"
    call showpoem(poemn1)
    n "I can already tell you don't like it"
    "nastuki gave a loud sigh"
    mc "what are you talking about?"
    mc "I really liked it"
    n "r-really?" 
    n "I-I mean yeah duh, it's because I'm a pro"
    mc "if you say so Natsuki"
    jump poem_loop
        

label m_poem1:
    scene bg club_day
    show monika 1a at t43  zorder 2
    with wipeleft_scene
    m "hello [player]"
    m 1a "I'm excited to see what you've come with~"
    mc "well since you insist"
    "I handed monika my poem"
    "I think it won't be as good as she says it is"
    m 1h "mmmh.."
    mc "mmmh?"
    m 1j "I think it's lovely [player]"
    mc "well thank you, I did work hard on it"
    m "I can see that, it's good to see you work on th poems!"
        


    

