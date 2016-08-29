#Getting Started with Docker

This was done on a machine running 4.4.19-1-MANJARO

##Getting Started

1. Install Docker
		sudo pacman -S docker

2. Add user to the docker group
		sudo usermod -aG docker delvison

3. Start docker service
		sudo systemctl start docker

4. Check that docker is running 
		sudo systemctl status docker

5. Test docker
		sudo docker run hello-world

6. Download ubuntu image
		docker pull ubuntu

7. run a new container with ubuntu in it and connect to it
		docker run -i -t ubuntu

8. install nodejs. nodejs-legacy needed to install the express-genearator module
		apt-get update
		apt-get install nodejs
		apt-get install nodejs-legacy 
		apt-get install npm

9. install the express generator module from npm
		npm install -g express-generator

10. exit container. list docker containers.
		docker ps -a

11. commit container and create the image
		docker commit -a "delvison &lt;delvisoncastillo@gmail.com&gt;" -m "node and express" ff10641effee  node-express:0.1
		docker tag node-express:0.1 node-express:latest

12. run a container and expose port 8080 of our host system connected to port 3000 in our container 
		mkdir mynodeapp
		docker run -it -v /home/delvison/good_uncle/mynodeapp:/mynodeapp -p 8080:3000 node-express


13. start a node app using express
		express mynodeapp
		cd mynodeapp
		npm install
		npm start

https://scotch.io/tutorials/build-a-restful-api-using-node-and-express-4

## Install docker on ubuntu ami
wget -qO- https://get.docker.com/ | sh
sudo apt-get -y install python-pip
sudo apt-get -y install python-pip
sudo pip install docker-compose


