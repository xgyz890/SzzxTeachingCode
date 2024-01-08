import numpy as np
import time

low=1
high=1000
s_t=0.8
n=np.random.randint(low,high)
name=input("Your name:")

def draw_sep_line():
    print("**"*10)
    
def textcolor(code='0'):
    """
    Set up the display effects of text. 
    """
    return '\033[%sm'%code

print(textcolor("1;32;41")+"Initial range:{}~{}".format(low,high)+textcolor())

while True:
    draw_sep_line()
    try:
        a1=int(input("{}'s turn:".format(name)))
        time.sleep(s_t)
        if a1>high or a1<low:
            print("Number out of range. Switching to AI's turn...")
        else:
            if a1>n:
                print("{}'s num is too big".format(name))
                high=a1-1
            elif a1<n:
                print("{}'s num is too small".format(name))
                low=a1+1
            else:
                print(textcolor("5;37;40")+
                     "{} wins!".format(name)+
                      textcolor())
                break
        time.sleep(s_t)
        print("Available numbers:"+
              textcolor('1;32;41')+
              "{}~{}".format(low,high)+
              textcolor())

    except ValueError:
        print("Invalid number. Switching to AI's turn...")
    
    draw_sep_line()
    time.sleep(s_t)
    print("AI's turn")
    time.sleep(s_t)
    if high>low:
        a2=np.random.randint(low,high)
    else:
        a2=low
    time.sleep(s_t)
    print("AI guessed: {}".format(a2))
    time.sleep(s_t)
    if a2>n:
        print("AI's num is too big")
        high=a2-1
    elif a2<n:
        print("AI's num is too small")
        low=a2+1
    else:
        print(textcolor("5;37;40")+
                     "AI wins!"+
                      textcolor())
        break
    time.sleep(s_t)
    print("Available numbers:"+
              textcolor('1;32;41')+
              "{}~{}".format(low,high)+
              textcolor())

    
    
