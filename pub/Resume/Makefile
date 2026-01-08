file=CV.tex # Default build file
#ifeq ($(findstring .,$(file)),.)
#    # Found
#    source=$(basename $(file))
#else
#    # Not found
#    source=$(file)
#endif
	
source=$(basename $(file))
CWD=$(PWD)
AUX = $(wildcard *.aux)
BIBTEX = $(echo %.aux,$(AUX))
all:
	#(cd Graph; make all)
	make --always-make acm
acm:
	# Compile using PDF-Latex
	make file=$(source) single
	make pub
pub:
	make file=ListofPublication.tex single
ieee:
	# Compile using DVI->PS->PDF
	latex -interaction=nonstopmode $(source).tex
	make bibtex
	latex -interaction=nonstopmode $(source).tex
	dvips -o $(source).ps $(source).dvi
	ps2pdf $(source).ps
embeded:
	gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dEmbedAllFonts=true -sOutputFile=$(source).embed.pdf -f $(source).pdf
greyscale:
	gs -sOutputFile=$(source).greyscale.pdf -dEmbedAllFonts=true -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray  -dCompatibilityLevel=1.4  -dNOPAUSE  -dBATCH $(fileName).embed.pdf
check:
	pdffonts $(source).embed.pdf
clean : 
	rm -f *.aux *.bbl *.blg $(source).dvi $(source).ps 
	rm -f *.synctex.gz
	rm -f *.log *.loa *.lof *.lot *.los *.glsdefs *.nom
	rm -f *.nlo *.toc *.idx *.ilg *.ind *.nls *.out *.run.xml *-blx.bib
distclean :
	make clean
	rm -f $(source).pdf
	find . -type f -name '*eps-converted-to.pdf' -delete
cover:
	pdflatex C0_Cover.tex
	make clean
final:
	make embeded
	make greyscale
	make check
chapter: # Not Working Yet
	@echo "Tex file name:";
	@read -r -p line; 
	@echo "Input received:" $(fname)
	make file=$(fname) debug
bibtex:
	ls *.aux |xargs -n1 sh -c 'bibtex $$1' sh
single:
	source=$(basename $(file))
	$(info [source,file] is [${source},${file}])
	pdflatex -synctex=1 -interaction=nonstopmode $(source) || exit 0
	biber $(source)
	pdflatex -synctex=1 -interaction=nonstopmode $(source) || exit 0
	pdflatex -synctex=1 -interaction=nonstopmode $(source) || exit 0
	#pdflatex -synctex=1 -interaction=nonstopmode $(source).tex || exit 0	# Faltu error in kile
	#make bibtex
	#makeindex $(source).nlo -s nomencl.ist -o $(source).nls
	#pdflatex -synctex=1 -interaction=nonstopmode $(source).tex || exit 0	# Faltu error in kile
debug:
	source=$(basename $(file))
	$(info [source,file] is [${source},${file}])	
