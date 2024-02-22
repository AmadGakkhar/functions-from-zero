FROM public.ecr.aws/lambda/python:3.10
RUN mkdir -p /app 
COPY ./app.py /app/
COPY ./requirements.txt /app/requirements.txt
COPY ./utils /app/utils
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8000
CMD ["app:app"
, "--host", "0.0.0.0", "--port", "8000"]

ENTRYPOINT [ "uvicorn" ]