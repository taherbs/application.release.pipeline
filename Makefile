# docker listener service makefile
APP_SERVICE_NAME = "applicationreleasepipeline"

.PHONY: build
build:
	docker-compose build --no-cache

.PHONY: start-new
start-new: clean build
	docker-compose up --build --remove-orphans --detach

.PHONY: start
start: stop
	docker-compose up --detach

.PHONY: stop
stop:
	docker-compose down --remove-orphans

.PHONY: ssh-php
ssh-php:
	docker exec -u 0 -it $(APP_SERVICE_NAME)_php_1 /bin/sh

.PHONY: ssh-web
ssh-web:
	docker exec -u 0 -it $(APP_SERVICE_NAME)_web_1 /bin/sh

.PHONY: tests
tests:
	docker run $(APP_SERVICE_NAME)_php:latest /bin/sh -c "sh /var/www/run_tests.sh"

.PHONY: sql
sql:
	mysql -h localhost -P 35808 --protocol=tcp -u admin -padmin

.PHONY: rm-data
rm-data:
	rm -rf ./local_data_save/* && echo "*\n!.gitignore" > ./local_data_save/.gitignore

.PHONY: delete-env
delete-env:
	cd ./aws/sceptre && sceptre delete-env feature && sceptre delete-env cd && sceptre delete-env ci && sceptre delete-env misc

.PHONY: clean
clean: stop rm-data
	docker-compose rm -f -s -v