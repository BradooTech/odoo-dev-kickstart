# -*- mode: ruby -*-
# vi: set ft=ruby :

USER = "ubuntu"

$runserver = <<SCRIPT
    # must run with vagrant user
    # cd /vagrant
    cd /home/ubuntu/odoo/odoo

    tmux -2 new-session -d -s odoo -n 'odoo'
    tmux send-keys "./odoo-bin --config=odoo-config" C-m

SCRIPT

ENV['VAGRANT_DEFAULT_PROVIDER']="virtualbox"

Vagrant.configure('2') do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 8069, host: 8069
  config.vm.network "forwarded_port", guest: 5432, host: 5432 

  config.vm.provision :shell, 
	  path: "scripts/bootstrap-odoo.sh", 
	  privileged: false, 
	  keep_color: true

  config.vm.provision "shell",
           inline: $runserver,
           privileged: false,
           run: "always"
  
  config.ssh.forward_agent = true
  config.ssh.insert_key = true
  config.ssh.username = USER

  config.vm.provider "virtualbox" do |v|
    	v.memory = 1024
     	v.cpus = 2
  end

  config.vm.synced_folder "./odoo", "/home/" + USER  + "/odoo/", create: true
  config.vm.synced_folder "./custom-addons", "/home/" + USER  + "/odoo-modules/", create: true
end

