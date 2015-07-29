from fabric.api import *

# These arguments are for testing
args = {}
args["testing_N"] = 4
args["debug"]   = "-d"
args["verbose"] = "-v"
args["force"]   = "-f"

# Don't build the third order sequences by default
args["second_order_flag"] = ""
args["third_order_flag"] = ""

args["calc_exec"]       = "python EoGF/update_invariants.py"
args["calc_generate"]   = "python EoGF/update_graphs.py"
args["calc_invariants"] = "python EoGF/update_invariants.py"
options = " -d -v "

@task
def generate():
    cmd = "{calc_generate} {testing_N} -f"
    local(cmd.format(**args))

@task
def invariants():
    all_invariants(args["testing_N"])

@task
def sequences():
    local("python EoGF/build_sequences.py -f {second_order_flag} "
          " {third_order_flag}".format(**args))
    local("python EoGF/build_sequence_db.py")

@task
def review():
    local("python EoGF/verification/review_sequences.py")

# Push/commit are helper functions for development
@task
def push():
    local("git status")
    local("git commit -a")
    local("git push")

@task
def commit():
    test()
    push()

@task
def clean():
    local("rm -vf database/*{testing_N}*".format(**args))
    local("find . -name '*.pyc' | xargs -I {} rm -v {}")
    local("find . -name '*~' | xargs -I {} rm -v {}")

#######################################################################

cmd_invar_calc = "{calc_exec} {N} {debug} {verbose} {force} -i {name}"
def all_invariants(N):
    polynomial(N)
    fraction(N)
    integer(N)
    boolean(N)
    subgraph(N)

def polynomial(N):
    local(cmd_invar_calc.format(N=N,name="polynomial",**args))

def fraction(N):
    local(cmd_invar_calc.format(N=N,name="fraction",**args))

def integer(N):
    local(cmd_invar_calc.format(N=N,name="integer",**args))

def boolean(N):
    local(cmd_invar_calc.format(N=N,name="boolean",**args))

def subgraph(N):
    local(cmd_invar_calc.format(N=N,name="subgraph",**args))

def zeros(N):
    local(cmd_invar_calc.format(N=N,name="zeros",**args))

#######################################################################
    
@task
def test():
    args["verbose"] = ""
    args["debug"]   = ""
    args["force"]   = ""
    clean()
    generate()
    all_invariants(args["testing_N"])
    local("nosetests-2.7 -s -v")
