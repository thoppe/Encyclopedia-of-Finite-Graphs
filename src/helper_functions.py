import sqlite3
import itertools, os, logging, multiprocessing

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

def landing_table_itr(f_landing_table, index_args, max_iter=10000):
    with open(f_landing_table,'r') as FIN:
        for group in grouper(FIN,max_iter):
            VALS = []
            for item in group:
                ix = item.strip().split()
                val = [ix[n] for n in index_args]
                VALS.append(val)
            yield VALS
    

def select_itr(conn, cmd, chunksize=1000):  
    ''' Creates an iterator over an SQL query so the
        result isn't spammed in memory '''

    count = 0
    itr = conn.execute(cmd)

    while True:
        results = itr.fetchmany(chunksize)

        if not results:         break
        for result in results:  
            yield result      
            count += 1

    #logging.info("Selected {} results".format(count))



def grouper(iterable, n):
    ''' Groups an iterator into chunks of at most size n '''
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk


def parallel_compute(itr, func, callback=None, **cargs):
    ''' 
    Helper to compute a function over the graphs in parallel. Uses a 
    grouper to prevent loading too much into memeory at one time.
    Returns True/False if any exceptions have been called.
    '''

    allocator = grouper(itr, cargs["chunksize"])

    if "CORES" in cargs:
        P = multiprocessing.Pool(cargs["CORES"])
    else:
        P = multiprocessing.Pool()

    map_args = {"chunksize":20}
    if callback!=None:
        map_args["callback"] = callback

    results = [P.map_async(func, gitr, **map_args) for
               gitr in allocator]

    P.close()
    P.join()

    # Cycle through the results and see if any exceptions have been called
    for x in results:
        if not x.successful():
            return False

    return True

    

