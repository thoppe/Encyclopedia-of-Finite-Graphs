test_N = 9

all:
	rm -vf database/graph$(test_N).db
	time python src/generate_db.py $(test_N)
	time python src/update_schema.py $(test_N)
	time python src/update_invariants.py $(test_N)

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