
INFILE = freqdist.md
OUTFILE = freqdist.pdf
BIBTEX = freqdist.bib

PANDOC = pandoc
PANDOC_ARGS = -H kolita11.sty --bibliography $(BIBTEX) \
              --csl chicago-author-date.csl --variable fontsize=11pt
CONVERT = convert
CONVERT_ARGS = -density 250 -units PixelsPerInch

IMG_FILES := $(wildcard ../*.png)
PDF_FILES := $(patsubst %.png, %.pdf, $(IMG_FILES))

%.pdf: %.png
	$(CONVERT) $(CONVERT_ARGS) $< $(patsubst ../%.pdf, ./img-%.pdf, $@) 

all: $(OUTFILE)

$(OUTFILE): $(PDF_FILES)
	$(PANDOC) $(PANDOC_ARGS) $(INFILE) -o $(OUTFILE)

clean:
	rm -f $(patsubst ../%.pdf, img-%.pdf, $(PDF_FILES)) $(OUTFILE)
