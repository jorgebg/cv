build/tex/cv.pdf: cv.md
	vagrant status | grep -E "default *running"
	vagrant rsync
	vagrant ssh -- "cd /vagrant && python3 -m cv pdf"
	vagrant ssh-config > ssh-config
	rsync -e "ssh -F ssh-config" -r vagrant@default:/vagrant/build/ ./build/
	rm ssh-config

gh-pages: build/tex/cv.pdf
	mkdir -p .data
	cp build/tex/cv.pdf ".data/Jorge Barata.pdf"
	cp cv.md .data/index.md
	cp cv.ext.md .data/extended.md
	git stash
	git checkout gh-pages
	mv .data/* .
	git add "Jorge Barata.pdf" index.md extended.md
	git commit -m"Automated update"
	rmdir .data
	git checkout master
	git stash apply
	@echo "Please run: git push origin gh-pages:gh-pages"

.PHONY: gh-pages
