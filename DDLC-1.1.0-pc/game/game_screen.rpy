style note_text:
        color "#000"

style buy_text color "#00FF00"


screen computer:
        imagebutton idle "mod_assets/store.png" xalign 0.050 yalign 0.3 action Show("books")
        imagebutton idle "mod_assets/editor.png" xalign 0.050 yalign 0.5 action Show('Text')
        imagebutton idle "mod_assets/gallery.png" xalign 0.050  yalign 0.8 action Show('gallery')
      
image gamebg:
        "mod_assets/minigame_bg.png" 
        xzoom 0.35
        yzoom 0.35
        yalign 0.5
        xalign 0.5
        
screen books:
        add  "gamebg"
        text "portait of markov" xalign 0.15 yalign 0.655
        text "Kogarashi" xalign 0.67 yalign 0.655
        # textbutton "bacchus" xalign 0.15 yalign 1.0 action SetVariable("m_like", +1),  Return(True)                 
        add "mod_assets/y_mg_1.png"  xalign 0.15 yalign 0.4  zoom 0.20
        add "mod_assets/n_mg_1.png"  xalign 0.7 yalign 0.4  zoom 0.23
        textbutton "Buy now" xalign 0.15 yalign 0.7 action SetVariable("y_like", +1), Return(True)
        textbutton "Buy now" xalign 0.67 yalign 0.7 action SetVariable("n_like", +1), Return(True)
        textbutton "back" xalign 0.5 yalign 0.9 style "note_text" action Hide("books")

screen Text:
        add "mod_assets/note.png" xalign 0.5
        text "Note to self, \nDon't let Yuri and Natsuki fight"  xalign 0.5  
        textbutton "back" xalign 0.3 yalign 0.9 style "note_text" action Hide("Text")

screen gallery:
        if photos >= 1:
                add "mod_assets/placeholder.png" 
        





          