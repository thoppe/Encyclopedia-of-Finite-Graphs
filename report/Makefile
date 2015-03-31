PROJECT_NAME = report
SPELL_CHECK  = aspell check $(SPELL_ARGS) -t

TARGETS = $(PROJECT_NAME).pdf

all: $(TARGETS)
	-make view

view:
	evince $(PROJECT_NAME).pdf &

edit:
	emacs $(PROJECT_NAME).tex &

editrefs:
	emacs refs.bib &

clean:
	rm -vf *.aux *.pdf *.log *~ *.bbl *.blg *.out \#* *.bak *.tdo

commit:
	(cd .. && make commit)

package:
	rm -vf packaged_report.tar
	tar -cvf packaged_report.tar refs.bib report.tex ex_query.png combined_subgraphs.png


$(PROJECT_NAME).pdf: $(PROJECT_NAME).tex refs.bib
	make clean
	$(SPELL_CHECK) $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
	bibtex $(PROJECT_NAME).aux
	pdflatex $(PROJECT_NAME).tex
	pdflatex $(PROJECT_NAME).tex
