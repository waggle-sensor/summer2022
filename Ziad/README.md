#Welcome to my README!
----------------------


This is mainly resources that I created to implement and setup the MEC server for the waglle-sensor project. There are also usefull links and courses 
that helped me to figure out some tasks.


##Install SSH server: 

###Install SSH

sudo apt-get install openssh-server

sudo apt update

sudo service ssh status

sudo service ssh start or sudo systemctl start ssh


###Create Private Key

ssh-keygen -t rsa -b 4096

cd  .ssh/

cp id_rsa.pub authorized_keys

mkdir .ssh → on the server

scp authorized_keys  username@ip_address:/home/username/.ssh

chmod 700 ~/.ssh → on the server

chmod 600~/.ssh* → on the server
