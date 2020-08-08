#!/usr/bin/python
#Copyright 2020 SPAMMIT
#License issued under Apache license 2.0
#Written by: Kanishk 
import time 
import colorama 
import pyautogui
from colorama import Fore, Back, Style
print(Fore.GREEN)
print("##############################################")
print("#Script Name	:SPAMMIT                     #")
print("#Description	:Message spammer             #")
print("#Author         :Kanishk                     #")
print("#Instagram      :@kanishk_007_               #")
print("##############################################")
print("")
print(":'######::'########:::::'###::::'##::::'##:'##::::'##:'####:'########:")
print(":##... ##: ##.... ##:::'## ##::: ###::'###: ###::'###:. ##::... ##..::")
print(":##:::..:: ##:::: ##::'##:. ##:: ####'####: ####'####:: ##::::: ##::::")
print(": ######:: ########::'##:::. ##: ## ### ##: ## ### ##:: ##::::: ##::::")
print(":..... ##: ##.....::: #########: ##. #: ##: ##. #: ##:: ##::::: ##::::")
print(":##::: ##: ##:::::::: ##.... ##: ##:.:: ##: ##:.:: ##:: ##::::: ##::::")
print(": ######:: ##:::::::: ##:::: ##: ##:::: ##: ##:::: ##:'####:::: ##::::")
print(":......:::..:::::::::..:::::..::..:::::..::..:::::..::....:::::..:::::")
print("")
print(Fore.YELLOW)
time.sleep(1)
msg = input("> Enter the text: ")
print("")
repeat = int(input("> Input the number of repititions:  "))
print("")
limit = int(input("> Input the time limit between successive text [ms]:  "))
print("")
print(Fore.BLUE)
print("> Place your cursor on the spam location")
print("[Eg: If you want to spam on your friend's Instagram DM, just place the cursor on the text bar and execute the program!]")
print("> You have 5 seconds after you hit enter")
enter = input("> Hit enter when ready :)")
print(Fore.YELLOW)
print("Spamming in...")
count = 5
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1
for i in range(0,repeat):
	if msg != "":
		pyautogui.typewrite(msg + '\n')
		pyautogui.press("enter")
	else:
		print("No input was detected!")

time.sleep(limit/1000)

print(Fore.BLUE)
print("> End of spam :(")
print("> Follow me on Instagram => @kanishk_007_")
print("> Au Revoir!")







