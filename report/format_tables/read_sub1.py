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

def remove_numbers(name):
    word_names = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",
                    7:"seven",8:"eight",9:"nine",10:"ten"}
    for k,v in word_names.items():
        name = name.replace(str(k),v)
    return name
        

with open(f) as FIN:
    for line in FIN:
        if line.strip():
            output = []
            if "+" == line.strip()[0]:
                terms = line.split('`')
                OEIS = "\\OEIS{%s}" % terms[1]
                raw_name = remove_extra(terms[3])
                name, cond = split_name(raw_name)
                name = remove_numbers(name)

                # Modify what we are trying to display
                if "subgraphfree" in name:
                    if cond=="=0": cond = ">0"
                    elif cond=="=1": cond = "=0"
                        
                
                name = "$\\VAR%s %s$" % (name,cond)

                output = [OEIS, name]
                

                seq = terms[5]
                seq = seq.replace(',',' ').split()
                output = output + seq
                print ' & '.join(output) + ' \\\\'
            
        if "Unsubmitted" in line: break
