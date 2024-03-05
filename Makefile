# Variables
APP_NAME := render-job

# Targets
build:
	docker build -t $(APP_NAME) .

run:
	docker run --name $(APP_NAME) -d $(APP_NAME)

stop:
	docker stop $(APP_NAME)
	docker rm $(APP_NAME)

stage:
	docker tag $(APP_NAME):latest beafdocker/render-job:latest
	docker push beafdocker/render-job:latest