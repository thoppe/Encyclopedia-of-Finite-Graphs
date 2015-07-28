all:
	echo "Makefile is only for compiling the src"
	echo "Use fabic [fab --list]"

# Must be called first
compile:
	pip install -r requirements.txt
	(cd EoGF/invariants/bliss && make -j gmp)
	(cd EoGF/invariants/independent_edge_sets && make -j)
	(cd EoGF/invariants/independent_vertex_sets && make -j)
	(cd EoGF/nauty/ && ./configure && make -j)

clean:
	(cd EoGF/invariants/bliss && make clean)
	(cd EoGF/invariants/independent_edge_sets && make clean)
	(cd EoGF/invariants/independent_vertex_sets && make clean)
	(cd EoGF/nauty/ && make clean)

# Build all databases
#build:
#	make generate
#	make compute
#	make sequence

#clean:
#	rm -vf database/special/graph$(test_N)_special.db
#	rm -vf database/graph$(test_N).db

#report_lvl1:
#	python verification/lvl1_report.py > verification/raw_lvl1.md

#generate:
#	$(foreach n,$(possible_N_values),python EoGF/generate_graphs.py $(n);)

#compute:
#	make special
#	make distinct
#	make invariants

#special:
#	$(foreach n,$(possible_N_values),python EoGF/update_special2.py $(n);)

#distinct:
#	$(foreach n,$(possible_N_values),python EoGF/build_distinct_seq.py $(n);)

#invariants:
#	$(foreach n,$(possible_N_values),python EoGF/update_invariants.py $(n);)

#sequence:
#	python EoGF/build_sequence.py --max_n $(max_n)
#	python EoGF/build_relations.py --max_n $(max_n)
#	python verification/raw_dump_relations.py 

########################################################################

#package:
#	tar -cvf simple_connected_graphs_n10.tar database/* --exclude database/special
#	pbzip2 simple_connected_graphs_n10.tar

option_file = "options_simple_connected.json"
options:
	emacs $(option_file) &

full_clean:
	rm -rvf database/*

