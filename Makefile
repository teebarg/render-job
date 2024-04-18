# Variables
APP_NAME := render-job
RENDER_JOB_PORT := 5000

# Targets
build:
	docker build -t $(APP_NAME) .

run:
	docker run --name $(APP_NAME) -p ${RENDER_JOB_PORT}:8000 -d $(APP_NAME)

stop:
	docker stop $(APP_NAME)
	docker rm $(APP_NAME)

stage:
	docker tag $(APP_NAME):latest beafdocker/render-job:latest
	docker push beafdocker/render-job:latest

# stop suspended dev server processes
stopDevServer:
	# Stopping Dev Server PIDs
	- @lsof -ti :${RENDER_JOB_PORT} | xargs kill -9

dev: stopDevServer
	uvicorn main:app --host 0.0.0.0 --port ${RENDER_JOB_PORT} --reload
