# rocker/shiny served by nginx

This is a minimal example of how you can set up a shiny server serving one app with a webserver in front.
Shiny server is based on [rocker/shiny](https://hub.docker.com/r/rocker/shiny/)
and the webserver is based on [nginx](https://hub.docker.com/_/nginx/).

The whole thing should start with `docker-compose up` and you should see the minimal _shiny-bins-app_ 
from [the shiny docs](https://shiny.rstudio.com/articles/basics.html) on `localhost:80`.
