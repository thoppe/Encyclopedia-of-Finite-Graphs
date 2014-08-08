# Debugging/Testing commands

test_N = 9
all:
	python src/generate_graphs.py $(test_N)
	python src/update_special2.py $(test_N)
	python src/update_invariants.py $(test_N)
	python src/build_distinct_seq.py $(test_N)
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

max_n = 10
possible_N_values = $(shell seq 1 ${max_n})

build:
	make generate
	make compute
	make sequence

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
	python verification/raw_dump_relations.py $(max_n)

########################################################################

package:
	tar -cvf simple_connected_graphs_n10.tar database/* --exclude database/special
	pbzip2 simple_connected_graphs_n10.tar

options:
	emacs templates/ref_invariant_integer.json &

test:
	python src/unit_tests.py --max_n 7

commit:
	-@make push

push:
#	-@make all
	git add -u
	git status
	-git commit
	git push
pull:
	git pull

full_clean:
	rm -rvf database/*

compile:
	(cd src/bliss && make gmp)
	(cd src/independent_edge_sets && make)
	(cd src/independent_vertex_sets && make)
