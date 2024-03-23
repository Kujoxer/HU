#! /usr/bin/bash

free -h;
swapon --show;

sudo swapoff /swapfile;
sudo rm /swapfile;
echo "swap del!";

free -h;
swapon --show;
sudo fallocate -l 1G /swapfile;
sudo chmod 600 /swapfile;
sudo mkswap /swapfile;
sudo swapon /swapfile;

# NOTE: Раскоментируй если первый раз делаешь!
#echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab;

sudo sysctl vm.swappiness=95;
#echo 'vm.swappiness=95' | sudo tee -a /etc/sysctl.conf
