import sqlite3
import itertools, os, logging

def generate_database_name(N):
    return os.path.join("database", "graph{}.db".format(N))  

def load_graph_database(N, check_exist=True):
    ''' Given an input value of N, return a connection to the 
        cooresponding database '''

    f_database = generate_database_name(N)

    # Check if database exists, if so exit!
    if check_exist and not os.path.exists(f_database):
        err = "Database %s does not exist."%f_database
        logging.critical(err)
        exit()
    
    return sqlite3.connect(f_database, check_same_thread=False)
    

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
