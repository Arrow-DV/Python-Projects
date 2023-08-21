# Python Timer Project 2023/8/21 Made By Ali Hany
def flush():
    os.system("cls") # Clear Console Before Doing Anything -- Optinoal
# Import Needed Libary's
import os,time,winsound
# Make Variables And Functions
flush()
_timer_ = int(input("How Many Minutes : "))
flush()
def sleep(clock):
    while (clock * 60) != 0:
        for char in f"{clock} Mintue's Left!":
            print(char,end="",flush=True)
            time.sleep(.3)
        time.sleep(59.1)
        flush()
        clock -= 1
sleep(_timer_)
flush()
print("Time Out!")
winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)
