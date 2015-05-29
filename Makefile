.PHONY: install freeze

install:
	apt-get install xelatex xargs
	cat apt-packages.txt | xargs apt-get install

freeze:
	cat ./build/tex/cv.fls | xargs dlocate --package-only | sort -u > apt-packages.txt
