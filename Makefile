test_N = 5

all:
	python src/generate_db.py $(test_N)
	python src/update_schema.py $(test_N)

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