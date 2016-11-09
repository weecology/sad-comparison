all: intro.pdf chapter1.pdf chapter1.docx chapter2.pdf chapter3.pdf summary.pdf

intro.pdf: intro.md intro_refs.bib format.sty
	pandoc -H format.sty -V fontsize=12pt --bibliography intro_refs.bib --csl=ecology.csl intro.md -o intro.pdf

chapter1.pdf: chapter1.md sad_comparison_refs.bib format.sty
	pandoc -H format.sty -V fontsize=12pt --bibliography sad_comparison_refs.bib --csl=ecology.csl chapter1.md -o chapter1.pdf

chapter1.docx: chapter1.md sad_comparison_refs.bib format.sty
	pandoc -H format.sty -V fontsize=12pt --bibliography sad_comparison_refs.bib --csl=ecology.csl chapter1.md -o chapter1.docx

chapter2.pdf: chapter2.md miscDB_combined_refs.bib format.sty
	pandoc -H format.sty -V fontsize=12pt --bibliography miscDB_combined_refs.bib --csl=ecology.csl chapter2.md -o chapter2.pdf

chapter3.pdf: chapter3.md neutral_comparison_refs.bib format.sty
	pandoc -H format.sty -V fontsize=12pt --bibliography neutral_comparison_refs.bib --csl=ecology.csl chapter3.md -o chapter3.pdf

summary.pdf: summary.md summary_refs.bib format.sty
	pandoc -H format.sty -V fontsize=12pt --bibliography summary_refs.bib --csl=ecology.csl summary.md -o summary.pdf

miscDB_combined_refs: miscDB_paper_refs.bib miscDB_refs.bib
	cat miscDB_paper_refs.bib miscDB_refs.bib > miscDB_combined_refs.bib
