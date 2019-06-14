sudo apt-get install git
sudo apt install docker.io

git clone https://github.com/hemanth-koganti/datascrap.git
cd ./datascrap
sudo docker volume create -d local-persist -o mountpoint=/home/ubuntu/data --name=volvol
sudo docker run -d -v volvol:/usr/src/app indeed
