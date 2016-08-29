FROM ubuntu
MAINTAINER Delvison Castillo (delvisoncastillo@gmail.com)
RUN apt-get -y update 
RUN apt-get -y install nodejs
RUN apt-get -y install nodejs-legacy 
RUN apt-get -y install npm
RUN npm install -g express-generator
WORKDIR /mynodeapp
RUN npm install 
CMD [ "npm", "start"] 

