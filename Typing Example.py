import time
def print_v1(word):
    for char in word:
        print(char,end='', flush=True)
        time.sleep(.2)

print_v1("Hello World #EGYPT\n")