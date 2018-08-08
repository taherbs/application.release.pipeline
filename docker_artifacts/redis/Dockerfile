### Image Setup ###
FROM redis:latest
LABEL maintainer=taherbs
ARG DOCKER_ARTIFACT_DIR=./docker_artifacts/redis

## For security settings uncomment, make the dir, copy conf, and also start with the conf, to use it
#RUN mkdir -p /usr/local/etc/redis
#COPY redis.conf /usr/local/etc/redis/redis.conf

VOLUME /data


#CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
CMD ["redis-server"]

### Expose ports ###
EXPOSE 6379