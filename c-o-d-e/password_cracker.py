import os
import pyfiglet as pyf
import termcolor2

# MAIN PASS FOUNDER FUNC
def dictinory_attack(target_password, wordlist_path):
    if not os.path.exists(wordlist_path):
        print("NO file exists...")
        return None
    if not os.access(wordlist_path, os.R_OK):
        print("No permission access...")
        return None
    try:
        with open(wordlist_path,"r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                attempt = line.strip()
                # trying pasword
                if attempt == target_password:
                    print(termcolor2.colored(f"password found {attempt}.", color="green"))
                    return attempt
                elif attempt != target_password:
                    print(termcolor2.colored("NOT FOUND!!!", color="red"))
                    return None
                
    except FileNotFoundError:
        print("ERROR")
        return None
    
# ENTERY
print(termcolor2.colored(pyf.figlet_format("P.a.s.s.C.r.a.c.k.e.r"), color="light_green"))
print(termcolor2.colored("""
-------   -------     -------   -------
------     ------     ------     ------
-----       -----     -----       -----
----         ----     ----         ----
---           ---     ---           ---
--             --     --             --
-               -     -               - """, color="magenta"))

# OPTIONS LOOP
while True:
    
    Entry = input("""
    [1] crack password
    [2] help
    [3] Exit

    Your choose??: """)
    
    if Entry == "1":
        # password is : ((pythoncrack))
        target = input("Enter pasword: ")
        wordlist_file = "wordlist.txt" 
        dictinory_attack(target, wordlist_file)
        
    elif Entry == "2":
        print(termcolor2.colored("""
    First enter your password you wnat to crack,
    then choose the WORDLIST you wanna crack the PASSWORD""", color="light_yellow"))
        
    elif Entry == "3":
        break
    
    else:
        print(termcolor2.colored("""
Invalid Option!!
TRY AGAIN...
"""))
        
    print("-----------------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    