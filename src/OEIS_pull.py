import requests, json

OEIS_base_url = '''http://oeis.org/search'''

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


if __name__ == "__main__":
    seq_id = "A000109"
    print "Testing pull of", seq_id
    print pull_OEIS_seq_id(seq_id)
    print

    seq = [14,50,233,1249]
    print "Testing pull of", seq
    print json.dumps(pull_OEIS_seq_id(seq), indent=2)
    


