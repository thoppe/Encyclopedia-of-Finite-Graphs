
# Debugging/Testing commands

test_N = 5
all:
#	rm -vf database/graph$(test_N).db
	python src/generate_db.py $(test_N)
	python src/update_special.py $(test_N)
	python src/update_invariants.py $(test_N)

view:
	sqlitebrowser database/graph$(test_N).db
view_invariants:
	sqlitebrowser database/ref_invariant_integer.db
view_seq:
	sqlitebrowser database/sequence.db
view_ref:
	sqlitebrowser database/ref_invariant_integer.db

report_lvl1:
	python verification/lvl1_report.py > verification/raw_lvl1.txt


possible_N_values = 1 2 3 4 5 6 7 8 9 10

rebuild_database:
	$(foreach n,$(possible_N_values),python src/generate_db.py $(n);)
	make compute
#	make sequence
#	make package

compute:
	$(foreach n,$(possible_N_values),python src/update_special.py $(n);)
	$(foreach n,$(possible_N_values),python src/update_invariants.py $(n);)

sequence:
	python src/update_sequence.py 10

test:
	python src/unit_tests.py --max_n 8

package:
	tar -cf bak_database.tar database/
	pbzip2 -f bak_database.tar

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
	rm -vf database/*

compile:
	(cd src/bliss && make gmp)