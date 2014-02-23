test_N = 5

all:
	rm -vf database/graph$(test_N).db
	time python src/generate_db.py $(test_N)
	python src/update_schema.py $(test_N)
	time python src/update_invariants.py $(test_N)

possible_N_values = 1 2 3 4 5 6 7 8 9 10
rebuild_database:
	$(foreach n,$(possible_N_values),python src/generate_db.py $(n);)
	$(foreach n,$(possible_N_values),python src/update_schema.py $(n);)

compute:
	$(foreach n,$(possible_N_values),time python src/update_invariants.py $(n);)


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