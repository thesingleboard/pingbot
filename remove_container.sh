echo "Removeing all traces of pingbot container and pingbot image"
sudo docker stop pingbot
sudo docker rm pingbot
sudo docker rmi pingbot