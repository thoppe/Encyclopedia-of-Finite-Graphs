import logging
import argparse
import os
import collections
from helper_functions import load_graph_database, grab_all

desc = "Remove an invariant calculation from the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('remove_function_list', type=str, nargs="+")
parser.add_argument('--special', default=False, action='store_true')
parser.add_argument('--purge',   default=False, action='store_true',
                    help="Remove column from database (rebuild req.)")
parser.add_argument('--max_n', type=int, default=10,
                    help="Maximum graph size n to remove invariant")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)


script_purge_columns = '''
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE {name}_backup({existing_columns});
INSERT INTO {name}_backup SELECT {existing_columns} FROM {name};
DROP TABLE {name};
CREATE TABLE {name}({existing_columns});
INSERT INTO {name} SELECT {existing_columns} FROM {name}_backup;
DROP TABLE {name}_backup;
COMMIT;
'''

cmd_grab_column_names = '''PRAGMA table_info("{}")'''

cmd_remove_invariant = '''
UPDATE invariant_integer
SET {} = NULL'''

cmd_remove_computed = '''
DELETE FROM computed
WHERE function_name = "{}" '''

cmd_remove_special_invariant = '''DELETE FROM {}'''


def remove_invariant(name, conn):
    conn.execute(cmd_remove_invariant.format(name, name))
    conn.execute(cmd_remove_computed.format(name))


def remove_special_invariant(name, conn):
    conn.execute(cmd_remove_special_invariant.format(name))
    conn.execute(cmd_remove_computed.format(name))

if not cargs["special"]:

    graph_conn = collections.OrderedDict()
    for n in range(1, cargs["max_n"] + 1):
        graph_conn[n] = load_graph_database(n)

    if not cargs["purge"]:
        for n, conn in graph_conn.items():
            for function_name in cargs["remove_function_list"]:
                msg = "Starting removal of {} from graph database {}"
                logging.info(msg.format(function_name, n))
                remove_invariant(function_name, conn)
            conn.commit()


    if cargs["purge"]:

        existing_columns = []
        for item in grab_all(graph_conn[1], 
                             cmd_grab_column_names.format("invariant_integer")):
            existing_columns.append(item[1])

        remaining_columns = [c for c in existing_columns 
                             if c not in cargs["remove_function_list"]]
        cols = ','.join(remaining_columns)
        cmd = script_purge_columns.format(name="invariant_integer",
                                          existing_columns=cols)
        for n, conn in graph_conn.items():
            msg = "Purging graph database {}"
            logging.info(msg.format(n))
            conn.executescript(cmd)


    # Remove the sequence database as it may be corrupted
    # (will have to rebuild)
    f_sequence = os.path.join("database", "sequence.db")
    if os.path.exists(f_sequence):
        os.remove(f_sequence)
        logging.warning("Removed {}. Please rebuild.".format(f_sequence))

elif cargs["special"]:

    graph_conn = collections.OrderedDict()
    for n in range(1, cargs["max_n"] + 1):
        graph_conn[n] = load_graph_database(n, special=True)

    for n, conn in graph_conn.items():
        for function_name in cargs["remove_function_list"]:
            msg = "Starting removal of {} from graph database {}"
            logging.info(msg.format(function_name, n))
            remove_special_invariant(function_name, conn)
        conn.commit()
