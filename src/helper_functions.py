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
    msg = ("Shutting down processes. Will exit with a NameError "
           "after timeout.")
    print msg
    raise NotARealError

# Register SIGINT handler function
signal.signal(signal.SIGINT, siginthndlr) 

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
        msg = "Couldn't parse JSON file {}, {}"
        raise IOError(msg.format(f_option_file, Ex))


def get_database_graph(options):
    fname = "{graph_types}_graphs_{N}.h5"
    fname = os.path.join("database",fname.format(**options))
    return fname

def get_database_invariants(options):
    fname = "{graph_types}_{N}_invariants.h5"
    fname = os.path.join("database",fname.format(**options))
    return fname

def get_database_sequence(options):
    fname = "{graph_types}_sequence.h5"
    fname = os.path.join("database",fname.format(**options))
    return fname

def is_invariant_calc_complete(name, invariant_db):
    
    if name not in invariant_db:
        return False
    
    dset = invariant_db[name]
    gn   = dset.shape[0]
    offset = dset.attrs["compute_start"]
    remaining_n = gn-offset
    return not remaining_n

class graph_iterator(object):
    '''
    Iterates over the graphs and adds in any requested invariants.
    '''
    
    def __init__(self, graph_db, N, invariant_db,
                    offset=0, chunksize=1000,
                    requirement_db_list=[]):
    
        gn = graph_db.shape[0]
        self.N  = N
        self.G = chunked_iterator(graph_db,gn,offset,chunksize)
        self.ITRS = {"twos_representation":self.G}
        
        for name in requirement_db_list:

            # Check that invariant requirements have been met
            if not is_invariant_calc_complete(name, invariant_db):
                raise KeyError(name)

            # Add in the invariant
            dset = invariant_db[name]
            self.ITRS[name] = chunked_iterator(dset,gn,offset,chunksize)

    def __iter__(self):
        return self

    def next(self):

        while self.G:
            item = {"N":self.N}
            for key in self.ITRS:
                item[key] = self.ITRS[key].next()
            return item

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
        

######################### Visualization code ##############################

def viz_graph(g, pos=None, **kwargs):
    if pos is None:
        pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
    graph_tool.draw.graph_draw(g, pos, **kwargs)


