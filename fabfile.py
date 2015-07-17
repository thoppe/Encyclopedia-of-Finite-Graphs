from fabric.api import *

def push():
    # Helper function for development
    local("git status")
    local("git commit -a")
    local("git push")

def gen():
    cmd = "python src/update_graphs.py 4 -f"
    local(cmd)

def polynomial():
    local("python src/update_special.py 4 -f -v -d -i polynomial")

def fraction():
    local("python src/update_special.py 4 -f -d -v -i fraction")

def integer():
    local("python src/update_special.py 4 -f -d -v -i integer")

def boolean():
    local("python src/update_special.py 4 -f -d -v -i boolean")


    
    
