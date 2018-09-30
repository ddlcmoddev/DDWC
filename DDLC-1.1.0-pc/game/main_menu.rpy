init:
    image ddwc_bg:
        "mod_assets/bg.png" 
        subpixel True
        topleft
        xzoom 0.657 yzoom 0.657
        subpixel True
        
        parallel:
            ypos 0
            time 0.65
            ease_cubic 2.5 ypos -500

        parallel:
            xoffset 0 yoffset 0
            linear 3.0 xoffset -300 yoffset -300
            repeat
       

screen main_menu():

    
    # This ensures that any other menu screen is replaced.
    tag menu


    style_prefix "main_menu"

    add "ddwc_bg"
        

       

    #add "menu_art_y"
    #add "menu_art_n"
    add "menu_particles"
    frame:
        pass

## The use statement includes another screen inside this one. The actual
## contents of the main menu are in the navigation screen.
    use navigation

    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_logo"
    #add "menu_art_s"
    add "menu_particles"
    #add "menu_art_m"
    add "menu_fade"

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "v. [config.version]":
                style "main_menu_version"


    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav2"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size

screen menu_nav2:
    background "mod_assets/menu-nav.png"
    xalign 1.0
    yalign 1.0
    
