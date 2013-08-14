#/bin/sh
sudo useradd $1
sudo passwd $1
sudo mkdir /home/$1
sudo chown -R $1:$1 /home/$1
