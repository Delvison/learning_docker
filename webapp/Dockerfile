FROM ruby:2.2.0
MAINTAINER Delvison Castillo (delvisoncastillo@gmail.com)
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
WORKDIR /webapp
ADD Gemfile /webapp/Gemfile
ADD Gemfile.lock /webapp/Gemfile.lock
RUN bundle install
CMD [ "rails", "s"]
