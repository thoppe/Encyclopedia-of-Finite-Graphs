PROJECT_NAME = report
SPELL_CHECK  = aspell check $(SPELL_ARGS) -t

TARGETS = $(PROJECT_NAME).pdf

all: $(TARGETS)
	-make view

view:
	evince $(PROJECT_NAME).pdf &

edit:
	emacs $(PROJECT_NAME).tex &

clean:
	rm -vf *.aux *.pdf *.log *~ *.bbl *.blg *.out

$(PROJECT_NAME).pdf: $(PROJECT_NAME).tex
	$(SPELL_CHECK) $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
	bibtex $(PROJECT_NAME).aux
	pdflatex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
