from fabric.api import *

args = {}
args["N"] = 4
args["debug"] = "-d"
args["verbose"] = "-v"
args["force"] = "-f"

args["calc_exec"] = "python src/update_special.py"
options = " -d -v "

def push():
    # Helper function for development
    local("git status")
    local("git commit -a")
    local("git push")
def commit():
    push()

def generate():
    cmd = "python src/update_graphs.py {N} -f"
    local(cmd.format(**args))

def clean():
    local("rm -vf database/*{N}*".format(**args)) 

def test():
    args["verbose"] = ""
    clean()
    generate()
    polynomial()
    fraction()
    integer()
    boolean()


cmd_invar_calc = "{calc_exec} {N} {debug} {verbose} {force} -i {name}"

def polynomial():
    local(cmd_invar_calc.format(name="polynomial",**args))

def fraction():
    local(cmd_invar_calc.format(name="fraction",**args))

def integer():
    local(cmd_invar_calc.format(name="integer",**args))

def boolean():
    local(cmd_invar_calc.format(name="boolean",**args))

    
    
