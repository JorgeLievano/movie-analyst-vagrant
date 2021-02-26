# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"

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
    config.vm.provision :shell, path: "./provisions/database.sh"
  end

end
