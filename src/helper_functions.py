import sqlite3, gc, csv, os, errno
import itertools, os, logging, multiprocessing

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def generate_database_name(N):
    return os.path.join("database", "graph{}.db".format(N))  

def generate_special_database_name(N):
    return os.path.join("database", "special", "graph{}_special.db".format(N))  

def load_graph_database(N, check_exist=True, special=False,timeout=5):
    ''' Given an input value of N, return a connection to the 
        cooresponding database '''
    
    # Build the needed directories
    mkdir_p("database")
    mkdir_p("database/special")

    if not special:
        f_database = generate_database_name(N)
    else:
        f_database = generate_special_database_name(N)

    # Check if database exists, if so exit!
    if check_exist and not os.path.exists(f_database):
        err = "Database %s does not exist."%f_database
        logging.critical(err)
        exit()

    return sqlite3.connect(f_database, check_same_thread=False,
                           timeout=timeout)

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
def grab_all(connection, cmd,*args):
    return connection.execute(cmd,*args).fetchall()

# Helper functions to grab a vector of data
def grab_vector(connection, cmd,*args):
    return [x[0] for x in connection.execute(cmd,*args).fetchall()]

# Helper function to only grab a scalar, like COUNT(*)
def grab_scalar(connection, cmd,*args):
    return [x[0] for x in connection.execute(cmd,*args).fetchall()][0]

# Helper function to get the column names
def grab_col_names(connection, table):
    cmd = '''SELECT * FROM {} LIMIT 1;'''.format(table)
    cursor = connection.execute(cmd)
    return [x[0] for x in cursor.description]

def landing_table_itr(f_landing_table, index_args, max_iter=50000):
    with open(f_landing_table,'r') as FIN:
        for group in grouper(FIN,max_iter):
            VALS = []
            for item in group:
                ix = item.strip().split()
                val = [ix[n] for n in index_args]
                VALS.append(val)
            yield VALS
    

def select_itr(conn, cmd, chunksize=5000):  
    ''' Creates an iterator over an SQL query so the
        result isn't spammed in memory '''

    itr = conn.execute(cmd)

    while True:
        results = itr.fetchmany(chunksize)

        if not results:         break
        for result in results:  
            yield result      


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

    if "CORES" not in cargs:
        processes = multiprocessing.cpu_count()
    else:
        processes = cargs["CORES"]
            
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
                print "HERE!",args, func
                
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

########################################################################

def csv_validator(contents, cmd_insert):
    # Check for the extra bit written at the end
    expected_args = len([x for x in cmd_insert if x=="?"]) + 1
    for item in contents:
        if len(item) == expected_args:
            yield item[:-1]
    
def import_csv_to_table(f_csv, table, cmd_insert):
    with open(f_csv) as csvfile:
        contents = csv.reader(csvfile, delimiter=',')
        valid_contents = csv_validator(contents,cmd_insert)
        table.executemany(cmd_insert, valid_contents)

def compute_parallel(
        function_name, 
        connection,
        pfunc, cmd_insert, targets,N):

    f_landing_table = os.path.join("landing_table_{}_{}"
                                   .format(function_name,N))

    if os.path.exists(f_landing_table):
        logging.info("Saving from landing table {}".format(f_landing_table))
        import_csv_to_table(f_landing_table, connection,cmd_insert)
        connection.commit()
        os.remove(f_landing_table)

    P = multiprocessing.Pool()
    sol = P.imap(pfunc,targets)
    cmd_insert = cmd_insert.format(function_name)
    FOUT = open(f_landing_table,'w')

    for k, (g_id, terms) in enumerate(sol):
        cmd = cmd_insert.format(function_name, g_id)
        for item in terms:
            s  = ','.join(["{}"]*(len(item) + 1))
            s  = s.format(g_id, *item)
            s += ',1\n'  # Validator bit
            FOUT.write(s)
        
        if k and k%5000==0:
            msg ="Saving {} graphs ({})".format(function_name,k)
            logging.info(msg)
            FOUT.flush()
            os.fsync(FOUT.fileno())

    FOUT.close()

    if os.path.exists(f_landing_table):
        logging.info("Saving from landing table {}".format(f_landing_table))
        import_csv_to_table(f_landing_table, connection, cmd_insert)
        connection.commit()
        os.remove(f_landing_table)
