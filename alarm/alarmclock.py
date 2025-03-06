#https://www.zedge.net/ringtones/64456525-7989-4834-8e11-290b68d790f1
from playsound import playsound
import time
import random
import threading

CLEAR = "\033[H\033[J"
STOP=False
STR=""

def alarm(second):
    time_elapsed = 0

    while time_elapsed < second and not STOP:
        time.sleep(1)
        time_elapsed += 1

        time_left = second - time_elapsed
        min_left=time_left//60
        sec_left=time_left%60
        if time_elapsed<=second:
            print(CLEAR)
        print(f"Alarm will go in: {min_left:02d}:{sec_left:02d}")
    
    while True:
        if not STOP:
            playsound("c:/Users/91823/Desktop/python/alarm/alarm23.mp3")
        else:
            break

def stop_alarm(second):
    time.sleep(second+1)
    global STOP
    while True:
        capcha = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',
          '1','2','3','4','5','6','7','8','9','0']

        choose=random.choices(capcha,k=6)
        choose_str="".join(choose)
        print(f"CAPCHA : "+choose_str)
        c=0
        while True:
            user_input=input("Enter the above capcha: ")
            if user_input==choose_str:
                    STOP=True
                    c=1
                    break
            else:
                    print("Please re-enter the capcha")
        
        if c==1:
            break

minutes = int(input("Enter the number of minutes: "))
second=int(input("Enter the number of seconds: "))
total_seconds = minutes * 60 + second

t1=threading.Thread(target=alarm,args=(total_seconds,))
t2= threading.Thread(target=stop_alarm,args=(total_seconds,))

t1.start()
t2.start()

t1.join()
t2.join()

print("GOOD MORNING SWEETHEART :) ")