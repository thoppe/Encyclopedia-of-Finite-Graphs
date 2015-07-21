from fabric.api import *

args = {}
args["N"] = 4
args["debug"]   = "-d"
args["verbose"] = "-v"
args["force"]   = "-f"

args["calc_exec"] = "python src/update_invariants.py"
options = " -d -v "

def push():
    # Helper function for development
    local("git status")
    local("git commit -a")
    local("git push")
def commit():
    test()
    push()

def generate():
    cmd = "python src/update_graphs.py {N} -f"
    local(cmd.format(**args))

def clean():
    local("rm -vf database/*{N}*".format(**args))
    local("find . -name '*.pyc' | xargs -I {} rm -v {}")
    local("find . -name '*~' | xargs -I {} rm -v {}")

def nose():
    local("nosetests-2.7 -s -v")


def test():
    args["verbose"] = ""
    args["debug"]   = ""
    args["force"]   = ""
    clean()
    generate()
    polynomial()
    fraction()
    integer()
    boolean()
    subgraph()
    nose()


cmd_invar_calc = "{calc_exec} {N} {debug} {verbose} {force} -i {name}"

def polynomial():
    local(cmd_invar_calc.format(name="polynomial",**args))

def fraction():
    local(cmd_invar_calc.format(name="fraction",**args))

def integer():
    local(cmd_invar_calc.format(name="integer",**args))

def boolean():
    local(cmd_invar_calc.format(name="boolean",**args))

def subgraph():
    local(cmd_invar_calc.format(name="subgraph",**args))

def zeros():
    local(cmd_invar_calc.format(name="zeros",**args))

    
    
