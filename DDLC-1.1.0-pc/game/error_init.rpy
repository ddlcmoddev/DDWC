label error_init(text=""):
style error_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 30
style exception_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#ea2300"
    size 25
image error_text = ParameterizedText(style="error_text", anchor=(0,0), xpos=50, ypos=50)
image logo = im.FactorScale("logo.png", 0.5, xalign=0.5, yalign=0.3) 
image errorbg = "mod_assets/error.png"

python:

    import urllib2
    def modfiles():
        renpy.file("script.rpy")
        renpy.file("day_1.rpy")
        renpy.file("day_2.rpy")
        renpy.file("day2_end.rpy")
        renpy.file("game.rpy")
    
    def ddlcfiles():
        renpy.file("images.rpa")
        renpy.file("audio.rpa")
        renpy.file("scripts.rpa")
        renpy.file("fonts.rpa")
    def testconnection():
        urllib2.urlopen("http://216.58.192.142")
    try:
        filesearch()
    except:
        ui.text("Mod files seem to be missing", style="exception_text", xalign=0.5, yalign=0.7)
    
    try:
        ddlcfiles()
        
    except:
        ui.text("Original DDLC files seem to be missing", style="exception_text", xalign=0.5, yalign=0.75)
        
      

    try:
        testconnection()
        
    except urllib2.URLError:
        ui.text("No internet connection", style="exception_text", xalign=0.5, yalign=0.65)
    
   

    ui.text("An exception has occured", style="error_text", xalign=0.5, yalign=0.1)
    ui.textbutton("Quit", xalign=0.35, yalign=0.8, style="error_text", action=Quit(confirm=None))
    ui.textbutton("Attempt auto-fix", xalign=0.5, yalign=0.8, style="error_text", action=Jump("autofix"))
    ui.textbutton("Contact support", xalign=0.7, yalign=0.8, style="error_text", action=OpenURL("https://tawk.to/chat/5af75492227d3d7edc253b14/default/?$_tawk_popout=true"))
    ui.close()
    ui.interact()