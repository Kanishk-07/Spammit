#!/usr/bin/python
#Copyright 2020 SPAMMIT
#License issued under Apache license 2.0
import time 
import pyautogui
print("""
:'######::'########:::::'###::::'##::::'##:'##::::'##:'####:'########:
:##... ##: ##.... ##:::'## ##::: ###::'###: ###::'###:. ##::... ##..::
:##:::..:: ##:::: ##::'##:. ##:: ####'####: ####'####:: ##::::: ##::::
: ######:: ########::'##:::. ##: ## ### ##: ## ### ##:: ##::::: ##::::
:..... ##: ##.....::: #########: ##. #: ##: ##. #: ##:: ##::::: ##::::
:##::: ##: ##:::::::: ##.... ##: ##:.:: ##: ##:.:: ##:: ##::::: ##::::
: ######:: ##:::::::: ##:::: ##: ##:::: ##: ##:::: ##:'####:::: ##::::
:......:::..:::::::::..:::::..::..:::::..::..:::::..::....:::::..:::::
""")
print("")
time.sleep(1)
msg = input("> Enter the text: ")
print("")
repeat = int(input("> Input the number of repititions:  "))
print("")
limit = int(input("> Input the time limit between successive text [ms]:  "))
print("")
print("> Place your cursor on the spam location")
print("> You have 5 seconds after you hit enter")
enter = input("> Hit enter when ready")
print("\nSpamming in...")
count = 5
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1
for i in range(0, repeat):
	if msg != "":
		pyautogui.typewrite(msg + '\n')
		pyautogui.press("enter")
	else:
		print("No input was detected!")

time.sleep(limit/1000)

print("> End of spam")
print("> Au Revoir!")







