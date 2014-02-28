import requests, json

OEIS_base_url = '''http://oeis.org/search'''

import logging
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)

# Graph OEIS keywords will have "nonn" non-negative numbers

def strip_comments(text):
    text = [x for x in text.split('\n') if x and x[0] != "#"]
    return '\n'.join(text)

def jsonify_OEIS(text, show_extra=False):
    text = strip_comments(text)
    data = {}
    for line in text.split('\n'):
        if line[0] == "%":
            terms = line.split()
            line_type = terms[0][1:]
            seq_idx   = terms[1]
            line_info = line.partition(seq_idx)[2].strip()

            if seq_idx not in data:
                data[seq_idx] = {}
            if line_type not in data[seq_idx]:
                data[seq_idx][line_type] = []
            
            data[seq_idx][line_type] = line_info
            
        else:
            if show_extra:
                print line

    return data
   

def pull_OEIS_seq_id(OEIS_seq_id,**fmt_args):
    payload = {"q":"id:%s"%OEIS_seq_id,
               "fmt":"text"}
    r = requests.get(OEIS_base_url, params=payload)
    return jsonify_OEIS(r.text,**fmt_args)

def pull_OEIS_seq(seq,**fmt_args):
    ''' Expects a set of integers '''
    seq_text = str(seq)[1:-1]
    payload = {"q":"%s"%seq_text,
               "fmt":"text"}
    r = requests.get(OEIS_base_url, params=payload)
    return jsonify_OEIS(r.text,**fmt_args)

def pull_OEIS_bfile(OEIS_seq_id, **fmt_args):
    if OEIS_seq_id[0] != "A":
        msg = "Valid OEIS sequence ID start with A"
        raise SyntaxError(msg)
    seq = OEIS_seq_id[1:]
    url = "http://www.oeis.org/A{seq}/b{seq}.txt"
    r = requests.get(url.format(seq=seq))

    terms = []
    for line in strip_comments(r.text).split('\n'):
        try: 
            n,val = map(int,line.split())
        except Exception as ex:
            msg = "Problem with bfile %s, %s"%(r.url,ex)
            raise ValueError(msg)
        terms.append((n,val))

    return zip(*terms)


if __name__ == "__main__":
    seq_id = "A000109"

    print "Testing pull of", seq_id
    print pull_OEIS_seq_id(seq_id)
    print pull_OEIS_bfile(seq_id)
    print

    seq = [14,50,233,1249]
    print "Testing pull of", seq
    print json.dumps(pull_OEIS_seq_id(seq), indent=2)
    


