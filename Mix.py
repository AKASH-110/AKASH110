import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\nSorry System not support this tools');sys.exit()




print("""\033[1;32m          o      oooo   oooo      o       oooooooo8 ooooo ooooo 
\033[1;97m         888      888  o88       888     888         888   888  
\033[1;32m        8  88     888888        8  88     888oooooo  888ooo888  
\033[1;97m       8oooo88    888  88o     8oooo88           888 888   888  
\033[1;32m     o88o  o888o o888o o888o o88o  o888o o88oooo888 o888o o888o """)

print('\n\n\033[1;37m[•] This tools only for 64bit device ')
print('\n[1] RANDOM NUMBER CLONE M1 \n[2] RANDOM NUMBER CLONE M2 (Updated)\n[3] Check Update \n')
xd=input('[•] choose: ')
if xd in ['1','01']:
    if path.isfile('free.cpython-311.so'):
        import free
    
elif xd in ['2','02']:
    if path.isfile('mb1.cpython-311.so'):
        import mb1    
       
        print('\n[•] Checking updates...')
        system('python MIX.py update')
