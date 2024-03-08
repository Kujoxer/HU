sudo swapoff /swapfile;
sudo rm /swapfile;
echo "swap del!";
free -h;
swapon --show;
sudo fallocate -l 1G /swapfile;
sudo chmod 600 /swapfile;
sudo mkswap /swapfile;
sudo swapon /swapfile;
#echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab;
sudo sysctl vm.swappiness=85;
#echo 'vm.swappiness=85' | sudo tee -a /etc/sysctl.conf
