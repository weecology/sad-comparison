all: chapter1.pdf

chapter1.pdf: chapter1.md sad_comparison_refs.bib
	pandoc -H format.sty -V fontsize=12pt --bibliography sad_comparison_refs.bib --csl=ecology.csl chapter1.md -o chapter1.pdf
