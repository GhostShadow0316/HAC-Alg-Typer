# import libraries
import os,os.path
import webbrowser

# define funcs
def cls():
    from os import system
    system("cls")

def s(times=1):
    for i in range(times):
        print()

def help():
    print('''How To Use

Press "w" for "U"
Press "s" for "D"
Press "a" for "L"
Press "d" for "R"
Press "q" for "F"
Press "e" for "B"
Press "z" for "M"
Press "x" for "S"
Press "c" for "E"
Press "'" for "'"
Press "/" to "make the last letter to a lower case"
Press a letter two times for a "2" behide the letter

Use "cls" to clear the window
Use "/s" to save all alg you typed''')


def save():
    global ipl,opl
    getpath = False
    while not getpath:
        path = input('Save Path("exit" to exit) > ')
        if path=="exit":
            return
        elif os.path.exists(path):
            if os.path.isdir(path):
                getpath = True
            else:
                s()
                print("Input a Dir")
                s()
        else:
            s()
            print("Input a True Path")
            s()
    fn = input('Save File Name > ')
    if path=="":
        from time import localtime
        time1 = localtime()
        if not(str(time1.tm_mon)[0]=="0"):
            save_file = open(f"{path}/alg_{time1.tm_year}0{time1.tm_mon}{time1.tm_mday}_{time1.tm_hour} {time1.tm_min}.txt","w+",encoding='utf-8')
        else:
            save_file = open(f"{path}/alg_{time1.tm_year}{time1.tm_mon}{time1.tm_mday}_{time1.tm_hour} {time1.tm_min}.txt","w+",encoding='utf-8')
    else:
        save_file = open(f"{path}/{fn}")
    for i in opl:
        save_file.write(f"{i}\n")
    save_file.close()
    s()
    print(f"Saved! filename:{str(save_file)[25:-29]}")
    s()
    

def main():
    global hint,ip,ipl,opl
    ip = input(f"{hint}> ")
    hint = ""

    if ip=="/h":
        help()
    elif ip=="cls":
        cls()
    elif ip=="/s":
        save()
    else:
        ipl.append(ip)
        dealwithalg(ip)


def dealwithalg(ip):
    global opl,hint
    op=""
    for i in ip:
        if i=="d":
            op += " R"
        elif i=="a":
            op += " L"
        elif i=="w":
            op += " U"
        elif i=="s":
            op += " D"
        elif i=="q":
            op += " F"
        elif i=="e":
            op += " B"
        elif i=="x":
            op += " M"
        elif i=="z":
            op += " S"
        elif i=="c":
            op += " E"
        elif i=="'":
            op += "'"
        elif i=="/":
            op += "w"
        elif i=="(":
            op += " ("
        else:
            op += i
    op = op.replace("''","'").replace("  "," ").replace("2'","'2").replace("'w","w'").replace("2w","w2").replace("( ","(")    .replace("Rw","r").replace("Lw","l").replace("Uw","u").replace("Dw","d").replace("Fw","f").replace("Bw","b")    .replace("R R","R2").replace("L L","L2").replace("U U","U2").replace("D D","D2").replace("F F","F2").replace("B B","B2").replace("r r","r2").replace("l l","l2").replace("u u","u2").replace("d d","d2").replace("f f","f2 ").replace("b b","b2")
    
    
    opl.append(hint)
    opl.append(op[1:])
    s(2)
    print(op[1:])
    s(2)
    

def title():
    cls()
    print("Cube Alg Typer")
    s()
    print("ver. 20220417-5")

## main ##
ipl,opl = [],[]
hint = ""
title()
s(3)
print('"/HELP" or "/h" for help')
s()

while True:
    main()