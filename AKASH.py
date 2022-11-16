import os
import sys

print("""\033[1;32
   ###    ##    ##    ###     ######  ##     ##
  ## ##   ##   ##    ## ##   ##    ## ##     ##
 ##   ##  ##  ##    ##   ##  ##       ##     ##
##     ## #####    ##     ##  ######  #########
######### ##  ##   #########       ## ##     ##
##     ## ##   ##  ##     ## ##    ## ##     ##
##     ## ##    ## ##     ##  ######  ##     ##""")
print("")
print("[1]RANDOM UID CLONE M<1")
print("[2]RANDOM UID CLONE M<2")
print("[3]RANDOM UID CLONE M<3")
print("[4]EXIT")

xd =input("CHOOSE:")
if xd ==['1']:
  os.system("python m1.py")

elif xd ==['2']:
  os.system("python m2.py")
  
elif xd ==['3']:
  os.system("python m3.py")
  
elif xd ==['4']:
  os.system("exit")
 

