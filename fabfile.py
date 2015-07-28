from fabric.api import *

args = {}
args["N"] = 4
args["debug"]   = "-d"
args["verbose"] = "-v"
args["force"]   = "-f"

args["calc_exec"] = "python EoGF/update_invariants.py"
options = " -d -v "

@task
def push():
    # Helper functions for development
    local("git status")
    local("git commit -a")
    local("git push")

@task
def commit():
    test()
    push()

@task
def generate():
    cmd = "python EoGF/update_graphs.py {N} -f"
    local(cmd.format(**args))
    
@task
def clean():
    local("rm -vf database/*{N}*".format(**args))
    local("find . -name '*.pyc' | xargs -I {} rm -v {}")
    local("find . -name '*~' | xargs -I {} rm -v {}")

@task
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
    local("nosetests-2.7 -s -v")


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

    
    
