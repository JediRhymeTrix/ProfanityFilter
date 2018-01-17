from fabric.api import local


with open("hello.txt", "w") as f:
    f.write("Hello World!")


print "Entering bash..."
local("/bin/bash")
print "Goodbye!"