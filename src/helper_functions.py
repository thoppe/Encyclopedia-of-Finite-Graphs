import gc
import csv
import os
import errno
import json
import itertools
import logging
import multiprocessing
from contextlib import contextmanager

from functools import wraps


def require_arguments(*reqargs):
    ''' Decorator to check for optional arguments of a function '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            err_msg = "{} requires argument {}"
            for arg in reqargs:
                if not arg in kwargs:
                    raise TypeError(err_msg.format(func,arg))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def load_options(f_option_file):
    # Load the file into a string
    try:
        with open(f_option_file) as FIN:
            raw_text = FIN.read()
    except:
        msg = "Couldn't find option file {}".format(f_option_file)
        raise IOError(msg)

    # Parse the text as json
    try:
        return json.loads(raw_text)
    except Exception as Ex:
        msg = "Couldn't parse JSON file {}, {}".format(f_option_file, Ex)
        raise IOError(msg)


def get_database_graph(options):
    fname = "{graph_types}_graphs_{N}.h5"
    return os.path.join("database",fname.format(**options))

def get_database_special(options):
    fname = "{graph_types}_special_{N}.h5"
    return os.path.join("database",fname.format(**options))


def graph_iterator(graphs, N, offset=0, chunksize=1000):   
    for i in xrange(offset, graphs.shape[0], chunksize):
        for rep in graphs[i:i+chunksize]:
            yield {"packed_representation":rep,"N":N}


'''

def generate_database_name(N):
    return os.path.join("database", "graph{}.db".format(N))


def generate_special_database_name(N):
    return os.path.join("database", "special", "graph{}_special.db".format(N))


def generate_distinct_sequence_database_name():
    return os.path.join("database", "distinct_seq.db")


def load_distinct_database(check_exist=True, timeout=5):

    f_database = generate_distinct_sequence_database_name()

    # Check if database exists, if so exit!
    if check_exist and not os.path.exists(f_database):
        err = "Database %s does not exist." % f_database
        logging.critical(err)
        exit()

    return sqlite3.connect(f_database, check_same_thread=False,
                           timeout=timeout)


def load_graph_database(N, check_exist=True, special=False, timeout=5):
    '' Given an input value of N, return a connection to the
        cooresponding database ''

    # Build the needed directories
    mkdir_p("database")
    mkdir_p("database/special")

    if not special:
        f_database = generate_database_name(N)
    else:
        f_database = generate_special_database_name(N)

    # Check if database exists, if so exit!
    if check_exist and not os.path.exists(f_database):
        err = "Database %s does not exist." % f_database
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
    cmd_attach = ''ATTACH database "{}" AS "{}"''
    conn.execute(cmd_attach.format(f_attach, as_name))

# Helper function to grab all data


def grab_all(connection, cmd, *args):
    return connection.execute(cmd, *args).fetchall()

# Helper functions to grab a vector of data


def grab_vector(connection, cmd, *args):
    return [x[0] for x in connection.execute(cmd, *args).fetchall()]

# Helper function to only grab a scalar, like COUNT(*)
def grab_scalar(connection, cmd, *args):
    cursor = connection.execute(cmd, *args)
    return cursor.next()[0]

# Helper function to get the column names


def grab_col_names(connection, table):
    cmd = ''SELECT * FROM {} LIMIT 1;''.format(table)
    cursor = connection.execute(cmd)
    return [x[0] for x in cursor.description]

# def landing_table_itr(f_landing_table, index_args, max_iter=50000):
#    with open(f_landing_table,'r') as FIN:
#        for group in grouper(FIN,max_iter):
#            VALS = []
#            for item in group:
#                ix = item.strip().split()
#                val = [ix[n] for n in index_args]
#                VALS.append(val)
#            yield VALS
'''

######################################################################

@contextmanager
def parallel_compute(data_ITR, func, debug=False):
    if debug:
        pfunc = itertools.imap
    else:
        P     = multiprocessing.Pool()
        pfunc = P.imap
    yield pfunc(func,data_ITR)
    
    if not debug:
        P.close()
        P.join()
        P.terminate()
        del P
        
