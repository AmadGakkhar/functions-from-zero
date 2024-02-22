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
