label opt:

init python:

    renpy.get_refresh_rate(precision=5)
    if  _return <= 1000:
        renpy.notify("DDWC tried to free up some memory because your fps was low")
        