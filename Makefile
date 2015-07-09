# Debugging/Testing commands
test_N = 4

max_n = 10
possible_N_values = $(shell seq 1 ${max_n})

all:
	python src/generate_graphs.py $(test_N)
	python src/update_special2.py $(test_N)
	python src/update_invariants.py $(test_N)
	python src/build_distinct_seq.py $(test_N)

# Must be called first
compile:
	pip install -r requirements.txt
	(cd src/bliss && make -j gmp)
	(cd src/independent_edge_sets && make -j)
	(cd src/independent_vertex_sets && make -j)
	(cd src/nauty/ && ./configure && make -j)

# Build all databases
build:
	make generate
	make compute
	make sequence

clean:
	rm -vf database/special/graph$(test_N)_special.db
	rm -vf database/graph$(test_N).db

view:
	sqlitebrowser database/graph$(test_N).db
view_seq:
	sqlitebrowser database/sequence.db
view_distinct:
	sqlitebrowser database/distinct_seq.db
view_special:
	sqlitebrowser database/special/graph$(test_N)_special.db

report_lvl1:
	python verification/lvl1_report.py > verification/raw_lvl1.md

generate:
	$(foreach n,$(possible_N_values),python src/generate_graphs.py $(n);)

compute:
	make special
	make distinct
	make invariants

special:
	$(foreach n,$(possible_N_values),python src/update_special2.py $(n);)

distinct:
	$(foreach n,$(possible_N_values),python src/build_distinct_seq.py $(n);)

invariants:
	$(foreach n,$(possible_N_values),python src/update_invariants.py $(n);)

sequence:
	python src/build_sequence.py --max_n $(max_n)
	python src/build_relations.py --max_n $(max_n)
	python verification/raw_dump_relations.py 

########################################################################

package:
	tar -cvf simple_connected_graphs_n10.tar database/* --exclude database/special
	pbzip2 simple_connected_graphs_n10.tar

option_file = "options_simple_connected.json"
options:
	emacs $(option_file) &

test:
	python src/unit_tests.py

full_clean:
	rm -rvf database/*

