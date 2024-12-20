# start by pulling the python image
FROM python:3.10-slim-buster

# copy the requirements file into the image
# COPY ./requirements.txt /app/requirements.txt
COPY requirements.txt requirements.txt

# switch working directory
# WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
# COPY . /app
COPY . .

# configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]

# CMD ["app.py" ]

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
