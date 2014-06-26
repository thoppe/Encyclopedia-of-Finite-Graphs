f = "verification/submission_lvl1.md"

extra = "[]_"
def remove_extra(s):
    for ex in extra:
        s = s.replace(ex,"")
    return s

def split_name(name):
    
    for n in xrange(len(name)):
        if name[n] in "=<>":
            return name[:n], name[n:]


with open(f) as FIN:
    for line in FIN:
        if line.strip():
            output = []
            if "+" == line.strip()[0]:
                terms = line.split('`')
                OEIS = "\\OEIS{%s}" % terms[1]
                raw_name = remove_extra(terms[3])
                name, cond = split_name(raw_name)
                name = "$\\VAR%s %s$" % (name,cond)

                output = [OEIS, name]

                seq = terms[5]
                seq = seq.replace(',',' ').split()
                output = output + seq
                print ' & '.join(output) + ' \\\\'
            
        if "Unsubmitted" in line: break
