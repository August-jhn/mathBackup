
print("""this little program is designed to move all files of a certain type to a designated location
a tree depth can also be specified, though it defaults to 10
all files of the type specified will be moved to a lcoation which can also be specfied""")

import subprocess
import os

MAXDEPTH = 10

maxdepth = MAXDEPTH

print("Enter a relative path:")
path = input()
print("enter a target directory:")
target = input()

if input("Would you like to specify a recursion depth? Type y if yes").upper() == "Y":
    maxdepth = input("Depth: ")
else:
    maxdepth = MAXDEPTH

dirs = os.listdir()

moved = 0

def search(dirs, depth, dir):

    for d in dirs:
        folder = os.path.isdir(d)
        file = os.path
        if folder:
            print("   "*depth + "folder: ", d)
            if depth <= maxdepth:
                search(os.listdir(dir + "/" + d), depth + 1, dir + "/" + d)
        if file:
            print("   "*depth + "file: ", d)

search(dirs, 0, "")

