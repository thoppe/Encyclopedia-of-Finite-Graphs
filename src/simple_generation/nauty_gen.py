import os, sys, argparse, logging

desc = '''
Use nauty from the command line to generate all simple isomorphic graphs.
[INCOMPLETE]
'''.strip()

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int, help='Number of vertices')
cargs = vars(parser.parse_args())


def out_buff(buffer):
    line = ''.join(buffer).strip().split('\n')
    edge = ' '.join(line[2:])
    edge = edge.replace('  ',' ')
    print edge    

buffer = []
for x in sys.stdin.read():
    buffer.append(x)
    if len(buffer)>2 and buffer[-1]=='\n' and buffer[-2]=='\n':
        out_buff(buffer)
        buffer = []

out_buff(buffer)


cmd = "geng {N} -cq | showg -e"# | python buffer_showg.py > complete_edges_{N}"
print cmd.format(**cargs)
#os.system(cmd.format(N=N))
