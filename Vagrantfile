# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"

  mask = "192.168.100."

  #config.vm.provision :shell, inline: "sudo apt-get update"
  #config.vm.provision :shell, inline: "sudo apt-get install git -y"

  #config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
      #vb.memory = "512"
      # Customize the amount of procesors on the VM
      #vb.cpus = 2
 # end

  config.vm.define "db" do |db|
    db.vm.provision "file", source: "./provisions/python", destination: "python-scripts" 
    db.vm.provision :shell, path: "./provisions/database-provision.sh"
    db.vm.network "private_network", ip: "#{mask}"+"41"
  end

  config.vm.define "api" do |api|
    api.vm.provision "file", source: "./sources", destination: "nginx-sources"
    api.vm.provision "file", source: "./provisions/python", destination: "python-scripts"
    api.vm.provision :shell, path: "./provisions/api-provision.sh"
    api.vm.network "private_network", ip: "#{mask}"+"42"
    api.vm.network "forwarded_port", guest: 80, host: 9001
  end

  config.vm.define "ui" do |ui|
    ui.vm.provision :shell, path: "./provisions/ui.sh"
    ui.vm.network "private_network", ip: "#{mask}"+"43"
    ui.vm.network "forwarded_port", guest: 80, host: 9003
  end

  config.vm.define "bash_api" do |bash_api|
    bash_api.vm.provision :shell, path: "./provisions/bash/setup-node.sh"
    bash_api.vm.network "private_network", ip: "#{mask}"+"42"
    bash_api.vm.network "forwarded_port", guest: 80, host: 9001
  end


end
