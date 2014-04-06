import sqlite3, gc
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

def load_sql_script(conn, f_script):

    with open(f_script) as FIN:
        script = FIN.read()
        conn.executescript(script)
        conn.commit()

def attach_table(conn, f_attach, as_name):
    cmd_attach = '''ATTACH database "{}" AS "{}"'''
    conn.execute(cmd_attach.format(f_attach,as_name))

def attach_ref_table(conn):
    ''' 
    Attaches the master invariant reference table to the connection.
    Additionally, builds/updates the table from the template '''
    
    f_ref = os.path.join("database","ref_invariant_integer.db")

    f_ref_template = os.path.join("templates",
                                  "ref_invariant_integer.sql")

    ref_conn = sqlite3.connect(f_ref)         
    load_sql_script(ref_conn, f_ref_template)
    ref_conn.close()

    attach_table(conn, f_ref, "ref_db")

# Helper function to grab all data
def grab_all(connection, cmd):
    return connection.execute(cmd).fetchall()

# Helper functions to grab a vector of data
def grab_vector(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()]

# Helper function to only grab a scalar, like COUNT(*)
def grab_scalar(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()][0]

def landing_table_itr(f_landing_table, index_args, max_iter=50000):
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

    max_size = 100
    dump_size = cargs["chunksize"]
    processes = multiprocessing.cpu_count()
    
    Q_IN  = multiprocessing.Queue(max_size)
    Q_OUT = multiprocessing.Queue()

    def handle_CB(results):
        if callback != None:
            callback(results)

    def worker(q_in, q_out):
        
        while True:

            # Grab an item from the queue
            try:
                k,args = q_in.get()
            except Exception as ex:
                print "FAIL?", ex

            # Break on final arg
            if args == "COMPLETED": break

            # Process the item
            try:
                val  = func(args)
                # Add to result list

            except Exception as ex:
                err = "Error on function %s"%ex
                raise SyntaxError(err)
                return False
        
            q_out.put(val)

        return True
                         
    # Start the processes
    P = []
    for _ in range(processes):
        proc = multiprocessing.Process(target=worker,
                                       args=(Q_IN,Q_OUT))
        proc.damon = True
        proc.start()
        P.append(proc)

    # Keep track of what has been added
    counter = 0
        
    for k,g in enumerate(itr):
        Q_IN.put((k,g))
        counter += 1

        while Q_OUT.qsize() >= dump_size:
            results = [Q_OUT.get() for _ in xrange(dump_size)]
            counter -= dump_size
            handle_CB(results)
            gc.collect()

    # Signal the End
    for _ in range(processes):
        Q_IN.put((None,"COMPLETED"))

    Q_IN.close()
    Q_IN.join_thread()

    while counter > dump_size:
        results = [Q_OUT.get() for _ in xrange(dump_size)]
        counter -= dump_size
        handle_CB(results)

    final_results = [Q_OUT.get() for _ in xrange(counter)]
    handle_CB(final_results)

    # Need to properly check for errors
    return True
