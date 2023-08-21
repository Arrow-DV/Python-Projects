# Made In 8/19/2023 By Ali Hany <3
# Vist Our Website https://arrow-dev.rf.gd/ For More Projects
# Last Update 8/19/2023

# Import Needed Libary's
import hashlib
from sys import argv as arg
# Make Variables
basic_hash  = arg[2] # The Given Hash
hash_length = len(basic_hash)
# Function To Read The File Hash
def read_hash():
    with open(arg[1],"rb") as file:
        global basic_hash,hash_length
        type = ""
        if hash_length == 32    : # MD5
            _hash_ = hashlib.md5() 
            type = "MD5"
        elif hash_length == 40  : # SHA-1
            _hash_ = hashlib.sha1()
            type = "SHA-1"
        elif hash_length == 64  : # SHA-256
            _hash_ = hashlib.sha256()
            type = "SHA-256"
        elif hash_length == 128 : # SHA-512
            _hash_ = hashlib.sha512()
            type = "SHA-512"
        else:
            print(f"{basic_hash} invaild Type Of Hash Please Make Sure You Type It Correct")
            exit()
        _hash_.update(file.read())
        _main_ = _hash_.hexdigest()
        print(f"Hash: {_main_}\nType: {type}")
        return _main_
# Check Sha Of Both
# ARG[0] -> Python File 
# ARG[1] -> The File  
# ARG[2] -> Given Hash
try:      
    if read_hash() == basic_hash:
        print("• Both Hash's Are Congruent •")
    else : print("• Hash's Not The The Same *UnSafe*! •")
except IndexError:
    print("Missing Values")
except FileNotFoundError:
    print("File Wasn't Found")
except Exception as err:
    print(f"{err}")
