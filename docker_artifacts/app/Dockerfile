### Image Setup ##############################
FROM php:7-fpm
LABEL maintainer=taherbs
ARG DOCKER_ARTIFACT_DIR=./docker_artifacts/app
ENV COMPOSER_ALLOW_SUPERUSER 1

### Copy php config ###
COPY $DOCKER_ARTIFACT_DIR/php.ini /usr/local/etc/php/conf.d/

### Copy project code base ###
COPY ./code /var/www

### Run the Docker command ###
WORKDIR /var/www

ENV LOG_STREAM="/tmp/stdout"
RUN mkfifo $LOG_STREAM && chmod 777 $LOG_STREAM
CMD ["/bin/sh","-c","php-fpm -R -D | tail -f $LOG_STREAM"]

### Expose ports ###
EXPOSE 9000