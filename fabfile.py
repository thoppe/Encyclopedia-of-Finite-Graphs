from fabric.api import *

options = " -d -v "

def push():
    # Helper function for development
    local("git status")
    local("git commit -a")
    local("git push")

def gen():
    cmd = "python src/update_graphs.py 4 -f"
    local(cmd)

def test():
    polynomial()
    fraction()
    integer()
    boolean()

def polynomial():
    local("python src/update_special.py 4 {} -i polynomial".format(options))

def fraction():
    local("python src/update_special.py 4 -d -v -i fraction")

def integer():
    local("python src/update_special.py 4 -d -v -i integer")

def boolean():
    local("python src/update_special.py 4 -d -v -i boolean")


    
    
