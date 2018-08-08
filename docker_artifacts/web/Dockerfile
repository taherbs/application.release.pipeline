### Image Setup ###
FROM nginx:stable-alpine
LABEL maintainer=taherbs
ARG DOCKER_ARTIFACT_DIR=./docker_artifacts/web
ARG FCGI_HOST=127.0.0.1

### Copy project code base ###
COPY ./code /var/www

### Ngnix Cconfig ###
RUN ln -snf /usr/share/zoneinfo/Europe/Rome /etc/localtime && \
	echo Europe/Rome > /etc/timezone && \
	rm -f /etc/nginx/nginx.conf && \
	rm -fr /etc/nginx/conf.d/

COPY $DOCKER_ARTIFACT_DIR/nginx.conf /etc/nginx/
COPY $DOCKER_ARTIFACT_DIR/proxyfcgi.conf /etc/nginx/conf.d/
RUN sed -i 's/\@FCGI_HOST\@/'"$FCGI_HOST"'/' /etc/nginx/conf.d/proxyfcgi.conf

### Run the Docker command ###
WORKDIR /var/www
CMD ["nginx", "-g", "daemon off;"]

### Expose ports ###
EXPOSE 80