import os
import time

# open files
if os.path.exists("source.mhtml"):
    print("here1")
    sourcefile = open("source.mhtml","r")
    source = str(sourcefile)
else:
    raise Exception("source.mhtml not found. Did you put it inside the project folder?")
print("Opened source.mhtml")
output = open("output.txt","r+")
print("Opened output.txt")
output.write("// Program start - "+time.ctime()+"\n")

# look for not statements
for x in sourcefile:
    if "quot" not in x:
        continue
    else:
        print("Found not condition! Printing to output...")
        output.write("Found not condition at "+x+" - "+time.ctime()+"\n")
print("Done.")
output.write("// Program end - "+time.ctime()+"\n")