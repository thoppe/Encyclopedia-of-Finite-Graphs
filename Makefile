test_N = 6

all:
	python src/generate_db.py $(test_N)
	python src/populate_simple_graphs.py $(test_N)

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

