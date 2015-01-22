all: cv.yaml cv.private.yaml
	php -c bin/php.ini bin/gen.php
	cd tex; xelatex cv.tex

clean:
	$(RM) tex/cv.aux  tex/cv.log  tex/cv.out tex/cv.tex tex/cv.pdf
