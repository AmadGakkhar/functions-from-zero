[![Function to Deploy](https://github.com/AmadGakkhar/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/AmadGakkhar/functions-from-zero/actions/workflows/main.yml)

# functions-from-zero

## To call Microservice

''' bash
curl -X 'POST' \
  'https://studious-adventure-9jrgqpvvqrj27wpq-8000.app.github.dev/get-info' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "page_name": "Microsoft"
}'
'''
### Build Docker Container
run
docker build -t my-fastapi-app .
docker image ls (Will list the images)
docker ps -a (Lists all docker containers)
docker run -d -p 8000:8000 my-fastapi-app (Runs image in the container)
docker logs [container id] (check container logs)


To delete all containers including its volumes use,

docker rm -vf $(docker ps -aq)

To delete all the images,

docker rmi -f $(docker images -aq)

## Invoke POST Request

Run
bash invoke.sh
