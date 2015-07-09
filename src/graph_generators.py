import subprocess
import numpy as np

_nauty_geng_exec = 'src/nauty/geng'
_nauty_showg_exec = 'src/nauty/showg'

def nauty_simple_graph_itr(**args):
    ''' Creates a generator for all simple graphs using nauty '''

    cmd = "{geng} {N} -cq | {showg} -eq -l0"
    cmd = cmd.format(geng=_nauty_geng_exec,
                     showg=_nauty_showg_exec,
                     **args)

    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    while True:
        header_line = proc.stdout.readline()
        edge_line = proc.stdout.readline()
        if not header_line:
            break
        yield edge_line.strip()
