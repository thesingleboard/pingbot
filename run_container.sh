sudo docker run -d -p 9002:9002 -v /home/pi/Documents/dnsmasq-configs:/opt/pingbot --name pingbot \
-e HOSTS='/hosts' \
-e GITROOT='/opt/pingbot' \
-e GITURL='http://gitlab/jarrance/dnsmasq-configs.git'  \
pingbot