commit:
	-@make push

push:
	-@make all
	git status
	git add -A
	-git commit
	git push
pull:
	git pull

