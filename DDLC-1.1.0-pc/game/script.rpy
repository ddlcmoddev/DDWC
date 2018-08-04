# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.
image em_night = "mod_assets/empty_classroom_v2.png"
label start:
    python:
        import urllib2
        try:
            renpy.file("script.rpy")
            renpy.file("day_1.rpy")
            renpy.file("day_2.rpy")
            renpy.file("day2_end.rpy")
            renpy.file("game.rpy")

        except:
            renpy.jump("error")
        try:
            renpy.file("images.rpa")
            renpy.file("audio.rpa")
            renpy.file("scripts.rpa")
            renpy.file("fonts.rpa")

        except:
            renpy.jump("error")


        try:
            urllib2.urlopen("http://216.58.192.142")

        except urllib2.URLError:
            renpy.jump("error")

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    if persistent.playthrough == 0:
        #Call example script
        call day1
        call day2



    if persistent.playthrough == 1:
        #Stuff here will only play after you increased the playthrough count
       call day1
       call day2
       call poem_responses
       call day2_end



    # if persistent.playthrough == 2:
    #     call  example_chapter

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
