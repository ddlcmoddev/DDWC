label minigame:
    stop music fadeout 2.0
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    image bg_minigame = "mod_assets/ren_OS.png"
    image y1 = im.FactorScale("y_mg_1.png", 0.25, xalign=0.15, yalign=0.1)
    image m1 = im.FactorScale("m_mg_1.png", 0.25, xalign=0.15, yalign=0.9)
    scene bg_minigame
    




#This is the beginning of the poem minigame
label start_game(transition=True):
     #Stop previous music
   
    #Disable un-needed UI things
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    # if persistent.playthrough == 0 and chapter == 0:
  
    #     call screen dialog("We're done choosing poems! So from now on we are going to read books. Choose the book you think fits best with the girl you like!", ok_action=Return())
    # $ chosen = 0

    if persistent.playthrough == 0:
        call screen dialog("It's time to get rid of the poems!\n\nPick books based on the cover and the title you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
    python:

        m_like = 0
        y_like = 0  
        n_like = 0
        s_like = 0
        bought_ymg1 =  False
        try:
            renpy.call_screen("computer")
            renpy.hide_screen("computer")
            renpy.hide_screen("books")
                
                
            played = 1
            renpy.jump("day2_end")
        except:
            renpy.call("error")
       
  
    # show screen placeholder
            
        


    #Display a tutorial tooltip on very first playthrough of minigame
    
   

   