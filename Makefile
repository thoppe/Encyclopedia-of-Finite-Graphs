
# Debugging/Testing commands

test_N = 7
all:
	rm -vf database/graph$(test_N).db
	python src/generate_db.py $(test_N)
	python src/update_invariants.py $(test_N)
view:
	sqlitebrowser database/graph$(test_N).db

possible_N_values = 1 2 3 4 5 6 7
rebuild_database:
	$(foreach n,$(possible_N_values),python src/generate_db.py $(n);)
	make compute
	make sequence
	make package

compute:
	$(foreach n,$(possible_N_values),python src/update_invariants.py $(n);)

sequence:
	time python src/build_sequence.py

package:
	tar -cf bak_database.tar database/
	pbzip2 -f bak_database.tar

commit:
	-@make push

push:
	-@make all
	git add -A
	git status
	-git commit
	git push
pull:
	git pull




full_clean:
	rm -vf database/*