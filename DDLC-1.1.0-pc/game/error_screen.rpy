style error_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 30
style exception_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#ea2300"
    size 25

screen error:

    add "mod_assets/error.png"
    add "mod_assets/logo.png" xalign 0.5  yalign 0.3 zoom 0.4 
    
    text "An exception has occured"  style "error_text"  xalign 0.5  yalign 0.1 
    textbutton "Quit"  xalign 0.35 yalign 0.8 style "error_text" action Quit(confirm=None)
    textbutton "Attempt auto-fix"  xalign 0.5  yalign 0.8 style "error_text"  action Jump("autofix")
    textbutton "Contact support" xalign 0.7 yalign 0.8 style "error_text" action OpenURL("https://tawk.to/chat/5af75492227d3d7edc253b14/default/?$_tawk_popout=true")