label filedesktop:

init python:
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass
    
    
          
python:    
        
    import os
    love = "I love you " 
    loveyou = love + user  
    txt = ".txt"
    os.chdir(os.path.expanduser('~/desktop'))
    file = open(loveyou + txt,'w+')
    file.write('I still love you')
    file.close()