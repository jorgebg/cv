Vagrant.configure("2") do |config|
  config.vm.box = "debian/stretch64"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y texlive-xetex python3-pip
    cd /vagrant
    apt-get install -y $(cat apt-packages.txt)
    pip3 install -r requirements.txt
    # python3 -m cv html pdf
  SHELL
end
