# base image
FROM nginx:1.21-alpine

# copy configuration files
COPY nginx.conf /etc/nginx/nginx.conf
COPY myproject.conf /etc/nginx/conf.d/

# set working directory
WORKDIR /usr/share/nginx/html

# copy static files
COPY --from=0 /code/static .

# expose port
EXPOSE 80
