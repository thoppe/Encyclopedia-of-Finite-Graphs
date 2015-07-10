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


import signal, sys

def siginthndlr(sig, frame):
    msg = "Shutting down processes. Will exit with a NameError after timeout."
    print msg
    raise NotARealError

signal.signal(signal.SIGINT, siginthndlr) #Register SIGINT handler function

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
    fname = "{graph_types}_invariants_{N}.h5"
    return os.path.join("database",fname.format(**options))


def graph_iterator(graphs, N, offset=0, chunksize=1000,
                   requirement_db_list=[]):

    gn = graphs.shape[0]
    
    G = chunked_iterator(graphs,gn,offset,chunksize)
    ITRS = {"twos_representation":G}

    for name, db in requirement_db_list:
        ITRS[name] = chunked_iterator(db,gn,offset,chunksize)

    while G:
        item = {"N":N}
        for key in ITRS:
            item[key] = ITRS[key].next()
        yield item

def chunked_iterator(ITR, ITR_n, offset=0, chunksize=10000):
    for i in xrange(offset, ITR_n, chunksize):
        for item in ITR[i:i+chunksize]:
            yield item
    
######################################################################

_global_pool_object = None

@contextmanager
def parallel_compute(data_ITR, func, debug=False,
                     chunksize=100, CORES=None):

    pfunc_args = {}
    
    if debug:
        pfunc = itertools.imap
    else:
        P     = multiprocessing.Pool(CORES)
        pfunc = P.imap
        pfunc_args["chunksize"] = chunksize
        
    try:
        yield pfunc(func,data_ITR,**pfunc_args)
        
    finally:        
        if not debug:
            P.close()
            P.join()
            P.terminate()
            del P
        

        
