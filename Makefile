all: cv.yaml cv.private.yaml
	php -c bin/php.ini bin/gen.php
	cd tex; xelatex -recorder cv.tex

clean:
	$(RM) tex/cv.aux  tex/cv.log  tex/cv.out tex/cv.tex tex/cv.pdf tex/cv.fls 

install:
	apt-get install xelatex xargs
	cat apt-packages.txt | xargs apt-get install

freeze: all
	cat ./tex/cv.fls | xargs dlocate --package-only | sort -u > apt-packages.txt
