# Debugging/Testing commands

test_N = 5
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


possible_N_values = 1 2 3 4 5 6 7 8 9 10

build:
	make generate
	make compute
	make sequence

generate:
	$(foreach n,$(possible_N_values),python src/generate_graphs.py $(n);)

compute:
	$(foreach n,$(possible_N_values),python src/update_special2.py $(n);)
	$(foreach n,$(possible_N_values),python src/build_distinct_seq.py $(n);)
	$(foreach n,$(possible_N_values),python src/update_invariants.py $(n);)

sequence:
	python src/build_sequence.py --max_n 10
	python src/build_relations.py --max_n 10
	python verification/raw_dump_relations.py

########################################################################

test:
	python src/unit_tests.py --max_n 8

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
