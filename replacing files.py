#moving fies and dirctory in py
import os 
source = "test.txt"
destination = "C:\\Users\\damie\\Downloads\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already file there")
    else: 
        os.replace(source,destination)
        print(source + "was moved")
except FileExistsError:
    print(source + "was not found")
    
