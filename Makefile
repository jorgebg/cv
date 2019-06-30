.vagrant: Vagrantfile
	vagrant up
	touch .vagrant

build/html/cv.html build/tex/cv.pdf: .vagrant cv.md
	vagrant rsync
	vagrant ssh -- "cd /vagrant && python3 -m cv html pdf"
	vagrant ssh-config > ssh-config
	rsync -e "ssh -F ssh-config" -r vagrant@default:/vagrant/build/ ./build/
	rm ssh-config
