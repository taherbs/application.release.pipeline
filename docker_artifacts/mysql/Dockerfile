### Image Setup ###
FROM mysql:5.7
LABEL maintainer=taherbs
ARG DOCKER_ARTIFACT_DIR=./docker_artifacts/mysql
ARG MYSQL_DATABASE=db
ARG MYSQL_USER=admin
ARG MYSQL_PASSWORD=admin
ARG MYSQL_ROOT_PASSWORD=admin

### MySql Config ###
ADD $DOCKER_ARTIFACT_DIR/startup /etc/mysql/startup
ADD $DOCKER_ARTIFACT_DIR//my.cnf /etc/mysql/conf.d/my.cnf

RUN chown -R mysql:root /var/lib/mysql/

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

RUN sed -i 's/MYSQL_DATABASE/'$MYSQL_DATABASE'/g' /etc/mysql/startup && \
    sed -i 's/MYSQL_USER/'$MYSQL_USER'/g' /etc/mysql/startup && \
    sed -i 's/MYSQL_PASSWORD/'$MYSQL_PASSWORD'/g' /etc/mysql/startup

### Initialize DB ###
CMD ["mysqld", "--init-file=/etc/mysql/startup"]

### Expose ports ###
EXPOSE 3306