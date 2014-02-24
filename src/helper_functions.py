import itertools

def select_itr(conn, cmd, chunksize=100):  
    ''' Creates an iterator over an SQL query so the
        result isn't spammed in memory '''

    itr = conn.execute(cmd)
    while True:
        results = itr.fetchmany(chunksize)
        if not results:         break
        for result in results:  yield result      

def grouper(iterable, n):
    ''' Groups an iterator into chunks of at most size n '''
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

    
def load_template(f_template):
    ''' Loads a file into a list and skips "# comments" '''
    template = []
    with open(f_template) as FIN:
        for line in FIN:
            line = line.strip()
            if line and line[0][0] != "#":
                template.append(line)
    return template
