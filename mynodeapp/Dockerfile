FROM ubuntu
MAINTAINER Delvison Castillo (delvisoncastillo@gmail.com)
RUN apt-get -y update
RUN apt-get -y install nodejs
RUN apt-get -y install nodejs-legacy
RUN apt-get -y install npm
WORKDIR /mynodeapp
RUN npm install
EXPOSE 3000
CMD [ "npm", "start"]
