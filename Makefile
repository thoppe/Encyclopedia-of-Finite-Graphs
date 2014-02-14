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

