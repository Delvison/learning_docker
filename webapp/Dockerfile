FROM ruby:2.2.0
MAINTAINER Delvison Castillo (delvisoncastillo@gmail.com)
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
WORKDIR /webapp
ADD Gemfile /webapp/Gemfile
ADD Gemfile.lock /webapp/Gemfile.lock
RUN bundle install
EXPOSE 3000

# The main command to run when the container starts. Also
# tell the Rails dev server to bind to all interfaces by
# default.
CMD ["sh","run.sh"]
# CMD ["rake","db:migrate","&&","bundle","exec","rails","server","-b","0.0.0.0"]
