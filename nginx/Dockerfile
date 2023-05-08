FROM nginx:1.21.5-alpine

#COPY ./nginx/nginx.conf /etc/nginx/conf.d
RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/

# expose port
# EXPOSE 80
