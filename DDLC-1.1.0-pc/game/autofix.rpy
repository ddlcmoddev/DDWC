label autofix:

scene errorbg

image logo animated:
    xalign 0.5
    yalign 0.3
    
    "mod_assets/logo.png"  with Dissolve(0.5, alpha=True)
    pause 1.0
    
    
    "mod_assets/logo_load.png" with Dissolve(0.5, alpha=True)
    pause 1.0
    
    repeat

show logo animated

python:
    
    ui.text("Please be patient while we try to fix the error", style="error_text", xalign=0.5, yalign=0.8)
    renpy.pause(6.0)
    ui.text("deleting cache...", style="error_text", xalign=0.5, yalign=0.7)
    renpy.free_memory()
    renpy.diff_memory(update=True)
    renpy.pause(4.0)
    ui.text("reloading script...", style="error_text", xalign=0.5, yalign=0.7)
    renpy.reset_physical_size()
    renpy.pause(4.0)
    ui.text("checking files...", style="error_text", xalign=0.5, yalign=0.7)
    try:
        renpy.file("script.rpy")
    except:
        ui.text("Mod file seems to be missing: script.rpy", style="exception_text", xalign=0.5, yalign=0.7)
        
    try:
        renpy.file("day_1.rpy")
    except:
        ui.text("Mod file seems to be missing: day1.rpy", style="exception_text", xalign=0.5, yalign=0.7)
    try:
        renpy.file("day_2.rpy")
    except:
        ui.text("Mod file seems to be missing: day2.rpy", style="exception_text", xalign=0.5, yalign=0.7)
    try:
        renpy.file("day2_end.rpy")
    except:
        ui.text("Mod file seems to be missing: day2_end.rpy", style="exception_text", xalign=0.5, yalign=0.7)
    try:
        renpy.file("game.rpy")
    except:
        ui.text("Mod file seems to be missing: game.rpy", style="exception_text", xalign=0.5, yalign=0.7)

    
   
    try:
        renpy.file("images.rpa")
    except:
        ui.text("DDLC file seems to be missing: images.rpa", style="exception_text", xalign=0.5, yalign=0.7)
        ui.text("please add missing file", style="exception_text", xalign=0.5, yalign=0.8)
    try:
        renpy.file("audio.rpa")
    except:
        ui.text("DDLC file seems to be missing: audio.rpa", style="exception_text", xalign=0.5, yalign=0.7)
        ui.text("please add missing file", style="exception_text", xalign=0.5, yalign=0.8)
    try:
        renpy.file("scripts.rpa")
    except:
        ui.text("DDLC file seems to be missing: scripts.rpa", style="exception_text", xalign=0.5, yalign=0.7)
        ui.text("please add missing file", style="exception_text", xalign=0.5, yalign=0.8)
    try:
        renpy.file("fonts.rpa")
    except:
        ui.text("DDLC file seems to be missing: fonts.rpy", style="exception_text", xalign=0.5, yalign=0.7)
        ui.text("please add missing file", style="exception_text", xalign=0.5, yalign=0.8)


    renpy.pause(4.0)
    ui.text("testing internet connection...", style="error_text", xalign=0.5, yalign=0.7)
    try:
        urllib2.urlopen("http://216.58.192.142")
        
    except urllib2.URLError:
        ui.text("No internet connection", style="exception_text", xalign=0.5, yalign=0.65-0)
        ui.textbutton("Quit", xalign=0.5, yalign=0.9, style="error_text", action=Quit(confirm=None))
        ui.interact()
    renpy.pause(2.0)

    ui.text("Please relaunch the game", style="error_text", xalign=0.5, yalign=0.7)
    renpy.pause(3.0)

    renpy.quit(relaunch=True, status=0) 